#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

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
    
    return a

  def run_command(self, dtc):
    a=()
    if utils.cmd_exist(self.cmd['name']):
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
        if len(a) > 0 and a[0] == 0:
          self.otpt['status'].append('PASS')
        else:
          self.otpt['status'].append('FAILURE')

    return self.otpt
    
