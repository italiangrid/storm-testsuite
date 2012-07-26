#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import sys
import unittest
import getopt
import exceptions
import random

from tstorm.run import run_tests

from tstorm.utils import stress_file
from tstorm.utils import report_file
from tstorm.utils import settings
from tstorm.utils import usage
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
from tstorm.tests.functional.regression import regression_ldaptests as rlt

class RunStressTestsError(exceptions.Exception):
    pass

class RunStressTests(run_tests.RunTests):
    def __init__(self):
        super(RunStressTests, self).__init__()
        self.parameters['report'] = False
        self.parameters['stress_report'] = True
        self.parameters['number_cycles'] = 2
        self.parameters['number_hours'] = 2
        self.parameters['refresh_report'] = 2

    def do_parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvn:r:",
                ["help","nostressreport",
                 "version","number-cycles=",
                 "number-hours=","refresh-report="
                 "storm-release="])
        except getopt.GetoptError, err:
            print str(err)
            usage.get_usage(run='stress')
            sys.exit(2)

        for opt, value in opts:
            if opt in ("-h", "--help"):
                usage.get_usage(run='stress')
                sys.exit(0)
            elif opt in ("-v", "--version"):
                msg = 'T-StoRM version %s' % (__import__('tstorm').get_version())
                print msg
                sys.exit(0)
            elif opt in ("-n", "--number-cycles"):
                self.parameters['number_cycles'] = int(value)
            elif opt in ("--number-hours"):
                self.parameters['number_hours'] = int(value)
            elif opt in ("--refresh-report"):
                self.parameters['refresh_report'] = int(value)
            elif opt in ("-r", "--storm-release"):
                try:
                    self.parameters['storm_release'] = release.Release(value)
                except release.ReleaseError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(run='stress')
                    sys.exit(2)
            elif opt in ("--nostressreport"):
                self.parameters['stress_report'] = False
            else:
                raise run_tests.OptionError("Unhandled option")

    def run_test(self, tfn, uid, lfn, tt, n_df,n_dfn):
        sd=True
        if 'ts_https' in uid.get_aggregator() or \
           'ts_http' in uid.get_aggregator() or \
           'ts_https_voms' in uid.get_aggregator() or \
           '_https_' in uid.get_aggregator() or \
           '_http_' in uid.get_aggregator() or \
           '_https' in uid.get_aggregator() or \
           '_http' in uid.get_aggregator():
            sd=False
        ifn,dfn,back_ifn= settings.set_inpt_fn(n_df,n_dfn,subdir=sd)
        if uid.get_aggregator() != "" and \
            ('_wo' not in uid.get_aggregator() or \
            '_glueone' not in uid.get_aggregator() or \
            '_gluetwo' not in uid.get_aggregator()):
            lfn.put_name(uid.get_name())
            lfn.put_description(uid.get_description())
            lfn.put_uuid(uid.get_id())
            if uid.is_regression():
                lfn.put_ruid(uid.get_rfc())
            lfn.put_output()
            runner = unittest.TextTestRunner(verbosity=2).run(eval(uid.get_aggregator()))
            lfn.put_prologue()

    def do_run_tests(self):

        log_file = report_file.ReportFile(report = self.parameters['report'])
        self.stress_instance = stress_file.StressReportFile(report = self.parameters['stress_report'])

        tests_methods = self.tests_instance.get_methods(tests = self.parameters['valid_tests'],run='stress')

        #print tests_methods.keys()
        tests_status = {}
        tests_status = tests_status.fromkeys(tests_methods, (False,0))

        while False in [x[0] for x in tests_status.values()]:
            count = 0
            test_index = random.choice([n for n,x in enumerate(tests_methods.items())])
            while count < self.parameters['number_cycles']:
                self.run_test(self.parameters['tfn'],
                    tests_methods.items()[test_index][1], log_file, tests_methods.items()[test_index][0],
                    self.parameters['custom_destination_file'][0], \
                    self.parameters['custom_destination_file'][1])
                count += 1
            tests_status[tests_status.items()[test_index][0]]=(True, tests_status.items()[test_index][1][1]+count)

        print tests_status
        if self.parameters['report']:
            log_file.close_file()
        self.stress_instance.close_file()
