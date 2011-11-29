#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class InfoSystem:
  def __init__(self, bh, ip, sad):
    self.behn = bh
    self.info_port = ip
    self.sa_descr = sad
    self.cmd = {
      'name': 'curl',
      'protocol': 'http',
      'port': self.info_port
    }
    self.otpt = {
      'status':'',
      'busy-space':'',
      'used-space':'',
      'unavailable-space':'',
      'reserved-space':'',
      'total-space':'',
      'free-space':'',
      'available-space':''
    }

  def get_command(self):
    a = self.cmd['name'] + ' -s ' + self.cmd['protocol'] + '://' + self.behn + ':' + self.cmd['port'] + '/info/status/' + self.sa_descr + '_TOKEN'
    return a

  def run_command(self):
    a=()
    if utils.cmd_exist(self.cmd["name"]):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self):
    a=self.run_command()
    if len(a) > 0 and a[0] == 0:
      for x in self.otpt:
        if x == 'status':
          self.otpt[x] = 'PASS'
        else:
          y = a[1].split('\n')
          if x in y[0]:
            self.otpt[x] = y[0].split('"'+x+'":')[1].split(',')[0].split('}}')[0]
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt
