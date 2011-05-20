'''
File: mkdir.py
Authors: Elisabetta Ronchieri
'''

import commands
import os

class SrmMkdir:
  def __init__(self, endpoint, accesspoint, dfn):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.cmd = {
      'name': 'srmmkdir',
      'protocol': 'srm'}
    self.otpt = {
      'status':[],
      'path':[]}

  def get_command(self, pt):
    a=self.cmd['name'] + ' -2 -debug '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + pt
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

  def run_command(self, dtc):
    a=()
    if self.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command(dtc))
    return a

  def get_output(self):
    dtc=self.dfn.split('/')
    dtc=dtc[1:]
    y='/'
    for x in dtc:
      if x != '':
        a=self.run_command(y + x)
        y = y + x + '/'
        self.otpt['path'].append(y)
        if a[0] == 0:
          self.otpt['status'].append('PASS')
        else:
          self.otpt['status'].append('FAILURE')

    return self.otpt
    
