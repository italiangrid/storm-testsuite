import datetime
import os
import sys
import time

class ReportFile:
  def __init__(self, fPath = '/tmp', fName = "tstorm"):
    self.fpath = fPath
    t=datetime.datetime.now()
    ts=str(time.mktime(t.timetuple()))
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
    self.log_file = open(os.path.join(self.fpath, self.fname), 'a+')

  def close_file(self):
    self.log_file.close()

  def flush_file(self):
    self.log_file.flush()

  def put(self, text):
    if  len(text) > 0:
      self.log_file.write(text)

  def put_name(self, text = ""):
    self.put_separator()
    self.put('Name          : %s\n' % text)

  def put_description(self, text = ""):
    self.put('Description   : %s\n' % text)

  def put_output(self):
    self.put('Output        : \n')

  def put_cmd(self, text = ""):
    self.put('%s\n' % text)

  def put_result(self, text = ""):
    self.put('Result        : %s\n' % text)
    self.put_separator()
    self.put('\n')

  def put_ruid(self, text = ""):
    self.put('RfC Unique ID : %s\n' % text)
 
  def put_separator(self):
    self.put('==========================================\n')
