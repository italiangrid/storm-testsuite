#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import sys
import unittest
import getopt
import exceptions

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
from tstorm.tests.load import loadstests as lt

class OptionError(exceptions.Exception):
    pass

class RunTestsError(exceptions.Exception):
    pass

class RunTests(object):
    def __init__(self):
        self.parameters = {}
        self.parameters['custom_conf_file'] = (False, 'tstorm.ini')
        try:
            storm_release = release.Release(__import__('tstorm').get_storm_release())
        except release.ReleaseError, err:
            print '\n\nExecution: ', err
            usage.get_usage(self.parameters)
            sys.exit(2)
        self.parameters['storm_release'] = storm_release
        self.parameters['voms'] = True
        self.parameters['report'] = True
        self.parameters['custom_destination_file'] = (False, '')
        self.parameters['tests_sequence'] = (False, [])
        self.parameters['tests_sequence_file']= (False, '')
        self.parameters['list_tests_details'] = (False, {})
        self.parameters['filter_tests_details'] = (False, {})
        self.parameters['valid_tests'] = {}
        self.parameters['node'] = []
        if settings.configuration_file_exists(file_name = 'map_tests_ids.json'):
            '''Get Test Id Mapping Info from file'''
            self.parameters['mti_info'] =  settings.get_json_file_information(file_name = 'map_tests_ids.json')
        else:
            raise RunTestsError("map-tests-ids.json file is not in the right location")
        self.tests_instance = tests.Tests(self.parameters['mti_info'])

    def verify_conf_file(self):
        if self.parameters['custom_conf_file'][0]:
            if settings.file_exists(self.parameters['custom_conf_file'][1]):
                self.parameters['custom_conf_file'] = (True, settings.get_custom_configuration_file(file_name=self.parameters['custom_conf_file'][1]))
            else:
                raise RunTestsError("ini file is not in the right location")
        else:
            if settings.configuration_file_exists(file_name = self.parameters['custom_conf_file'][1]):
                self.parameters['custom_conf_file'] = (False, settings.get_configuration_file(file_name = self.parameters['custom_conf_file'][1]))
            else:
                raise RunTestsError("ini file is not in the right location")

        check_configuration_file = configuration.LoadConfiguration(conf_file = self.parameters['custom_conf_file'][1])
        if not check_configuration_file.is_configuration_file_valid():
            print '''Example of ini configuration file:\n'''
            check_configuration_file.print_configuration_file_template()
            raise RunTestsError("Wrong Test Configuration file")
        for key, value in check_configuration_file.get_test_settings()['node'].items():
            if value.lower() == 'yes':
                self.parameters['node'].append(key)

    def do_parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvlc:d:i:f:s:r:",
                ["help","noreport","novoms","list", "conf=","destfile=",
                "ids=","file-ids=","version","filter-list=",
                "storm-release="])
        except getopt.GetoptError, err:
            print str(err)
            usage.get_usage(self.parameters)
            sys.exit(2)

        for opt, value in opts:
            if opt in ("-h", "--help"):
                usage.get_usage(self.parameters)
                sys.exit(0)
            elif opt in ("-v", "--version"):
                msg = 'T-StoRM version %s' % (__import__('tstorm').get_version())
                print msg
                sys.exit(0)
            elif opt in ("-c", "--conf"):
                self.parameters['custom_conf_file'] = (True, value)
            elif opt in ("-d", "--destfile"):
                self.parameters['custom_destination_file'] = (True, value)
            elif opt in ("-i", "--ids"):
                try:
                    tmp_sequence_tests = sequence.Sequence(value).get_sequence()
                    self.parameters['tests_sequence'] = (True, tmp_sequence_tests)
                except sequence.SequenceError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(self.parameters)
                    sys.exit(2)
            elif opt in ("-f", "--file-ids"):
                self.parameters['tests_sequence_file'] = (True, value)
            elif opt in ("-l", "--list"):
                self.parameters['list_tests_details'] = (True, {})
            elif opt in ("-s", "--filter-list"):
                try:
                    tmp_filter_tests_details = filters.Filters(value).get_filters()
                    self.parameters['filter_tests_details'] = (True, tmp_filter_tests_details)
                except filters.FiltersError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(self.parameters)
                    sys.exit(2)
            elif opt in ("-r", "--storm-release"):
                try:
                    self.parameters['storm_release'] = release.Release(value)
                except release.ReleaseError, err:
                    print '\n\nExecution: ', err
                    usage.get_usage(self.parameters)
                    sys.exit(2)
            elif opt in ("--novoms"):
                self.parameters['voms'] = False
            elif opt in ("--noreport"):
                self.parameters['report'] = False
            else:
                raise OptionError("Unhandled option")

    def run_test(self, tfn, uid, lfn, n_df, n_dfn):
        sd=True
        if uid.is_regression():
            sd=False
        elif 'ts_https' in uid.get_aggregator() or \
           'ts_http' in uid.get_aggregator() or \
           'ts_https_voms' in uid.get_aggregator() or \
           '_https_' in uid.get_aggregator() or \
           '_http_' in uid.get_aggregator() or \
           '_https' in uid.get_aggregator() or \
           '_http' in uid.get_aggregator():
            sd=False
        ifn,dfn,back_ifn= settings.set_inpt_fn(n_df,n_dfn,path=lfn.get_path(),subdir=sd)
        if uid.get_aggregator() != "" and '_wo' not in uid.get_aggregator():
            lfn.put_name(uid.get_name())
            lfn.put_description(uid.get_description())
            lfn.put_uuid(uid.get_id())
            if uid.is_regression():
                lfn.put_ruid(uid.get_rfc())
            lfn.put_output()
            runner = unittest.TextTestRunner(verbosity=2).run(eval(uid.get_aggregator()))
            lfn.put_prologue()

    def set_valid_tests(self):
        self.parameters['valid_tests'] = self.tests_instance.get_valid_tests(self.parameters['storm_release'])
   
    def modify_valid_tests(self):
        if self.parameters['tests_sequence_file'][0]:
            if settings.file_exists(self.parameters['tests_sequence_file'][1]):
                self.parameters['tests_sequence'] = (True,
                   self.parameters['tests_sequence'][1] + settings.get_tests_sequence(self.parameters['tests_sequence_file'][1]))
            else:
                raise RunTestsError("File that contains tests sequence does not exist")

        if self.parameters['tests_sequence'][0]:
            if not settings.is_tests_sequence_valid(self.parameters['tests_sequence'][1],
                self.parameters['mti_info'].values()):
                raise RunTestsError("Wrong Tests Sequence")

        new_valid_tests = {}
        for x in self.parameters['tests_sequence'][1]:
            for key, value in self.parameters['valid_tests'].items():
                if x == value.get_id():
                    new_valid_tests[key] = value
                    #print new_valid_tests[key], key, value
                    break
        return new_valid_tests

    def do_pre_run(self):
        self.verify_conf_file()
        self.set_valid_tests()
        if self.parameters['tests_sequence'][0]:
            self.parameters['valid_tests'] = self.modify_valid_tests()

        if self.parameters['tests_sequence_file'][0]:
            self.parameters['valid_tests'] = self.modify_valid_tests()

    def do_list(self):
        if self.parameters['list_tests_details'][0]:
            self.tests_instance.get_info(node=self.parameters['node'])
            sys.exit(0)
        if self.parameters['filter_tests_details'][0]:
            self.tests_instance.get_info(node=self.parameters['node'], info=self.parameters['filter_tests_details'][1])
            sys.exit(0)

    def do_run_tests(self):

        log_file = report_file.ReportFile(report = self.parameters['report'])

        tests_methods = self.tests_instance.get_methods(tests = self.parameters['valid_tests'], node=self.parameters['node'])

        for key, value in tests_methods.items():
            self.run_test(self.parameters['custom_conf_file'][1], \
                value, log_file, \
                self.parameters['custom_destination_file'][0], \
                self.parameters['custom_destination_file'][1])

        log_file.close_file()
