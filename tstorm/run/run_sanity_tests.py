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

from tstorm.tests.deployment import conftests as ct
from tstorm.tests.deployment.regression import regression_conftests as rct
from tstorm.tests.deployment.regression import regression_infotests as rit

class RunSanityTestsError(exceptions.Exception):
    pass

class RunSanityTests(run_tests.RunTests):
    def __init__(self):
        super(RunSanityTests, self).__init__()
        self.parameters['custom_conf_file'] = (False, 'tstorm-sanity.ini')
        self.parameters['voms'] = False

    def do_parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvlc:i:f:s:r:",
                ["help","noreport","list", "conf=",
                 "ids=","file-ids=","version","filter-list=",
                 "storm-release="])
        except getopt.GetoptError, err:
            print str(err)
            usage.get_usage(self.parameters, run='sanity')
            sys.exit(2)

        for opt, value in opts:
            if opt == "-h" or opt == "--help":
                usage.get_usage(self.parameters, run='sanity')
                sys.exit(0)
            elif opt == "-v" or opt == "--version":
                msg = 'T-StoRM version %s' % (__import__('tstorm').get_version())
                print msg
                sys.exit(0)
            elif opt == "-c" or opt == "--conf":
                self.parameters['custom_conf_file'] = (True, value)
            elif opt == "-i" or opt == "--ids":
                try:
                    tmp_sequence_tests = sequence.Sequence(value).get_sequence()
                    self.parameters['tests_sequence'] = (True, tmp_sequence_tests)
                except sequence.SequenceError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(self.parameters, run='sanity')
                    sys.exit(2)
            elif opt == "-f" or opt == "--file-ids":
                self.parameters['tests_sequence_file'] = (True, value)
            elif opt == "-l" or opt == "--list":
                self.parameters['list_tests_details'] = (True, {})
            elif opt == "-s" or opt == "--filter-list":
                try:
                    tmp_filter_tests_details = filters.Filters(value).get_filters(run='sanity')
                    self.parameters['filter_tests_details'] = (True, tmp_filter_tests_details)
                except filters.FiltersError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(self.parameters, run='sanity')
                    sys.exit(2)
            elif opt == "-r" or opt == "--storm-release":
                try:
                    self.parameters['storm_release'] = release.Release(value)
                except release.ReleaseError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(self.parameters, run='sanity')
                    sys.exit(2)
            elif opt == "--noreport":
                self.parameters['report'] = False
            else:
                raise run_tests.OptionError("Unhandled option")

    def run_test(self, tfn, uid, lfn):
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
            self.tests_instance.get_info(node=self.parameters['node'],run='sanity')
            sys.exit(0)
        if self.parameters['filter_tests_details'][0]:
            self.tests_instance.get_info(info=self.parameters['filter_tests_details'][1],node=self.parameters['node'],run='sanity')
            sys.exit(0)

    def do_run_tests(self):
        log_file = report_file.ReportFile(report = self.parameters['report'])

        tests_methods = self.tests_instance.get_methods(tests = self.parameters['valid_tests'],node=self.parameters['node'],run='sanity')

        for key, value in tests_methods.items():
            self.run_test(self.parameters['custom_conf_file'][1], \
                value, log_file)

        log_file.close_file()
