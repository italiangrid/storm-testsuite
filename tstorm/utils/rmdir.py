__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class SrmRmdir:
  def __init__(self, endpoint, accesspoint, dfn):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.cmd = {
      'name': 'srmrmdir',
      'protocol': 'srm'}
    self.otpt = {
      'status':[],
      'path':[]}

  def get_command(self, pt):
    a=self.cmd['name'] + ' -2 -debug '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + pt
    print a
    return a

  def run_command(self, dtc):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command(dtc))
    return a

  def get_output(self):  
    y=self.dfn
    while y != '/':
      a=self.run_command(y)
      self.otpt['path'].append(y)
      if len(a) > 0 and a[0] == 0:
        self.otpt['status'].append('PASS')
      else:
        self.otpt['status'].append('FAILURE')
      y=os.path.dirname(y)

    return self.otpt

class StoRMRmdir:
  def __init__(self, endpoint, accesspoint, dfn):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.cmd = {
      'name': 'clientSRM',
      'rqst_protocol': 'httpg',
      'protocol': 'srm'}
    self.otpt = {
      'status':[],
      'statusCode':[],
      'explanation':[]}

  def get_command(self, pt):
    a = self.cmd['name'] + ' rmdir -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + pt
    print a
    return a

  def run_command(self, dtc):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command(dtc))
    return a

  def get_output(self):
    y=self.dfn
    while y != '/':
      a=self.run_command(y)
      if len(a) > 0 and a[0] == 0:
        if 'SRM_SUCCESS' in a[1]:
          for x in self.otpt:
            if x == 'status':
              self.otpt['status'].append('PASS')
            else:
              yy = a[1].split('\n')
              for z in yy:
                if x in z:
                  self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
        else:
          self.otpt['status'].append('FAILURE')
      else:
        self.otpt['status'].append('FAILURE')
      y=os.path.dirname(y)

    return self.otpt
