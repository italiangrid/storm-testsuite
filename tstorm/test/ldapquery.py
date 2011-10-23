__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ldapsearch as ls 

class LdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, basedn='mds-vo-name=resource,o=grid', filter="'objectClass=GlueService'", attributes='GlueServiceType GlueServiceName'):
      super(LdapTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.basedn = basedn
      self.filter = filter
      self.attributes = attributes

    def test_glue_service(self):
      print '''Name          : STORM BUG: GLUESERVICENAME AND GLUESERVIVETYPE CONTAIN WRONG VALUES'''
      print '''Description   : Yaim-Storm for GLUE2 configuration called a worng script setting wrong values in the GlueServiceName
and GlueServiceType attributes of the GLUE1.3 schema.'''
      print '''RfC Unique ID : https://storm.cnaf.infn.it:8443/redmine/issues/143'''
      print '''Output        :\n'''
      self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], self.attributes, self.basedn, self.filter).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.assert_('emi.storm' not in self.ls_result['GlueServiceType'])

    def test_glue_storage_share_capacity(self):
      print '''Name          : GLUE2 GLUE2STORAGESHARECAPACITY* SIZES ALWAYS ZERO'''
      print '''Description   : Glue2 GLUE2StorageShareCapacity* sizes always 0.'''
      print '''RfC Unique ID : https://storm.cnaf.infn.it:8443/redmine/issues/147'''
      print '''Output        :\n'''
      self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GLUE2StorageServiceCapacityFreeSize GLUE2StorageServiceCapacityUsedSize GLUE2StorageServiceCapacityTotalSize GLUE2StorageServiceCapacityReservedSize', 'GLUE2GroupID=resource,o=glue', "'(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=online))'").get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.assert_(int(self.ls_result['GLUE2StorageServiceCapacityTotalSize']) != 0)

      self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GLUE2StorageServiceCapacityFreeSize GLUE2StorageServiceCapacityUsedSize GLUE2StorageServiceCapacityTotalSize GLUE2StorageServiceCapacityReservedSize', 'GLUE2GroupID=resource,o=glue', "'(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=nearline))'").get_output()
      if self.ls_result['status'] == 'PASS':
        self.assert_(self.ls_result['status'] == 'PASS')
        self.assert_(int(self.ls_result['GLUE2StorageServiceCapacityTotalSize']) >= 0)
      else:
        self.assert_(self.ls_result['status'] == 'FAILURE')

    def test_glue_available_space(self):
      print '''Name          : WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB'''
      print '''Description   : Wrong calculation of SA_AVAILABLE_SPACE'''
      print '''RfC Unique ID : https://storm.cnaf.infn.it:8443/redmine/issues/150'''
      print '''Output        :\n'''
      self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GlueSALocalID', self.basedn, "'(objectclass=GlueSA)'").get_output()
      self.assert_(self.ls_result['status'] == 'PASS')

      for x in self.ls_result['GlueSALocalID']:
        self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GlueSAFreeOnlineSize GlueSAStateAvailableSpace', self.basedn, "'(&(objectclass=GlueSA)(GlueSALocalID="+x+"))'").get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        self.assert_(int(self.ls_result['GlueSAStateAvailableSpace'])/(1000*1000) >= int(self.ls_result['GlueSAFreeOnlineSize']))

    def test_glue_used_space(self):
      
      print '''Description   : Wrong calculation of SA_USED_SPACE'''
      print '''RfC Unique ID : https://storm.cnaf.infn.it:8443/redmine/issues/150'''
      print '''Output        :\n'''
      self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GlueSALocalID', self.basedn, "'(objectclass=GlueSA)'").get_output()
      self.assert_(self.ls_result['status'] == 'PASS')

      for x in self.ls_result['GlueSALocalID']:
        self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GlueSAUsedOnlineSize GlueSAStateUsedSpace', self.basedn, "'(&(objectclass=GlueSA)(GlueSALocalID="+x+"))'").get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        self.assert_(int(self.ls_result['GlueSAStateUsedSpace'])/(1000*1000) >= int(self.ls_result['GlueSAUsedOnlineSize']))

    def test_size(self):
      print '''Name          : GET_SIZE INCORRECTLY HANDLES THE INFO'''
      print '''Description   : Wrong calculation of SA_USED_SPACE'''
      print '''RfC Unique ID : https://storm.cnaf.infn.it:8443/redmine/issues/146'''
      print '''Output        :\n'''
      self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GlueSALocalID', self.basedn, "'(objectclass=GlueSA)'").get_output()
      self.assert_(self.ls_result['status'] == 'PASS')

      for x in self.ls_result['GlueSALocalID']:
        self.ls_result = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GlueSATotalOnlineSize GlueSAUsedOnlineSize GlueSAFreeOnlineSize GlueSAReservedOnlineSize GlueSATotalNearlineSize', self.basedn, "'(&(objectclass=GlueSA)(GlueSALocalID="+x+"))'").get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        self.assert_(int(self.ls_result['GlueSATotalOnlineSize']) >= 0)
        self.assert_(int(self.ls_result['GlueSATotalNearlineSize']) >= 0)
        self.assert_(int(self.ls_result['GlueSAFreeOnlineSize']) >= 0)
        self.assert_(int(self.ls_result['GlueSAReservedOnlineSize']) >= 0)
        self.assert_(int(self.ls_result['GlueSAUsedOnlineSize']) >= 0)


      
