__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class LdapSearch:
  def __init__(self, endpoint, basedn='mds-vo-name=resource,o=grid', filter="'objectClass=GlueService'", attributes):
    self.endpoint = endpoint
    self.basedn = basedn
    self.filter = filter
    self.attributes = attributes
    self.cmd = {
      'name': 'ldapsearch',
      'protocol': 'ldap'
      'port': '2170'}
      'basedn':'-b' + self.basedn,
      'uri':'-H' + self.cmd['protocol'] + '://' + self.endpoint + ':' + self.cmd['port'],
      'pres':'-LLL',
      'sa':'-x'}
    self.otpt = {
      'status':'',
      'GlueServiceName':'',
      'GlueServiceType':''}

  def get_command(self):
    opt = ' ' + self.cmd['sa'] + ' ' + self.cmd['pres'] + ' ' + self.cmd['uri'] + ' ' +  self.cmd['basedn'] + ' '
    a= self.cmd['name'] + opt + self.filter + ' ' self.attributes
      
    print a
    return a

  def run_command(self, in_write=True):
    a=()
    if utils.cmd_exist(self.cmd["name"]):
      a=commands.getstatusoutput(self.get_command())
    return a

  def get_output(self, in_write=True):
    a=self.run_command()
    if len(a) > 0 and a[0] == 0:
      for x in self.otpt:
        if x == 'status':
          self.otpt['status'] = 'PASS'
        else:
          y = a[1].split('\n')
          for z in y:
            if x in z:
              self.otpt[x] = z.split(x)[1].split(': ')[1]
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt
