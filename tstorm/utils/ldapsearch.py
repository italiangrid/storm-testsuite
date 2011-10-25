__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class LdapSearch:
  def __init__(self, lfn, endpoint, attributes, basedn='mds-vo-name=resource,o=grid', filter="'objectClass=GlueService'"):
    self.endpoint = endpoint
    self.basedn = basedn
    self.filter = filter
    self.attributes = attributes
    self.lfn = lfn
    self.cmd = {
      'name': 'ldapsearch',
      'protocol': 'ldap',
      'port': '2170',
      'basedn':'-b' + ' ' + self.basedn,
      'uri':'-H',
      'pres':'-LLL',
      'sa':'-x'}
    self.otpt = {
      'status':'',
      'GlueServiceName':'',
      'GlueServiceType':'',
      'GLUE2StorageServiceCapacityFreeSize':'',
      'GLUE2StorageServiceCapacityUsedSize':'',
      'GLUE2StorageServiceCapacityTotalSize':'',
      'GLUE2StorageServiceCapacityReservedSize':'',
      'GlueSAStateUsedSpace':'',
      'GlueSAUsedOnlineSize':'',
      'GlueSAFreeOnlineSize':'',
      'GlueSAStateAvailableSpace':'',
      'GlueSATotalOnlineSize':'',
      'GlueSAReservedOnlineSize':'',
      'GlueSATotalNearlineSize':'',
      'GlueSALocalID':[]}

  def get_command(self):
    uri = self.cmd['uri'] + ' ' + self.cmd['protocol'] + '://' + self.endpoint + ':' + self.cmd['port']
    opt = ' ' + self.cmd['sa'] + ' ' + self.cmd['pres'] + ' ' + uri + ' ' +  self.cmd['basedn'] + ' '
    a=self.cmd['name'] + opt + self.filter + ' ' + self.attributes
      
    self.lfn.put_cmd(a)
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
          self.otpt['status'] = 'PASS'
        else:
          y = a[1].split('\n')
          for z in y:
            if x in z:
              if 'GlueSALocalID:' in z:
                self.otpt[x].append(z.split(x+': ')[1].strip())
              elif 'GlueSALocalID=' in z:
                 t=1
              else:
                self.otpt[x]=z.split(x)[1].split(': ')[1]
    else:
      self.otpt['status'] = 'FAILURE'

    return self.otpt
