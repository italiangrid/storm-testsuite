'''
File: removefile.py
Authors: Elisabetta Ronchieri
'''

import commands
import os

class RmLf:
  def __init__(self, fn='input-file', bfn='back-input-file'):
    self.ifn = fn
    self.bfn = bfn
    self.cmd = {
      'name': 'rm'}
    self.otpt = {
      'status':''}

  def get_command(self):
    a = self.cmd['name'] + ' ' + self.ifn + ' ' + self.bfn 
    print a
    return a

  def is_bin(self, cmd):
    return os.path.exists(cmd) and os.access(cmd, os.X_OK)
    
  def cmd_exist(self, cmd):
    fpath, fname = os.path.split(cmd)
    if fpath:
      if self.is_bin(cmd):
        return True
    else:
      for path in os.environ["PATH"].split(os.pathsep):
        tmp_cmd = os.path.join(path,cmd)
        if self.is_bin(tmp_cmd):
          self.cmd['name'] = tmp_cmd
          return True
    return False

  def run_command(self):
    a=()
    if self.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self):
    a=self.run_command()
    if a[0] == 0:
      self.otpt['status'] = 'PASS'
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt
