__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Cat:
  def __init__(self, fn='input-file'):
    self.ifn = fn
    self.cmd = {
      'name':'cat'}
    self.otpt = {
      'status':'',
      'otpt':''}

  def get_command(self):
    a = self.cmd['name'] + ' ' + self.ifn
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
      self.otpt['otpt'] = a[1]
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt