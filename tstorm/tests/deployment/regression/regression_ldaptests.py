__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment.regression import ldapquery 
from tstorm.tests.deployment.regression import gluetwo_ldapquery

# test for glue1.3

def ts_glue_service(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_glue_service',
       conf, uid, lfn,
       'objectClass=GlueService',
       ['GlueServiceType', 'GlueServiceName']))

    return s

def ts_glue_available_space_info_service(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_glue_available_space_info_service',
        conf, uid, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))

    return s

def ts_glue_available_space(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_glue_available_space',
        conf, uid, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))

    return s

def ts_glue_used_space(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_glue_used_space',
        conf, uid, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))

    return s

def ts_size(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_size',
        conf, uid, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))

    return s

def ts_info_service_failure(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_info_service_failure',
        conf, uid, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    
    return s

def ts_gluetwo_endpoint_undefined(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_gluetwo_endpoint_undefined',
        conf, uid, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))

    return s

def ts_gluetwo_storage_share_capacity(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_storage_share_capacity',
        conf, uid, lfn))

    return s

def ts_gluetwo_endpoint_undefined(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_endpoint_undefined',
        conf, uid, lfn))

    return s

def ts_gluetwo_storage_undefined(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_storage_undefined',
        conf, uid, lfn))

    return s

def ts_gluetwo_endpoint(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_endpoint',
        conf, uid, lfn))

    return s

def ts_gluetwo_service(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_service',
        conf, uid, lfn))

    return s
