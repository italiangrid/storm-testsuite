__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment.regression import ldapquery 
from tstorm.tests.deployment.regression import gluetwo_ldapquery

# test for glue1.3

def ts_glue_service(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_glue_service'][6])
    lfn.put_description(uid['ts_glue_service'][7])
    lfn.put_uuid(uid['ts_glue_service'][0])
    lfn.put_ruid(uid['ts_glue_service'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(ldapquery.LdapTest('test_glue_service',
       conf, lfn,
       'objectClass=GlueService',
       ['GlueServiceType', 'GlueServiceName']))
    lfn.put_prologue()

    return s

def ts_glue_available_space_info_service(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_glue_available_space_info_service'][6])
    lfn.put_description(uid['ts_glue_available_space_info_service'][7])
    lfn.put_uuid(uid['ts_glue_available_space_info_service'][0])
    lfn.put_ruid(uid['ts_glue_available_space_info_service'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(ldapquery.LdapTest('test_glue_available_space_info_service',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    lfn.put_prologue()

    return s

def ts_glue_available_space(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_glue_available_space'][6])
    lfn.put_description(uid['ts_glue_available_space'][7])
    lfn.put_uuid(uid['ts_glue_available_space'][0])
    lfn.put_ruid(uid['ts_glue_available_space'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(ldapquery.LdapTest('test_glue_available_space',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    lfn.put_prologue()

    return s

def ts_glue_used_space(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_glue_used_space'][6])
    lfn.put_description(uid['ts_glue_used_space'][7])
    lfn.put_uuid(uid['ts_glue_used_space'][0])
    lfn.put_ruid(uid['ts_glue_used_space'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(ldapquery.LdapTest('test_glue_used_space',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    lfn.put_prologue()

    return s

def ts_size(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_size'][6])
    lfn.put_description(uid['ts_size'][7])
    lfn.put_uuid(uid['ts_size'][0])
    lfn.put_ruid(uid['ts_size'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(ldapquery.LdapTest('test_size',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    lfn.put_prologue()

    return s

def ts_info_service_failure(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_info_service_failure'][6])
    lfn.put_description(uid['ts_info_service_failure'][7])
    lfn.put_uuid(uid['ts_info_service_failure'][0])
    lfn.put_ruid(uid['ts_info_service_failure'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(ldapquery.LdapTest('test_info_service_failure',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    lfn.put_prologue()

    return s

def ts_gluetwo_endpoint_undefined(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_gluetwo_endpoint_undefined'][6])
    lfn.put_description(uid['ts_gluetwo_endpoint_undefined'][7])
    lfn.put_uuid(uid['ts_gluetwo_endpoint_undefined'][0])
    lfn.put_ruid(uid['ts_gluetwo_endpoint_undefined'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(ldapquery.LdapTest('test_gluetwo_endpoint_undefined',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    lfn.put_prologue()

    return s

def ts_gluetwo_storage_share_capacity(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_gluetwo_storage_share_capacity'][6])
    lfn.put_description(uid['ts_gluetwo_storage_share_capacity'][7])
    lfn.put_uuid(uid['ts_gluetwo_storage_share_capacity'][0])
    lfn.put_ruid(uid['ts_gluetwo_storage_share_capacity'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_storage_share_capacity',
        conf, lfn))
    lfn.put_prologue()

    return s

def ts_gluetwo_endpoint_undefined(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_gluetwo_endpoint_undefined'][6])
    lfn.put_description(uid['ts_gluetwo_endpoint_undefined'][7])
    lfn.put_uuid(uid['ts_gluetwo_endpoint_undefined'][0])
    lfn.put_ruid(uid['ts_gluetwo_endpoint_undefined'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_endpoint_undefined',
        conf, lfn))
    lfn.put_prologue()

    return s

def ts_gluetwo_storage_undefined(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_gluetwo_storage_undefined'][6])
    lfn.put_description(uid['ts_gluetwo_storage_undefined'][7])
    lfn.put_uuid(uid['ts_gluetwo_storage_undefined'][0])
    lfn.put_ruid(uid['ts_gluetwo_storage_undefined'][3])
    lfn.put_output()
    lfn.flush_file()     
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_storage_undefined',
        conf, lfn))
    lfn.put_prologue()

    return s

def ts_gluetwo_endpoint(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_gluetwo_endpoint'][6])
    lfn.put_description(uid['ts_gluetwo_endpoint'][7])
    lfn.put_uuid(uid['ts_gluetwo_endpoint'][0])
    lfn.put_ruid(uid['ts_gluetwo_endpoint'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_endpoint',
        conf, lfn))
    lfn.put_prologue()

    return s

def ts_gluetwo_service(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_gluetwo_service'][6])
    lfn.put_description(uid['ts_gluetwo_service'][7])
    lfn.put_uuid(uid['ts_gluetwo_service'][0])
    lfn.put_ruid(uid['ts_gluetwo_service'][3])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(gluetwo_ldapquery.GluetwoLdapTest('test_gluetwo_service',
        conf, lfn))
    lfn.put_prologue()

    return s
