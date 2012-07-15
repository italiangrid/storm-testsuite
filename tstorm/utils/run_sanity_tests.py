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
from tstorm.utils import run_tests

from tstorm.tests.deployment.regression import regression_conftests as rct
from tstorm.tests.deployment.regression import regression_ldaptests as rlt

class RunSanityTestsError:
    def __init__(self, msg):
        self.args = msg
        self.errmsg = msg

class RunSanityTests(run_tests.RunTests):
    def __init__(self):
        super(run_tests.RunTests, self).__init__()
        self.parameters['tfn'] = 'tstorm-sanity.ini'
        self.parameters['voms'] = False

    def __usage(self):
        print """Usage: tstorm-sanity-tests [-h|--help] [-v|--version] """
        print """                    [-c|--conf] """
        print """                    [-i|--ids] [-f|--file-ids] """
        print """                    [--noreport]"""
        print """                    [-s|--filter-list] [-l|--list]"""
        print """                    [-r|--storm-release]"""
        print """where:"""
        print """- version, noreport and list are not followed by any"""
        print """  values"""
        print """- conf, storm-release and file-ids are followed by """
        print """  a value """
        print """- ids is followed by a sequence of id values separated by , """
        print """  and between '"""
        print """- filter-list is followed by a sequence of values separated """
        print """  by ; and between ', the values of which are"""
        print """  t|test=sequence of types of tests separated by , as """
        print """      DT that filters in relation with the """
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
        print """      tstorm-tests --filter-list 't=DT;regression=true;f=n,d,rfc,id'"""

    def __parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvlc:i:f:s:r:",
                ["help","noreport","list", "conf=",
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
            elif opt in ("--noreport"):
                self.parameters['report'] = False
            else:
                raise run_tests.OptionError("Unhandled option")

        self.__verify_conf_file()

    def __run_tests(self, tfn, uid, lfn, tt):
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

        if self.parameters['list_tests_details'][0]:
            self.tests_instance.get_sanity_info()
            sys.exit(0)
        if self.parameters['filter_tests_details'][0]:
            self.tests_instance.get_sanity_info(info=self.parameters['filter_tests_details'][1])
            sys.exit(0)

        if self.parameters['tests_sequence_file'][0]:
            if settings.file_exists(sel.parameters['tests_sequence_file'][1]):
                self.parameters['tests_sequence'] = (True,
                   self.parameters['tests_sequence'][1] + settings.get_tests_sequence(self.parameters['tests_sequence_file'][1]))
            else:
                raise RunSanityTestsErrors("File that contains tests sequence does not exist")

        if self.parameters['tests_sequence'][0]:
            if not settings.is_tests_sequence_valid(self.parameters['tests_sequence'][1],
                self.parameters['mti_info'].values()):
                raise RunSanityTestsErrors("Wrong Tests Sequence")

        if self.parameters['tests_sequence'][0]:
            self.parameters['valid_tests'] = self.__modify_valid_tests()

    def do_run_tests(self):

        log_file = report_file.ReportFile(report = self.parameters['report'])

        tests_methods = self.tests_instance.get_sanity_methods(tests = self.parameters['valid_tests'])

        for key, value in tests_methods.items():
            self.__run_tests(self.parameters['tfn'], \
                value, log_file, key)

        log_file.close_file()
