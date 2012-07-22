import datetime
import time
import os 
import unittest
from tstorm.utils import configuration
from tstorm.utils import ldapsearch 
from tstorm.utils import utils

__author__ = 'Elisabetta Ronchieri'

class LdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, lfn, filter='', attributes=''):
        super(LdapTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.filter = filter
        self.attributes = attributes
        self.lfn=lfn

    def test_glueone_service(self):
        ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
            self.filter, self.attributes, self.tsets['bdii']['basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')
        self.assert_('emi.storm' not in ls_result['glue1.3']['GlueServiceType'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
