__author__ = 'Elisabetta Ronchieri'

import commands
import os

class SrmPing:
  def __init__(self, endpoint):
    self.endpoint = endpoint
    self.cmd = {
      'name': 'srmping',
      'protocol': 'srm'}
    self.otpt = {
      'status':'',
      'VersionInfo': '',
      'backend_type': '',
      'backend_version': ''}

  def get_command(self):
    a = self.cmd['name'] + ' -2 -debug '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/'
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
      x=a[1].split('\n')
      k=self.otpt.keys()
      for y in x:
        if 'VersionInfo' in y:
          self.otpt['VersionInfo'] = y.split(':')[1][1:]
        if 'backend_type' in y:
          self.otpt['backend_type'] = y.split(':')[1]
        if 'backend_version' in y:
          self.otpt['backend_version'] = y.split('backend_version:')[1]
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt
    
