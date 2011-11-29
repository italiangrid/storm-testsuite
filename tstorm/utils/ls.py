#!/usr/bin/python

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
      'Checksum': '',
      'fileLocality': ''}

  def get_command(self):
    a= self.cmd['name'] + ' -l -b -D srmv2 '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
    return a

  def run_command(self):
    a=()
    if utils.cmd_exist(self.cmd['name']):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self):
    a=self.run_command()
    if len(a) > 0 and a[0] == 0:
      self.otpt['status'] = 'PASS'
      x=a[1].split('\n')
      k=self.otpt.keys()
      for y in x:
        if 'ONLINE_AND_NEARLINE' in y:
          self.otpt['fileLocality']='ONLINE_AND_NEARLINE'
        elif 'ONLINE' in y:
          self.otpt['fileLocality']='ONLINE'
        elif 'NEARLINE' in y:
          self.otpt['fileLocality']='NEARLINE'
        elif 'Checksum' in y:
          self.otpt['Checksum'] = y.split(':')[1][1:]
    else:
      self.otpt['status'] = 'FAILURE'
    return self.otpt

class StoRMLs:
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
      'explanation':[],
      'fileLocality':'',
      'checkSumType':'',
      'checkSumValue':''}
    self.map = {
      '0': 'ONLINE',
      '1': 'NEARLINE',
      '2': 'ONLINE_AND_NEARLINE'}

  def get_command(self):
    a = self.cmd['name'] + ' ls -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
    
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
                if x == 'fileLocality':
                  self.otpt[x] = self.map(c[z.split(x)[1].split('=')[1]])
                elif x in ('checkSumType', 'checkSumValue'):
                  self.otpt[x] = z.split(x)[1].split('="')[1].split('"')[0]
                else:
                  self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
      else:
        self.otpt['status'] = 'FAILURE'
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt

class Ls:
  def __init__(self, fn='input-file'):
    self.ifn = fn
    self.cmd = {
      'name':'ls'}
    self.otpt = {
      'status':'',
      'size':''}

  def get_command(self):
    a = self.cmd['name'] + ' -al '+ self.ifn
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
      self.otpt['size'] = a[1].split(' ')[4]
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt
    
