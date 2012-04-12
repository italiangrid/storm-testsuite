#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests import regression as re

def update_free_space_upon_rm_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_update_free_space_upon_rm',conf, ifn, dfn, bifn, uid, lfn))

    return s

def eight_digit_string_checksum_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_eight_digit_string_checksum',conf, ifn, dfn, bifn, uid, lfn))
  
    return s

def update_used_space_upon_pd_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_update_used_space_upon_pd',conf, ifn, dfn, bifn, uid, lfn))

    return s

def unsupported_protocols_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_unsupported_protocols',conf, ifn, dfn, bifn, uid, lfn))

    return s

def both_sup_and_unsup_protocols_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_both_sup_and_unsup_protocols',conf, ifn, dfn, bifn, uid, lfn, prt = 'gsiftp,file'))

    return s

def non_ascii_chars_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_non_ascii_chars', conf, ifn, dfn, bifn, uid, lfn))

    return s

def storm_backend_age_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_backend_age', conf, ifn, dfn, bifn, uid, lfn))

    return s

def storm_database_password_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_database_password', conf, ifn, dfn, bifn, uid, lfn))

    return s

def storm_gridhttps_authorization_denied_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_gridhttps_authorization_denied', conf, ifn, dfn, bifn, uid, lfn))

    return s
