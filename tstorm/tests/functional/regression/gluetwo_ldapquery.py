import datetime
import time
import os 
import unittest
import inspect

from tstorm.utils import configuration
from tstorm.utils import ldapsearch 
from tstorm.utils import utils

__author__ = 'Elisabetta Ronchieri'

class GluetwoLdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn, filter='', attributes=''):
        super(GluetwoLdapTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.filter = filter
        self.attributes = attributes
        self.id = uid.get_id()
        self.lfn=lfn

    def test_gluetwo_storage_share_capacity(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
                "(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=online))",
                ['GLUE2StorageServiceCapacityFreeSize',
                'GLUE2StorageServiceCapacityUsedSize',
                'GLUE2StorageServiceCapacityTotalSize',
                'GLUE2StorageServiceCapacityReservedSize'],
                self.tsets['bdii']['glue_two_basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GLUE2StorageServiceCapacityTotalSize value'
            self.assert_(int(ls_result['glue2.0']['GLUE2StorageServiceCapacityTotalSize']) != 0,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
                "(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=nearline))",
                ['GLUE2StorageServiceCapacityFreeSize',
                'GLUE2StorageServiceCapacityUsedSize',
                'GLUE2StorageServiceCapacityTotalSize',
                'GLUE2StorageServiceCapacityReservedSize'],
                self.tsets['bdii']['glue_two_basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()
            if ls_result['status'] == 'PASS':
                msg = 'Wrong GLUE2StorageServiceCapacityTotalSize value'
                self.assert_(int(ls_result['glue2.0']['GLUE2StorageServiceCapacityTotalSize']) >= 0,
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
            else:
                msg = 'ldap status'
                self.assert_(ls_result['status'] == 'FAILURE',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_gluetwo_endpoint_undefined(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
                "(&(objectclass=GLUE2Endpoint)(GLUE2EndpointInterfaceName=emi.storm))", 
                ['GLUE2EndpointSupportedProfile', 'GLUE2EndpointInterfaceExtension',
                'GLUE2EndpointIssuerCA', 'GLUE2EndpointTrustedCA'],
                self.tsets['bdii']['glue_two_basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()
            
            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GLUE2EndpointSupportedProfile value'
            self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2EndpointSupportedProfile'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GLUE2EndpointInterfaceExtension value'
            self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2EndpointInterfaceExtension'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GLUE2EndpointIssuerCA value'
            self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2EndpointIssuerCA'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GLUE2EndpointTrustedCA value'
            self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2EndpointTrustedCA'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_gluetwo_storage_undefined(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
                "(objectclass=GLUE2StorageShare)",
                ['GLUE2StorageShareAccessMode'],
                self.tsets['bdii']['glue_two_basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GLUE2StorageShareAccessMode value'
            self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2StorageShareAccessMode'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_gluetwo_endpoint(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
                "(&(objectclass=GLUE2Endpoint)(GLUE2EndpointInterfaceName=emi.storm))", 
                ['GLUE2EndpointCapability'], self.tsets['bdii']['glue_two_basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GLUE2EndpointCapability value'
            self.assert_('implementation.model' not in ls_result['glue2.0']['GLUE2EndpointCapability'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong GLUE2EndpointCapability value' 
            self.assert_('implementation.discovery' not in ls_result['glue2.0']['GLUE2EndpointCapability'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
 
            msg = 'Wrong GLUE2EndpointCapability value'
            self.assert_('implementation.monitoring' not in ls_result['glue2.0']['GLUE2EndpointCapability'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_gluetwo_service(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
                "(&(objectclass=GLUE2Service))",
                ['GLUE2StorageServie'], self.tsets['bdii']['glue_two_basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
