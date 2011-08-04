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
      self.ls_result = ls.LdapSearch(self.tsets['general']['endpoint'], self.basedn, self.filter, self.attributes).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.assert_('emi.storm' not in self.ls_result['GlueServiceType'])
