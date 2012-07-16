#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import sys
import unittest
import getopt
import exceptions
from tstorm.run import run_tests

#from tstorm.utils import report_file 
#from tstorm.utils import settings

#from tstorm.utils import sequence
#from tstorm.utils import release
#from tstorm.utils import range
#from tstorm.utils import limit
#from tstorm.utils import test
#from tstorm.utils import tests
#from tstorm.utils import filters
#from tstorm.utils import configuration

#from tstorm.tests import commontests as cts
#from tstorm.tests.atomic import atomicstests as at
#from tstorm.tests.functional import functionalitiestests as ft
#from tstorm.tests.functional import functionalitiestests_novoms as ftnv
#from tstorm.tests.functional import tapetests as tt
#from tstorm.tests.functional.regression import regressiontests as rt
#from tstorm.tests.functional.regression import regressiontests_novoms as rtnv

class RunStressTestsError(exceptions.Exception):
    pass

class RunStressTests(run_tests.RunTestss):
    def __init__(self):
        super(run_tests.RunTestss, self).__init__()
        self.parameters['tfn'] = 'tstorm-stress-tests.ini'
        self.parameters['stress_report'] = True
        self.parameters['number_cycles'] = 100

    def __usage_nostressreport(self,opt=True):
        if not opt:
            print """- nostressreport is not followed by any value"""
        else:
            print """                   [--nostressreport] """

    def __usage_number_cycles(self,opt=True):
        if not opt:
            print """- number-cycles is followed by a value"""
        else:
            print """                   [-n|--number-cycles] """ 

    def __usage(self):
        print """Usage: tstorm-stress-test [-h|--help] """
        self.__usage_version()
        self.__usage_noreport()
        self.__usage_nostressreport()
        self.__usage_number_cycles()
        self.__usage_storm_release()
        print """where:"""
        self.__usage_version(opt=False)
        self.__usage_noreport(opt=False)
        self.__usage_nostressreport(opt=False)
        self.__usage_number_cycles(opt=False)
        self.__usage_storm_release(opt=False)
        self.__usage_example_noreport()
        self.__usage_example_number_cycles()

    def __parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvn:r:",
                ["help","noreport","nostressreport",
                 "version","number-cycles=",
                 "storm-release="])
        except getopt.GetoptError, err:
            print str(err)
            self.__usage()
            sys.exit(2)

        for opt, value in opts:
            if opt in ("-h", "--help"):
                self.__usage()
                sys.exit(0)
            elif opt in ("-v", "--version"):
                msg = 'T-StoRM version %s' % (__import__('tstorm').get_version())
                print msg
                sys.exit(0)
            elif opt in ("-n", "--number-cycles"):
                self.parameters['number-cycles'] = int(value)
            elif opt in ("-r", "--storm-release"):
                try:
                    self.parameters['storm_release'] = release.Release(value)
                except release.ReleaseError, err:
                    print '\n\nExecution: ', err
                    self.__usage()
                    sys.exit(2)
            elif opt in ("noreport"):
                self.parameters['report'] = False
            elif opt in ("nostressreport"):
                self.parameters['stress_report'] = False
            else:
                raise run_tests.OptionError("Unhandled option")

        self.__verify_conf_file()

    def __run_test(self, tfn, uid, lfn, tt):
        sd=True
        if uid.is_regression():
            sd=False
        elif 'ts_https' in uid.get_aggregator():
            sd=False
        elif 'ts_http' in uid.get_aggregator():
            sd=False
        elif 'ts_https_voms' in uid.get_aggregator():
            sd=False
        ifn,dfn,back_ifn= settings.set_inpt_fn(n_df,n_dfn,subdir=sd)
        if uid.get_aggregator() != "" and uid.is_idenpotent():
            lfn.put_name(uid.get_name())
            lfn.put_description(uid.get_description())
            lfn.put_uuid(uid.get_id())
            if uid.is_regression():
                lfn.put_ruid(uid.get_rfc())
            lfn.put_output()
            runner = unittest.TextTestRunner(verbosity=2).run(eval(uid.get_aggregator()))
            lfn.put_prologue()

#    def do_pre_run(self):
#        self.__parse()
#        self.__set_valid_tests()

    def do_run_tests(self):

        log_file = report_file.ReportFile(report = self.parameters['report'])
        self.stress_instance = stress_file.StressReportFile(report = self.parameters['stress_report'])

        tests_methods = self.tests_instance.get_methods(tests = self.parameters['valid_tests'])

        for key, value in tests_methods.items():
            if not value.is_regression() and value.is_idenpotent():
                self.__run_test(self.parameters['tfn'],
                    value, log_file, key)

        log_file.close_file()
        self.stress_instance.close_file()
