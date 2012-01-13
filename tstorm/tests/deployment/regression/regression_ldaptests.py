#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment.regression import ldapquery 

def gluetwo_service_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_gluetwo_service', conf, uid, lfn,
       basedn = 'mds-vo-name=resource,o=grid',
       filter = 'objectClass=GlueService',
       attributes = ['GlueServiceType', 'GlueServiceName']))

    return s

def gluetwo_storage_share_capacity_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_gluetwo_storage_share_capacity', conf, uid, lfn))

    return s

def glue_available_space_info_service_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_glue_available_space_info_service', conf, uid, lfn))

    return s

def glue_available_space_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_glue_available_space', conf, uid, lfn))

    return s

def glue_used_space_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_glue_used_space', conf, uid, lfn))

    return s

def size_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_size', conf, uid, lfn))

    return s

def info_service_failure_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_info_service_failure', conf, uid, lfn))
    
    return s

def gluetwo_endpoint_undefined_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_gluetwo_endpoint_undefined', conf, uid, lfn))

    return s

def gluetwo_storage_undefined_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_gluetwo_storage_undefined', conf, uid, lfn))

    return s

def gluetwo_endpoint_ts(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ldapquery.LdapTest('test_gluetwo_endpoint', conf, uid, lfn))

    return s
