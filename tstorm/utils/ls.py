__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class LcgLs:
  def __init__(self, endpoint, accesspoint, dfn):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.cmd = {
      'name': 'lcg-ls',
      'protocol': 'srm'}
    self.otpt = {
      'status':'',
      'Checksum': ''}

  def get_command(self):
    a= self.cmd['name'] + ' -l -b -D srmv2 '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
    print a
    return a

  def run_command(self):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self):
    a=self.run_command()
    if a[0] == 0:
      self.otpt['status'] = 'PASS'
      x=a[1].split('\n')
      k=self.otpt.keys()
      for y in x:
        if 'Checksum' in y:
          self.otpt['Checksum'] = y.split(':')[1][1:]
    else:
      self.otpt['status'] = 'FAILURE'
    return self.otpt
    
