__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional.regression import glueone_ldapquery 
from tstorm.tests.functional.regression import gluetwo_ldapquery

# test for glue1.3

def ts_glueone_service(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(glueone_ldapquery.LdapTest('test_glueone_service',
       conf, lfn,
       'objectClass=GlueService',
       ['GlueServiceType', 'GlueServiceName']))
    return s

def ts_gluetwo_endpoint_undefined(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_gluetwo_endpoint_undefined',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    return s

def ts_gluetwo_storage_share_capacity(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_storage_share_capacity',
        conf, lfn))
    return s

def ts_gluetwo_endpoint_undefined(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_endpoint_undefined',
        conf, lfn))
    return s

def ts_gluetwo_storage_undefined(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_storage_undefined',
        conf, lfn))
    return s

def ts_gluetwo_endpoint(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_endpoint',
        conf, lfn))
    return s

def ts_gluetwo_service(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_service',
        conf, lfn))
    return s
