__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Dd:
  def __init__(self, fn='input-file'):
    self.ifn = fn
    self.cmd = {
      'name':'dd',
      'size':'1M'}
    self.otpt = {
      'status':''}

  def get_command(self):
    a = self.cmd['name'] + ' if=/dev/urandom of='+ self.ifn + ' bs=' + self.cmd['size'] + ' count=1'
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
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt

class Cf:
  def __init__(self, fn='input-file'):
    self.ifn = fn
    self.otpt = {
      'status':''}

  def get_output(self):
    c = 'a'
    try:
      f = open(self.ifn,'w')
      f.write(c)
      f.close()
      self.otpt['status'] = 'PASS'
    except IOError:
      self.otpt['status'] = 'FAILURE'
      pass

    return self.otpt
