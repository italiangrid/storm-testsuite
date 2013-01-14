import datetime
import os
import sys
import time
import utils

class StressReportFile:
    def __init__(self, fPath = '/var/log/tstorm/stress', fName = "tstorm-stress", report = True):
        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        id = utils.get_uuid()
        #self.fpath = fPath + '/' + ts
        self.fpath = fPath + '/' + id
        if not os.path.isdir(self.fpath):
            os.makedirs(self.fpath)
        self.fname = fName + '_' + ts + '.log'
        self.log_file = ""
        self.report = report
        if not os.path.isdir(self.fpath):
            self.fpath = os.getcwd()
        if not os.path.isdir(self.fpath):
            sys.stderr.write ("in LogFile initialization\n")
            sys.stderr.write ("file path set to: <<" + self.fpath + ">>\n")
            sys.stderr.write ("This appears to not be a valid directory.")
            sys.stderr.write ("This is a serious internal error")
            fail ("Log file path must be valid")
        if self.report:
            self.log_file = open(os.path.join(self.fpath, self.fname), 'a+')

    def get_filename(self):
        return self.fname

    def get_path(self):
        return self.fpath

    def close_file(self):
        if self.report:
            self.log_file.close()

    def flush_file(self):
        if self.report:
            self.log_file.flush()

    def put(self, text):
        if  len(text) > 0:
            self.log_file.write(text)

    def put_comment(self):
        if self.report:
            msg = ('###############################################################################################################\n'+
                '# This report starts with an header that explains the requested execution.\n'+
                '# In case a number of tests has been requested it will look like:\n'+
                '# ========================================== Requested tests: <number_of_requested_tests>; START_TIME: <current_time>\n' +
                '# In case a number of hours has been requested it will look like:\n'+
                '# ========================================== Requested hours of testing: <number_of_requested_testing_hours>; START_TIME: <current_time>\n' +
                '# Then for each reporting cycle an header that contains testing progress is shown.\n'+
                '# In case a number of tests has been requested it will look like:\n'+
                '# ========================================== NT: <number_of_performed_tests>; CURRENT_TIME: <current_time>\n'+
                '# In case a number of hours has been requested it will look like:\n'+
                '# ========================================== NH: <number_of_elapsed_hours>; CURRENT_TIME: <current_time>\n'+
                '# For each performed test this header is followed by a summary row that contains test name,\n'+
                '# how many times the test has been performed in the current reporting cycle and from the beginning of\n'+
                '# the stress testing:\n'+
                '# TEST_NAME  NUMBER_OF_TEST_EXECUTION_FOR_THE_REPORTING_CYCLE  TOTAL_NUMBER_OF_TEST_EXECUTION\n'+
                '# ...\n'+
                '# The report is closed by a summary footer.\n'+
                '# In case a number of tests has been requested it will look like:\n'+
                '# ========================================== Performed tests: <number_of_performed_tests>; ELAPSED_TIME: <elapsed_time>\n' +
                '# In case a number of hours has been requested it will look like:\n'+
                '# ========================================== Performed hours of testing: <number_of_performed_testing_hours>; TESTS_PERFORMED: <num_test_performed>\n' +
                '###############################################################################################################\n')

            self.put(msg) 

    def __raw__(self):
        return '=========================================='

    def put_header(self, hours='', cycle='', current_time=''):
        if self.report:
            msg = self.__raw__()
            if cycle != '':
                msg += ('  Requested tests: %s; START_TIME: %s'
                    % (cycle, current_time))
            elif hours != '':
                msg += (' Requested hours of testing:  %s; START_TIME: %s'
                    % (hours, current_time))
            self.put(msg + '\n')

    def put_footer(self, hours='', cycle='', elapsed_time=''):
        if self.report:
            msg = self.__raw__()
            if hours != '':
                msg += ('  Performed hours of testing: %s; TESTS_PERFORMED: %s'
                    % (hours, cycle))
            elif cycle != '':
                min = int(elapsed_time)/60
                sec = int(elapsed_time)%60
                msg += ('  Performed tests: %s; ELAPSED_TIME: %s min, %s sec' 
                    % (cycle, min, sec))
            self.put(msg + '\n')

    def put_epilogue(self, hours='', cycle='', current_time=''):
        if self.report:
            self.put_separator(hours=hours, cycle=cycle, current_time=current_time)
 
    def put_separator(self, hours='', cycle='', current_time=''):
        if self.report:
            msg = self.__raw__()
            if cycle != '':
                msg += ('  NT: %s; CURRENT_TIME: %s'
                    % (cycle, current_time))
            elif hours != '':
                msg += ('  NH: %s; CURRENT_TIME: %s'
                    % (hours, current_time))
            self.put(msg + '\n')
