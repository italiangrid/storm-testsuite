#!/usr/bin/python

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
      
    return a

  def run_command(self, in_write=True):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command(in_write))
    return a

  def get_output(self, in_write=True):
    a=self.run_command(in_write)
    if len(a) > 0 and a[0] == 0:
      self.otpt['status'] = 'PASS'
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt

class StoRMPtp:
  def __init__(self, endpoint, accesspoint, dfn, prt='gsiftp'):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.prt = prt
    self.cmd = {
      'name': 'clientSRM',
      'rqst_protocol': 'httpg',
      'protocol': 'srm'}
    self.otpt = {
      'status':'',
      'statusCode':[],
      'explanation':[],
      'TURL': '',
      'requestToken':''}

  def get_command(self):
    a = self.cmd['name'] + ' ptp -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn + ' -T -P ' + self.prt + ' -p'
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
        for x in self.otpt:
          if x == 'status':
            self.otpt['status'] = 'PASS'
          elif x in ('TURL', 'requestToken'):
            self.otpt[x] = a[1].split(x)[1].split('="')[1].split('"')[0]
          else:
            y = a[1].split('\n')
            for z in y:
              if x in z:
                self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
      elif 'SRM_FAILURE' in a[1]:
        for x in self.otpt:
          if x == 'status':
            self.otpt['status'] = 'FAILURE'
          elif x == 'requestToken':
            self.otpt[x] = a[1].split(x)[1].split('="')[1].split('"')[0]
          elif x in ('statusCode', 'explanation'):
            y = a[1].split('\n')
            for z in y:
              if x in z:
                self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
      else:
        self.otpt['status'] = 'FAILURE'
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt

class StoRMPtg:
  def __init__(self, endpoint, accesspoint, dfn, prt='gsiftp'):
    self.endpoint = endpoint
    self.accesspoint = accesspoint
    self.dfn = dfn
    self.prt = prt
    self.cmd = {
      'name': 'clientSRM',
      'rqst_protocol': 'httpg',
      'protocol': 'srm'}
    self.otpt = {
      'status':'',
      'statusCode':[],
      'explanation':[],
      'transferURL': '',
      'requestToken':''}

  def get_command(self):
    a = self.cmd['name'] + ' ptg -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn + ' -T -P ' + self.prt + ' -p'
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
        for x in self.otpt:
          if x == 'status':
            self.otpt['status'] = 'PASS'
          elif x in ('transferURL', 'requestToken'):
            self.otpt[x] = a[1].split(x)[1].split('="')[1].split('"')[0]
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

class StoRMPd:
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
    a = self.cmd['name'] + ' pd -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn + ' -t ' + self.turl
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

class StoRMRf:
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
    a = self.cmd['name'] + ' rf -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn + ' -t ' + self.turl 
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

class guc:
  def __init__(self, ifn, bifn, turl):
    self.ifn = ifn
    self.bifn = bifn
    self.turl = turl
    self.cmd = {
      'name': 'globus-url-copy'}
    self.otpt = {
      'status':'',
      'debug':''}

  def get_command(self, in_write=True):
    if in_write:
      a= self.cmd['name'] + ' -dbg file://'+ self.ifn + ' ' + self.turl
    else:
      a= self.cmd['name'] + ' -dbg ' + self.turl + ' file://'+ self.bifn

    return a

  def run_command(self, in_write=True):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command(in_write))
    return a

  def get_output(self, in_write=True):
    a=self.run_command(in_write)
    if len(a) > 0 and a[0] == 0:
      self.otpt['status'] = 'PASS'
      self.otpt['debug'] = a[1].split('status')[1][1:]
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt

class curl:
  def __init__(self, ifn, bifn, turl):
    self.ifn = ifn
    self.bifn = bifn
    self.turl = turl
    self.cmd = {
      'name': 'curl'}
    self.otpt = {
      'status':''}
    self.p_path = ''

  def get_command(self, use_ssl=True, in_write=True):
    curl_opt=''
    if use_ssl:
      curl_opt=' --cert ' + self.p_path + ' --capath /etc/grid-security/certificates '
      
    if in_write:
      a= self.cmd['name'] + ' -v ' + curl_opt + ' -T ' + self.ifn + ' ' + self.turl
    else:
      a= self.cmd['name'] + ' -v ' + curl_opt + self.turl + ' -o ' + self.bifn
    
    return a

  def run_command(self, use_ssl, in_write=True):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command(use_ssl, in_write))
    return a

  def get_output(self, use_ssl=True, in_write=True):
    state, self.p_path = utils.get_proxy_path()
    if state == 'FAILURE':
      self.otpt['status'] = state
      return self.otpt

    a=self.run_command(use_ssl, in_write)
    if len(a) > 0 and a[0] == 0:
      if 'html' in a[1]:
        self.otpt['status'] = 'FAILURE'
      else:
        self.otpt['status'] = 'PASS'
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt

