__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional.regression import regression as re

def ts_prepare_to_put_wrong_space_token(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_prepare_to_put_wrong_space_token',conf, ifn, dfn, bifn, lfn))
    return s

#NOT IMPLEMENTED
#"ts_prepare_to_put_expired_space_token":[
#"c396a2",
#"ST",
#true,
#[["https://storm.cnaf.infn.it:8443/redmine/issues/282","[1.8.3-1,*)"]],
#false,
#"PREPARE TO PUT WRONG ERROR CODE",
#"PrepareToPut returns SRM_SPACE_LIFETIME_EXPIRED instead of SRM_INVALID_REQUEST",
#"rt.ts_prepare_to_put_expired_space_token(tfn,ifn,dfn,back_ifn, uid,lfn)"
#],

def ts_prepare_to_put_expired_space_token(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_prepare_to_put_expired_space_token',conf, ifn, dfn, bifn, lfn))
    return s

def ts_get_space_metadata_on_valid_space_token(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_get_space_metadata_on_valid_space_token',conf, ifn, dfn, bifn, lfn))
    return s

def ts_update_free_space_upon_rm(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_update_free_space_upon_rm',conf, ifn, dfn, bifn, lfn))
    return s

def ts_eight_digit_string_checksum(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_eight_digit_string_checksum',conf, ifn, dfn, bifn, lfn))
    return s

def ts_update_used_space_upon_pd(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_update_used_space_upon_pd',conf, ifn, dfn, bifn, lfn))
    return s

def ts_unsupported_protocols(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_unsupported_protocols',conf, ifn, dfn, bifn, lfn))
    return s

def ts_both_sup_and_unsup_protocols(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_both_sup_and_unsup_protocols',conf, ifn, dfn, bifn, lfn, prt = 'gsiftp,file'))
    return s

def ts_non_ascii_chars(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_non_ascii_chars', conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_backend_age(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_backend_age', conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_database_password(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_database_password', conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_gridhttps_authorization_denied(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_storm_gridhttps_authorization_denied', conf, ifn, dfn, bifn, lfn))
    return s
