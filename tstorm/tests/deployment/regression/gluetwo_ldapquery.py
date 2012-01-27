#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
from tstorm.utils import configuration
from tstorm.utils import ldapsearch as ls 
from tstorm.utils import infosystem as ins
from tstorm.utils import utils

class GluetwoLdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn, filter='', attributes=''):
        super(LdapTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.filter = filter
        self.attributes = attributes
        self.uid = uid
        self.lfn=lfn

    def test_gluetwo_storage_share_capacity(self):
        self.lfn.put_name('GLUE2 GLUE2STORAGESHARECAPACITY* SIZES ALWAYS ZERO')
        self.lfn.put_description('Glue2 GLUE2StorageShareCapacity* sizes always 0.')
        if self.uid.has_key('test_gluetwo_storage_share_capacity'):
            self.lfn.put_uuid(self.uid['test_gluetwo_storage_share_capacity'])
        else:
            print 'ADD UID for test_gluetwo_storage_share_capacity'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/147')
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            "'(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=online))'",
            ['GLUE2StorageServiceCapacityFreeSize',
            'GLUE2StorageServiceCapacityUsedSize',
            'GLUE2StorageServiceCapacityTotalSize',
            'GLUE2StorageServiceCapacityReservedSize'],
            self.tsets['bdii']['glue_two_basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')
        self.assert_(int(ls_result['glue2.0']['GLUE2StorageServiceCapacityTotalSize']) != 0)

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            "'(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=nearline))'"
            ['GLUE2StorageServiceCapacityFreeSize',
            'GLUE2StorageServiceCapacityUsedSize',
            'GLUE2StorageServiceCapacityTotalSize',
            'GLUE2StorageServiceCapacityReservedSize'],
            self.tsets['bdii']['glue_two_basedn'])
        self.lfn.put_cmd(ldap_search.get_command())
        ls_result = ldap_search.get_output()
        if ls_result['status'] == 'PASS':
            self.assert_(int(ls_result['glue2.0']['GLUE2StorageServiceCapacityTotalSize']) >= 0)
        else:
            self.assert_(ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
