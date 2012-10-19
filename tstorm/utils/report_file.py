import datetime
import os
import sys
import time
import utils

class ReportFile:
    def __init__(self, fPath = '/var/log/tstorm', fName = "tstorm", report = True):
        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        id = utils.get_uuid()
        #self.fpath = fPath + '/' + ts
        self.fpath = fPath + '/' + id
        self.report = report

        if self.report:
            if not os.path.isdir(self.fpath):
                os.makedirs(self.fpath)
        self.fname = fName + '_' + ts + '.log'
        self.log_file = ""
         
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

    def put_epilogue(self):
        if self.report:
            self.put('\n')
            self.put_separator()

    def put_name(self, text = ""):
        if self.report:
            self.put_epilogue()
            self.put('Name          : %s\n' % text)

    def put_description(self, text = ""):
        if self.report:
            self.put('Description   : %s\n' % text)

    def put_output(self):
        if self.report:
            self.put('Output        : \n')

    def put_cmd(self, text = ""):
        if self.report:
            self.put('%s\n' % text)

    def put_result(self, text = ""):
        if self.report:
            self.put('Result        : %s\n' % text)

    def put_ruid(self, text = ""):
        if self.report:
            self.put('RfC Unique ID : %s\n' % text)

    def put_uuid(self, text = ""):
        if self.report:
            self.put('Unique ID     : %s\n' % text)

    def put_prologue(self):
        if self.report:
            self.put_separator()
            self.put('\n')
 
    def put_separator(self):
        if self.report:
            self.put('==========================================\n')
