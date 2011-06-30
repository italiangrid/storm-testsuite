__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class LcgBringonline:
  def __init__(self, endpoint, accesspoint, dfn):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.cmd = {
      'name': 'lcg-bringonline',
      'protocol': 'srm'}
    self.otpt = {
      'status':'',
      'requestToken':''}

  def get_command(self):
    a= self.cmd['name'] + ' -b --verbose -T srmv2 '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
    print a
    return a

  def run_command(self):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self):
    a=self.run_command()
    if len(a) > 0 and a[0] == 0:
      for x in self.otpt:
        if x == 'status':
          self.otpt['status'] = 'PASS'
        else:
          y = a[1].split('\n')
          for z in y:
            if 'Token' in z:
              self.otpt['requestToken']=z.split('Token:')[1].split(' ')[1]          
    else:
      self.otpt['status'] = 'FAILURE'
    return self.otpt

class SrmBringonline:
  def __init__(self, endpoint, accesspoint, dfn):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.cmd = {
      'name': 'srm-bring-online',
      'protocol': 'srm'}
    self.otpt = {
      'status':'',
      'requestToken':''}

  def get_command(self):
    a= self.cmd['name'] + ' -2 -debug '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
    print a
    return a

  def run_command(self):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self):
    a=self.run_command()
    if len(a) > 0 and a[0] == 0:
      for x in self.otpt:
        if x == 'status':
          self.otpt['status'] = 'PASS'
        else:
          y = a[1].split('\n')
          for z in y:
            if x in z:
              self.otpt[x]=z.split(x)[1].split('= ')[1]
    else:
      self.otpt['status'] = 'FAILURE'
    return self.otpt

class StoRMBol:
  def __init__(self, endpoint, accesspoint, dfn):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.cmd = {
      'name': 'clientSRM',
      'rqst_protocol': 'httpg',
      'protocol': 'srm'}
    self.otpt = {
      'status':'',
      'statusCode':[],
      'explanation':[]}

  def get_command(self):
    a = self.cmd['name'] + ' bol -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn + ' -p'
    print a
    return a

  def run_command(self):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self):
    a=self.run_command()
    if len(a) > 0 and a[0] == 0:
      if 'SRM_SUCCESS' in a[1]:
        if 'SRM_NOT_SUPPORTED' in a[1]:
          self.otpt['status'] = 'FAILURE'
        else:
          for x in self.otpt:
            if x == 'status':
              self.otpt['status'] = 'PASS'
            else:
              y = a[1].split('\n')
              for z in y:
                if x in z:
                  self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
      else:
        self.otpt['status'] = 'FAILURE'
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt

class StoRMSbol:
  def __init__(self, endpoint, accesspoint, dfn, turl):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.turl = turl
    self.cmd = {
      'name': 'clientSRM',
      'rqst_protocol': 'httpg',
      'protocol': 'srm'}
    self.otpt = {
      'status':'',
      'statusCode':[],
      'explanation':[]}

  def get_command(self):
    a = self.cmd['name'] + ' sbol -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn + ' -t ' + self.turl
    print a
    return a

  def run_command(self):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self):
    a=self.run_command()
    if len(a) > 0 and a[0] == 0:
      if 'SRM_SUCCESS' in a[1]:
        if 'SRM_NOT_SUPPORTED' in a[1]:
          self.otpt['status'] = 'FAILURE'
        else:
          for x in self.otpt:
            if x == 'status':
              self.otpt['status'] = 'PASS'
            else:
              y = a[1].split('\n')
              for z in y:
                if x in z:
                  self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
      else:
        self.otpt['status'] = 'FAILURE'
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt
