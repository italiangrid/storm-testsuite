#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import sys
import unittest
import getopt

from tstorm.utils import report_file 
from tstorm.utils import settings

from tstorm.utils import sequence
from tstorm.utils import release
from tstorm.utils import range
from tstorm.utils import limit
from tstorm.utils import test
from tstorm.utils import tests
from tstorm.utils import filters
from tstorm.utils import configuration

from tstorm.tests import commontests as cts
from tstorm.tests.atomic import atomicstests as at
from tstorm.tests.functional import functionalitiestests as ft
from tstorm.tests.functional import functionalitiestests_novoms as ftnv
from tstorm.tests.functional import tapetests as tt
from tstorm.tests.functional.regression import regressiontests as rt
from tstorm.tests.functional.regression import regressiontests_novoms as rtnv

class RunStressTestsError:
    def __init__(self, msg):
        self.args = msg
        self.errmsg = msg

class RunStressTests(run_tests.RunTests):
    def __init__(self):
        super(run_tests.RunTests, self).__init__()
        self.parameters['tfn'] = 'tstorm-stress-tests.ini'
        self.parameters['stfn'] = 'tstorm-performed-stress-tests.ini'
        self.parameters['report'] = False
        self.parameters['cycles'] = 100
        if settings.configuration_file_exists(file_name = 'map_tests_ids.json'):
            '''Get Test Id Mapping Info from file'''
            self.parameters['mti_info'] =  settings.get_json_file_information(file_name = 'map_tests_ids.json')
        else:
            raise RunTestsError("map-tests-ids.json file is not in the right location")
        self.tests_instance = tests.Tests(self.parameters['mti_info']) 

    def __usage(self):
        print """Usage: tstorm-stress-tests [-h|--help] [-v|--version] """
        print """                    [-c|--cycles] """
        print """                    [--report] """
        print """                    [-r|--storm-release]"""
        print """where:"""
        print """- version and report are not followed by any"""
        print """  values"""
        print """- storm-release is followed by """
        print """  a value """
        print """Example: if you want to run tests  producing a report"""
        print """      tstorm-tests --report"""
        print """Example: if you want to run tests for a certain number"""
        print """      tstorm-tests -c 10000'"""

    def __parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvlc:r:",
                ["help","report","cycles=",
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
            elif opt in ("-c", "--cycles"):
                self.parameters['cycles'] = value
            elif opt in ("-r", "--storm-release"):
                try:
                    self.parameters['storm_release'] = release.Release(value)
                except release.ReleaseError, err:
                    print '\n\nExecution: ', err
                    self.__usage()
                    sys.exit(2)
            elif opt in ("report"):
                self.parameters['report'] = True
            else:
                raise OptionError("Unhandled option")

        self.__verify_conf_file()

     def __run_tests(self, tfn, uid, lfn, tt, n_df, n_dfn):
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
        if uid.get_aggregator() != "":
            lfn.put_name(uid.get_name())
            lfn.put_description(uid.get_description())
            lfn.put_uuid(uid.get_id())
            if uid.is_regression():
                lfn.put_ruid(uid.get_rfc())
            lfn.put_output()
            runner = unittest.TextTestRunner(verbosity=2).run(eval(uid.get_aggregator()))
            lfn.put_prologue()

    def do_pre_run(self):
        self.__parse()
        self.__set_valid_tests()

    def do_run_tests(self):

        log_file = report_file.ReportFile(report = self.parameters['report'])
        stress_log_file = stress_report_file.StressReportFile(

        tests_methods = self.tests_instance.get_methods(tests = self.parameters['valid_tests'])

        for key, value in tests_methods.items():
            if not value.is_regression() and value.is_idenpotent():
                self.__run_tests(self.parameters['tfn'], \
                    value, log_file, key)

        log_file.close_file()
        stress_log_file.close_file()
