import datetime
import os
import sys
import time

class StressReportFile:
    def __init__(self, fPath = '/tmp', fName = "tstorm-stress", report = True):
        self.fpath = fPath
        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
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

    def close_file(self):
        if self.report:
            self.log_file.close()

    def flush_file(self):
        if self.report:
            self.log_file.flush()

    def put(self, text):
        if  len(text) > 0:
            self.log_file.write(text)

    def put_epilogue(self):
        if self.report:
            self.put('\n')
            self.put_separator()

    def put_prologue(self):
        if self.report:
            self.put_separator()
            self.put('\n')
 
    def put_separator(self):
        if self.report:
            self.put('==========================================\n')
