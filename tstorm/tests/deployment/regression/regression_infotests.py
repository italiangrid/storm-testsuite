__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment.regression import info_ldapquery 

# test for glue1.3

def ts_available_space_info_service(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(info_ldapquery.InfoTest('test_available_space_info_service',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    return s

def ts_available_space(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(info_ldapquery.InfoTest('test_available_space',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    return s

def ts_used_space(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(info_ldapquery.InfoTest('test_used_space',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    return s

def ts_size(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(info_ldapquery.InfoTest('test_size',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    return s

def ts_service_failure(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(info_ldapquery.InfoTest('test_info_service_failure',
        conf, lfn,
        'objectclass=GlueSA',
        ['GlueSALocalID']))
    return s

