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

class OptionError:
    def __init__(self, msg):
        self.args = msg
        self.errmsg = msg

class RunTestsError:
    def __init__(self, msg):
        self.args = msg
        self.errmsg = msg

class RunTests:
    def __init__(self):
        self.parameters = {}
        self.parameters['tfn'] = 'tstorm.ini'
        try:
            storm_release = release.Release(__import__('tstorm').get_storm_release())
        except release.ReleaseError, err:
            print '\n\nExecution: ', err
            self.usage()
            sys.exit(2)
        self.parameters['voms'] = True
        self.parameters['report'] = True
        self.parameters['custom_destination_file'] = (False, '')
        self.parameters['tests_sequence'] = (False, [])
        self.parameters['tests_sequence_file']= (False, '')
        self.parameters['list_tests_details'] = (False, {})
        self.parameters['filter_tests_details'] = (False, {})
        self.parameters['valid_tests'] = {}
        if settings.configuration_file_exists(file_name = 'map_tests_ids.json'):
            '''Get Test Id Mapping Info from file'''
            self.parameters['mti_info'] =  settings.get_json_file_information(file_name = 'map_tests_ids.json')
        else:
            raise RunTestsError("map-tests-ids.json file is not in the right location")
        self.tests_instance = tests.Tests(self.parameters['mti_info']) 

    def __usage(self):
        print """Usage: tstorm-tests [-h|--help] [-v|--version] [-c|--conf] """
        print """                    [-d|--destfile] [-i|--ids] [-f|--file-ids] """
        print """                    [--noreport] [--novoms]"""
        print """                    [-s|--filter-list] [-l|--list]"""
        print """                    [-r|--storm-release]"""
        print """where:"""
        print """- version, noreport, novoms and list are not followed by any"""
        print """  values"""
        print """- conf, destfile, storm-release and file-ids are followed by """
        print """  a value """
        print """- ids is followed by a sequence of id values separated by , """
        print """  and between '"""
        print """- filter-list is followed by a sequence of values separated """
        print """  by ; and between ', the values of which are"""
        print """  t|test=sequence of types of tests separated by , as """
        print """      (AT,UT,ST,DT) that filters in relation with the """
        print """      the type of test"""
        print """  r|regression=false|true that expresses if the test """
        print """      belongs to the regression category"""
        print """  idenpotent=false|true that expresses if the test belongs """
        print """      to the idenpotent category"""
        print """  o|output=filename that allows user to save ids in the """
        print """      specified filename"""
        print """  f|format=n|name,d|description,range,rfc,i|id,idenpotent that """
        print """      allows user to specify the order of print of test """
        print """      information""",
        print """Example: if you want to run tests without producing a report"""
        print """      tstorm-tests --noreport"""
        print """Example: if you want to run tests providing tests sequence"""
        print """      tstorm-tests -i '<id1>, <id2>, ...'"""
        print """Example: if you want to get tests information providing a """
        print """filter"""
        print """      tstorm-tests --filter-list 't=AT,UT,ST;regression=true;f=n,d,rfc,id'"""

    def __verify_conf_file(self):
        if settings.configuration_file_exists(file_name = self.parameters['tfn']):
            self.parameters['tfn'] = settings.get_configuration_file(file_name = self.parameters['tfn'])
        else:
            raise RunTestsError("ini file is not in the right location")

        check_configuration_file = configuration.LoadConfiguration(conf_file = self.parameters['tfn'])
        if not check_configuration_file.is_configuration_file_valid():
            print '''Example of ini configuration file:\n'''
            check_configuration_file.print_configuration_file_template()
            raise RunTestsError("Wrong Test Configuration file")

    def __parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvlc:d:i:f:s:r:",
                ["help","noreport","novoms","list", "conf=","destfile=",
                "ids=","file-ids=","version","filter-list=",
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
            elif opt in ("-c", "--conf"):
                self.parameters['tfn'] = value
            elif opt in ("-d", "--destfile"):
                self.parameters['custom_destination_file'] = (True, value)
            elif opt in ("-i", "--ids"):
                try:
                    tmp_sequence_tests = sequence.Sequence(value).get_sequence()
                    self.parameters['tests_sequence'] = (True, tmp_sequence_tests)
                except sequence.SequenceError, err:
                    print '\n\nExecution: ', err
                    self.__usage()
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
                    self.__usage()
                    sys.exit(2)
            elif opt in ("-r", "--storm-release"):
                try:
                    self.parameters['storm_release'] = release.Release(value)
                except release.ReleaseError, err:
                    print '\n\nExecution: ', err
                    self.__usage()
                    sys.exit(2)
            elif opt in ("--novoms"):
                self.parameters['voms'] = False
            elif opt in ("--noreport"):
                self.parameters['report'] = False
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

    def __set_valid_tests(self):
        self.parameters['valid_tests'] = self.tests_instance.get_valid_tests(release)
   
    def __modify_valid_tests(self):
        new_valid_tests = {}
        for key, value in self.parameters['valid_tests']:
            if value.get_id() in self.parameters['tests_sequence']:
                new_valid_tests[key] = value
        return new_valid_tests
 
    def do_pre_run(self):
        self.__parse()
        self.__set_valid_tests()

        if self.parameters['list_tests_details'][0]:
            self.tests_instance.get_info()
            sys.exit(0)
        if self.parameters['filter_tests_details'][0]:
            self.tests_instance.get_info(info=self.parameters['filter_tests_details'][1])
            sys.exit(0)

        if self.parameters['tests_sequence_file'][0]:
            if settings.file_exists(sel.parameters['tests_sequence_file'][1]):
                self.parameters['tests_sequence'] = (True,
                   self.parameters['tests_sequence'][1] + settings.get_tests_sequence(self.parameters['tests_sequence_file'][1]))
            else:
                raise RunTestsErrors("File that contains tests sequence does not exist")

        if self.parameters['tests_sequence'][0]:
            if not settings.is_tests_sequence_valid(self.parameters['tests_sequence'][1],
                self.parameters['mti_info'].values()):
                raise RunTestsErrors("Wrong Tests Sequence")

        if self.parameters['tests_sequence'][0]:
            self.parameters['valid_tests'] = self.__modify_valid_tests()

    def do_run_tests(self):

        log_file = report_file.ReportFile(report = self.parameters['report'])

        tests_methods = self.tests_instance.get_methods(tests = self.parameters['valid_tests'])

        for key, value in tests_methods.items():
            self.__run_tests(self.parameters['tfn'], \
                value, log_file, key,
                self.parameters['custom_destination_file'][0], \
                self.parameters['custom_destination_file'][1])

        log_file.close_file()
