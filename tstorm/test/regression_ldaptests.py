#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.test import functionalities as fu
from tstorm.test import ldapquery as lq
from tstorm.test import utilities as ut

def glue_info_ts(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(lq.LdapTest('test_glue_service', conf, lfn))

    return s

def glue_storage_share_capacity_ts(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(lq.LdapTest('test_glue_storage_share_capacity', conf, lfn))

    return s

def glue_available_space_info_service_ts(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(lq.LdapTest('test_glue_available_space_info_service', conf, lfn))

    return s

def glue_available_space_ts(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(lq.LdapTest('test_glue_available_space', conf, lfn))

    return s

def glue_used_space_ts(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(lq.LdapTest('test_glue_used_space', conf, lfn))

    return s

def size_ts(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(lq.LdapTest('test_size', conf, lfn))

    return s

def info_service_failure_ts(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(lq.LdapTest('test_info_service_failure', conf, lfn))
    
    return s
