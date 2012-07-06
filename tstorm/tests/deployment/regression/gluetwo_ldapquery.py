import datetime
import time
import os 
import unittest
from tstorm.utils import configuration
from tstorm.utils import ldapsearch as ls 
from tstorm.utils import infosystem as ins
from tstorm.utils import utils

__author__ = 'Elisabetta Ronchieri'

class GluetwoLdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn, filter='', attributes=''):
        super(GluetwoLdapTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.filter = filter
        self.attributes = attributes
        self.uid = uid
        self.lfn=lfn

    def test_gluetwo_storage_share_capacity(self):
        self.lfn.put_name(self.uid['test_gluetwo_storage_share_capacity'][5])
        self.lfn.put_description(self.uid['test_gluetwo_storage_share_capacity'][6])
        if self.uid.has_key('test_gluetwo_storage_share_capacity'):
            self.lfn.put_uuid(self.uid['test_gluetwo_storage_share_capacity'][0])
        else:
            print 'ADD UID for test_gluetwo_storage_share_capacity'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid(self.uid['test_gluetwo_storage_share_capacity'][2])
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            "(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=online))",
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
            "(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=nearline))",
            ['GLUE2StorageServiceCapacityFreeSize',
            'GLUE2StorageServiceCapacityUsedSize',
            'GLUE2StorageServiceCapacityTotalSize',
            'GLUE2StorageServiceCapacityReservedSize'],
            self.tsets['bdii']['glue_two_basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        if ls_result['status'] == 'PASS':
            self.assert_(int(ls_result['glue2.0']['GLUE2StorageServiceCapacityTotalSize']) >= 0)
        else:
            self.assert_(ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_gluetwo_endpoint_undefined(self):
        self.lfn.put_name(self.uid['test_gluetwo_endpoint_undefined'][5])
        self.lfn.put_description(self.uid['test_gluetwo_endpoint_undefined'][6])
        if self.uid.has_key('test_gluetwo_endpoint_undefined'):
            self.lfn.put_uuid(self.uid['test_gluetwo_endpoint_undefined'][0])
        else:
            print 'ADD UID for test_gluetwo_endpoint_undefined'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid(self.uid['test_gluetwo_endpoint_undefined'][2])
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            "(&(objectclass=GLUE2Endpoint)(GLUE2EndpointInterfaceName=emi.storm))", 
            ['GLUE2EndpointSupportedProfile', 'GLUE2EndpointInterfaceExtension',
            'GLUE2EndpointIssuerCA', 'GLUE2EndpointTrustedCA'],
            self.tsets['bdii']['glue_two_basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2EndpointSupportedProfile'])
        self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2EndpointInterfaceExtension'])
        self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2EndpointIssuerCA'])
        self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2EndpointTrustedCA'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_gluetwo_storage_undefined(self):
        self.lfn.put_name(self.uid['test_gluetwo_storage_undefined'][5])
        self.lfn.put_description(self.uid['test_gluetwo_storage_undefined'][6])
        if self.uid.has_key('test_gluetwo_storage_undefined'):
            self.lfn.put_uuid(self.uid['test_gluetwo_storage_undefined'][0])
        else:
            print 'ADD UID for test_gluetwo_storage_undefined'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid(self.uid['test_gluetwo_storage_undefined'][2])
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            "(objectclass=GLUE2StorageShare)",
            ['GLUE2StorageShareAccessMode'],
            self.tsets['bdii']['glue_two_basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        self.assert_('to be defined' not in ls_result['glue2.0']['GLUE2StorageShareAccessMode'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_gluetwo_endpoint(self):
        self.lfn.put_name(self.uid['test_gluetwo_endpoint'][5])
        self.lfn.put_description(self.uid['test_gluetwo_endpoint'][6])
        if self.uid.has_key('test_gluetwo_endpoint'):
            self.lfn.put_uuid(self.uid['test_gluetwo_endpoint'][0])
        else:
            print 'ADD UID for test_gluetwo_endpoint'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid(self.uid['test_gluetwo_endpoint'][2])
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            "(&(objectclass=GLUE2Endpoint)(GLUE2EndpointInterfaceName=emi.storm))", 
            ['GLUE2EndpointCapability'], self.tsets['bdii']['glue_two_basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        self.assert_('implementation.model' not in ls_result['glue2.0']['GLUE2EndpointCapability'])
        self.assert_('implementation.discovery' not in ls_result['glue2.0']['GLUE2EndpointCapability'])
        self.assert_('implementation.monitoring' not in ls_result['glue2.0']['GLUE2EndpointCapability'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_gluetwo_service(self):
        self.lfn.put_name(self.uid['test_gluetwo_service'][5])
        self.lfn.put_description(self.uid['test_gluetwo_service'][6])
        if self.uid.has_key('test_gluetwo_service'):
            self.lfn.put_uuid(self.uid['test_gluetwo_service'][0])
        else:
            print 'ADD UID for test_gluetwo_service'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid(self.uid['test_gluetwo_service'][2])
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            "(&(objectclass=GLUE2Service))",
            ['GLUE2StorageServie'], self.tsets['bdii']['glue_two_basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        self.assert_('GLUE2StorageService' not in ls_result['glue2.0']['GLUE2Service'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
