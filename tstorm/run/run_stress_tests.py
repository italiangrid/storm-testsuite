#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import sys
import unittest
import getopt
import exceptions
import random
import time
import datetime

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
from tstorm.tests.load import loadstests as lt

class RunStressTestsError(exceptions.Exception):
    pass

class RunStressTests(run_tests.RunTests):
    def __init__(self):
        super(RunStressTests, self).__init__()
        self.parameters['report'] = False
        self.parameters['stress_report'] = True
        self.parameters['number_cycles'] = 30
        self.parameters['number_hours'] = 0
        self.parameters['refresh_report'] = 10
        self.parameters['tests_status'] = {}
        self.parameters['tests_methods'] = {}

    def do_parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                "hvc:n:r:",
                ["help","nostressreport","report",
                 "version","conf=","number-cycles=",
                 "number-hours=","refresh-report=",
                 "storm-release="])
        except getopt.GetoptError, err:
            print str(err)
            usage.get_usage(run='stress')
            sys.exit(2)

        n_cycles = False
        n_hours = False
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
                n_cycles = True
            elif opt in ("-c", "--conf"):
                self.parameters['custom_conf_file'] = (True, value)
            elif opt in ("--number-hours"):
                self.parameters['number_hours'] = int(value)
                n_hours = True
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
            elif opt in ("--report"):
                self.parameters['report'] = True
            else:
                raise run_tests.OptionError("Unhandled option")

        if n_cycles and n_hours:
            msg = 'The options number-hours and number-cycles are'
            msg += ' mutually exclusive'
            raise run_tests.OptionError(msg)

    def run_test(self, tfn, uid, lfn, sfn, n_df, n_dfn):
        sd=True
        if 'ts_https' in uid.get_aggregator() or \
           'ts_http' in uid.get_aggregator() or \
           'ts_https_voms' in uid.get_aggregator() or \
           '_https_' in uid.get_aggregator() or \
           '_http_' in uid.get_aggregator() or \
           '_https' in uid.get_aggregator() or \
           '_http' in uid.get_aggregator():
            sd=False
        ifn,dfn,back_ifn= settings.set_inpt_fn(n_df,n_dfn,path=sfn.get_path(),subdir=sd)
        lfn.put_name(uid.get_name())
        lfn.put_description(uid.get_description())
        lfn.put_uuid(uid.get_id())
        if uid.is_regression():
            lfn.put_ruid(uid.get_rfc())
        lfn.put_output()
        runner = unittest.TextTestRunner(verbosity=2).run(eval(uid.get_aggregator()))
        lfn.put_prologue()

    def __is_time_elapsed(self, ct):
        nt=time.mktime(datetime.datetime.now().timetuple())
        pt=nt-ct
        if pt >= self.parameters['refresh_report']:
            return True
        return False

    def __get_end_time(self):
        later = time.time() + self.parameters['number_hours']*3600
        return time.strptime(time.ctime(later))

    def __get_randomly_test_index(self):
        en = [n for n,z in enumerate(self.parameters['tests_status'].items())]
        ti = random.choice(en)
        flag = self.parameters['tests_status'].items()[ti][1][0]
        while flag:
            tmp = [x[0] for x in self.parameters['tests_status'].values()]
            if False in tmp:
                en = [n for n,z in enumerate(\
                    self.parameters['tests_status'].items())]
                ti = random.choice(en)
            else:
                break
            flag = self.parameters['tests_status'].items()[ti][1][0]
        return ti

    def __set_tests_methods(self):
        self.parameters['tests_methods'] = self.tests_instance.get_methods(\
            tests = self.parameters['valid_tests'], run='stress')

    def __set_tests_status(self):
        self.parameters['tests_status'] = \
            self.parameters['tests_status'].fromkeys(\
                self.parameters['tests_methods'], (False, 0, 0))
        for key, value in self.parameters['tests_status'].items():
            if '_wo' in key or \
                '_glueone' in key or \
                '_gluetwo' in key or \
                'ts_https' in key or \
                'ts_http' in key or \
                'ts_https_voms' in key or \
                '_https_' in key or \
                '_http_' in key or \
                '_https' in key or \
                '_http' in key:
                self.parameters['tests_status'][key] = (True, 0, 0)
 
    def __refresh_stress_tests_info(self, count, new_time, stress_log_file):
        stress_log_file.put_epilogue(cycle=str(count), \
            elapsed_time=new_time.ctime())

        for key, value in self.parameters['tests_status'].items():
            if self.parameters['tests_methods'][key].get_aggregator() != "":
                if '_wo' not in key and \
                    '_glueone' not in key and \
                    '_gluetwo' not in key and \
                    'ts_https' not in key and \
                    'ts_http' not in key and \
                    'ts_https_voms' not in key and \
                    '_https_' not in key and \
                    '_http_' not in key and \
                    '_https' not in key and \
                    '_http' not in key:
                    msg = '%s    %s    %s\n' % (key, value[1], \
                        value[1]+value[2])
                    stress_log_file.put(msg)
                    self.parameters['tests_status'][key]=(value[0],\
                        0,value[2]+value[1])

        stress_log_file.flush_file()

    def for_cycles(self, count, passed_time, log_file, stress_log_file):
        while count < self.parameters['number_cycles']:
            test_index = self.__get_randomly_test_index()
            key = self.parameters['tests_status'].items()[test_index][0]

            if self.parameters['tests_methods'][key].get_aggregator() != "":
                tm_val = self.parameters['tests_methods'][key]

                if '_wo' not in tm_val.get_aggregator() and \
                    '_glueone' not in tm_val.get_aggregator() and \
                    '_gluetwo' not in tm_val.get_aggregator() and \
                    'ts_https' not in tm_val.get_aggregator() and \
                    'ts_http' not in tm_val.get_aggregator() and \
                    'ts_https_voms' not in tm_val.get_aggregator() and \
                    '_https_' not in tm_val.get_aggregator() and \
                    '_http_' not in tm_val.get_aggregator() and \
                    '_https' not in tm_val.get_aggregator() and \
                    '_http' not in tm_val.get_aggregator():
                    self.run_test(self.parameters['custom_conf_file'][1],
                        tm_val, log_file, stress_log_file,\
                        self.parameters['custom_destination_file'][0], \
                        self.parameters['custom_destination_file'][1])

                    ts_val = \
                        self.parameters['tests_status'].items()[test_index][1]
                    test_number = ts_val[1]+1
                    test_total_number = ts_val[2]
                    self.parameters['tests_status'][key]=(True, test_number, \
                        test_total_number)
                    count += 1

                    if self.__is_time_elapsed(passed_time):
                        new_time=datetime.datetime.now()
                        self.__refresh_stress_tests_info(count, new_time, \
                            stress_log_file)
                        passed_time = time.mktime(new_time.timetuple())

        return count

    def for_hours(self, count, passed_time, log_file, stress_log_file):
        end_time = self.__get_end_time()
        c_time = 0
        while c_time < end_time:
            test_index = self.__get_randomly_test_index()
            key = self.parameters['tests_status'].items()[test_index][0]

            if self.parameters['tests_methods'][key].get_aggregator() != "":
                tm_val = self.parameters['tests_methods'][key]

                if '_wo' not in tm_val.get_aggregator() and \
                    '_glueone' not in tm_val.get_aggregator() and \
                    '_gluetwo' not in tm_val.get_aggregator() and \
                    'ts_https' not in tm_val.get_aggregator() and \
                    'ts_http' not in tm_val.get_aggregator() and \
                    'ts_https_voms' not in tm_val.get_aggregator() and \
                    '_https_' not in tm_val.get_aggregator() and \
                    '_http_' not in tm_val.get_aggregator() and \
                    '_https' not in tm_val.get_aggregator() and \
                    '_http' not in tm_val.get_aggregator():
                    self.run_test(self.parameters['custom_conf_file'][1],
                        tm_val, log_file, stress_log_file,\
                        self.parameters['custom_destination_file'][0], \
                        self.parameters['custom_destination_file'][1])

                    ts_val = \
                        self.parameters['tests_status'].items()[test_index][1]
                    test_number = ts_val[1]+1
                    test_total_number = ts_val[2]
                    self.parameters['tests_status'][key]=(True, test_number, \
                        test_total_number)
                    count += 1
                    c_time = time.strptime(time.ctime())
                    if self.__is_time_elapsed(passed_time):
                        new_time=datetime.datetime.now()
                        self.__refresh_stress_tests_info(count, new_time, \
                            stress_log_file)
                        passed_time = time.mktime(new_time.timetuple())

        return count

    def do_list(self):
        if self.parameters['list_tests_details'][0]:
            self.tests_instance.get_info(run='stress')
            sys.exit(0)
        if self.parameters['filter_tests_details'][0]:
            self.tests_instance.get_info(info=self.parameters['filter_tests_details'][1],run='stress')
            sys.exit(0)

    def do_run_tests(self):
        # Prepare log file
        log_file = report_file.ReportFile(report = self.parameters['report'])
        stress_log_file = stress_file.StressReportFile(\
            report = self.parameters['stress_report'])

        # Prepare tests dictionaries
        self.__set_tests_methods()
        self.__set_tests_status()

        # Set counters
        start_time = datetime.datetime.now()
        count = 0
        stress_log_file.put_header('START', cycle=str(count), \
            elapsed_time=start_time.ctime())
        passed_time = time.mktime(start_time.timetuple())

        if self.parameters['number_hours'] != 0:
            count=self.for_hours(\
                count, passed_time, log_file, stress_log_file)
        else:
            count=self.for_cycles(\
                count, passed_time, log_file, stress_log_file)

        new_time=datetime.datetime.now()
        self.__refresh_stress_tests_info(count, new_time, stress_log_file)

        stress_log_file.put_header('END', cycle=str(count), \
            elapsed_time=new_time.ctime())

        if self.parameters['report']:
            log_file.close_file()
        if self.parameters['stress_report']:
            stress_log_file.close_file()
