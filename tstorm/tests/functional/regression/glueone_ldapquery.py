import datetime
import time
import os 
import unittest
import inspect

from tstorm.utils import configuration
from tstorm.utils import ldapsearch 
from tstorm.utils import utils

__author__ = 'Elisabetta Ronchieri'

class LdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn, filter='', attributes=''):
        super(LdapTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.filter = filter
        self.attributes = attributes
        self.id = uid.get_id()
        self.lfn=lfn

    def test_glueone_service(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
                self.filter, self.attributes, self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GlueServiceType value'
            self.assert_('emi.storm' not in ls_result['glue1.3']['GlueServiceType'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
