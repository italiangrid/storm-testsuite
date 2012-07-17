#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import sys
import unittest
import getopt
import exceptions

from tstorm.run import run_tests

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

from tstorm.tests.deployment.regression import regression_conftests as rct
from tstorm.tests.deployment.regression import regression_ldaptests as rlt

class RunSanityTestsError(exceptions.Exception):
    pass

class RunSanityTests(run_tests.RunTests):
    def __init__(self):
        super(RunSanityTests, self).__init__()
        self.parameters['tfn'] = 'tstorm-sanity.ini'
        self.parameters['voms'] = False

    def parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvlc:i:f:s:r:",
                ["help","noreport","list", "conf=",
                 "ids=","file-ids=","version","filter-list=",
                 "storm-release="])
        except getopt.GetoptError, err:
            print str(err)
            usage.get_usage(run='sanity')
            sys.exit(2)

        for opt, value in opts:
            if opt in ("-h", "--help"):
                usage.get_usage(run='sanity')
                sys.exit(0)
            elif opt in ("-v", "--version"):
                msg = 'T-StoRM version %s' % (__import__('tstorm').get_version())
                print msg
                sys.exit(0)
            elif opt in ("-c", "--conf"):
                self.parameters['tfn'] = value
            elif opt in ("-i", "--ids"):
                try:
                    tmp_sequence_tests = sequence.Sequence(value).get_sequence()
                    self.parameters['tests_sequence'] = (True, tmp_sequence_tests)
                except sequence.SequenceError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(run='sanity')
                    sys.exit(2)
            elif opt in ("-f", "--file-ids"):
                self.parameters['tests_sequence_file'] = (True, value)
            elif opt in ("-l", "--list"):
                self.parameters['list_tests_details'] = (True, {})
            elif opt in ("-s", "--filter-list"):
                try:
                    tmp_filter_tests_details = filters.Filters(value).get_filters(run='sanity')
                    self.parameters['filter_tests_details'] = (True, tmp_filter_tests_details)
                    print self.parameters['filter_tests_details']
                except filters.FiltersError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(run='sanity')
                    sys.exit(2)
            elif opt in ("-r", "--storm-release"):
                try:
                    self.parameters['storm_release'] = release.Release(value)
                except release.ReleaseError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(run='sanity')
                    sys.exit(2)
            elif opt in ("--noreport"):
                self.parameters['report'] = False
            else:
                raise run_tests.OptionError("Unhandled option")

    def run_test(self, tfn, uid, lfn, tt):
        if uid.get_aggregator() != "":
            lfn.put_name(uid.get_name())
            lfn.put_description(uid.get_description())
            lfn.put_uuid(uid.get_id())
            if uid.is_regression():
                lfn.put_ruid(uid.get_rfc())
            lfn.put_output()
            runner = unittest.TextTestRunner(verbosity=2).run(eval(uid.get_aggregator()))
            lfn.put_prologue()

    def do_list(self):
        if self.parameters['list_tests_details'][0]:
            self.tests_instance.get_info(run='sanity')
            sys.exit(0)
        if self.parameters['filter_tests_details'][0]:
            self.tests_instance.get_info(info=self.parameters['filter_tests_details'][1],run='sanity')
            sys.exit(0)

    def do_run_tests(self):
        log_file = report_file.ReportFile(report = self.parameters['report'])
        tests_methods = self.tests_instance.get_methods(tests = self.parameters['valid_tests'],run='sanity')
        for key, value in tests_methods.items():
            self.run_test(self.parameters['tfn'], \
                value, log_file, key)
        log_file.close_file()
