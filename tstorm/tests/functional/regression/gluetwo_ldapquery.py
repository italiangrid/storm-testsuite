import datetime
import time
import os 
import unittest
from tstorm.utils import configuration
from tstorm.utils import ldapsearch 
from tstorm.utils import utils

__author__ = 'Elisabetta Ronchieri'

class GluetwoLdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, lfn, filter='', attributes=''):
        super(GluetwoLdapTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.filter = filter
        self.attributes = attributes
        self.lfn=lfn

    def test_gluetwo_storage_share_capacity(self):
        ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
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
            self.assert_(int(ls_result['glue2.0']['GLUE2StorageServiceCapacityTotalSize']) >= 0)
        else:
            self.assert_(ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_gluetwo_endpoint_undefined(self):
        ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
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
        ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
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
        ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
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
        ldap_search = ldapsearch.LdapSearch(self.tsets['bdii']['endpoint'],
            "(&(objectclass=GLUE2Service))",
            ['GLUE2StorageServie'], self.tsets['bdii']['glue_two_basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
