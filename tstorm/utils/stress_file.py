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

    def put_header(self, stamp, cycle='', elapsed_time=''):
        if self.report:
            self.put_separator(stamp=stamp, cycle=cycle, elapsed_time=elapsed_time)

    def put_epilogue(self, cycle='', elapsed_time=''):
        if self.report:
            self.put_separator(cycle=cycle, elapsed_time=elapsed_time)

    def put_prologue(self):
        if self.report:
            self.put_separator()
 
    def put_separator(self, stamp='',cycle='', elapsed_time=''):
        if self.report:
            msg = '=========================================='
            if stamp != '':
                msg += ' ' + stamp
            if cycle != '':
                msg += ' ' + cycle
            if elapsed_time != '':
                msg += ' ' + elapsed_time
            self.put(msg + '\n')
