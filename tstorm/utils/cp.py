__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class LcgCp:
  def __init__(self, endpoint, accesspoint, ifn, dfn, bifn):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.ifn = ifn
    self.bifn = bifn
    self.cmd = {
      'name': 'lcg-cp',
      'protocol': 'srm'}
    self.otpt = {
      'status':''}

  def get_command(self, in_write=True):
    if in_write:
      a= self.cmd['name'] + ' -b --verbose -D srmv2 file://'+ self.ifn + ' ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
    else:
      a= self.cmd['name'] + ' -b --verbose -D srmv2 ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn + ' file://'+ self.bifn
      
    print a
    return a

#  def is_bin(self, cmd):
#    return os.path.exists(cmd) and os.access(cmd, os.X_OK)
    
#  def cmd_exist(self, cmd):
#    fpath, fname = os.path.split(cmd)
#    if fpath:
#      if self.is_bin(cmd):
#        return True
#    else:
#      for path in os.environ["PATH"].split(os.pathsep):
#        tmp_cmd = os.path.join(path,cmd)
#        if self.is_bin(tmp_cmd):
#          self.cmd['name'] = tmp_cmd
#          return True
#    return False

  def run_command(self, in_write=True):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command(in_write))
    return a

  def get_output(self, in_write=True):
    a=self.run_command(in_write)
    if a[0] == 0:
      self.otpt['status'] = 'PASS'
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt

  
    
