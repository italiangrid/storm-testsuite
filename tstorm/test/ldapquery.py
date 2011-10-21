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
      print '''\nDescription: Yaim-Storm for GLUE2 configuration called a worng script setting wrong values in the GlueServiceName
and GlueServiceType attributes of the GLUE1.3 schema.\n'''
      print '''\nRfC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/143\n'''
      self.ls_result = ls.LdapSearch(self.tsets['general']['endpoint'], self.attributes, self.basedn, self.filter).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.assert_('emi.storm' not in self.ls_result['GlueServiceType'])
