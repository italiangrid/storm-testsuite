__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional.regression import regression as re

def ts_update_free_space_upon_rm(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_update_free_space_upon_rm',conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_eight_digit_string_checksum(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_eight_digit_string_checksum',conf, ifn, dfn, bifn, uid, lfn))
  
    return s

def ts_update_used_space_upon_pd(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_update_used_space_upon_pd',conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_unsupported_protocols(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_unsupported_protocols',conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_both_sup_and_unsup_protocols(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_both_sup_and_unsup_protocols',conf, ifn, dfn, bifn, uid, lfn, prt = 'gsiftp,file'))

    return s

def ts_non_ascii_chars(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_non_ascii_chars', conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_storm_backend_age(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_backend_age', conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_storm_database_password(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_database_password', conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_storm_gridhttps_authorization_denied(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_gridhttps_authorization_denied', conf, ifn, dfn, bifn, uid, lfn))

    return s
