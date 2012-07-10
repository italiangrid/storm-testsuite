__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional.regression import regression as re

def ts_update_free_space_upon_rm(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_update_free_space_upon_rm'][6])
    lfn.put_description(uid['ts_update_free_space_upon_rm'][7])
    lfn.put_uuid(uid['ts_update_free_space_upon_rm'][0])
    lfn.put_ruid(self.uid['ts_update_free_space_upon_rm'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_update_free_space_upon_rm',conf, ifn, dfn, bifn, lfn))

    return s

def ts_eight_digit_string_checksum(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_eight_digit_string_checksum'][6])
    lfn.put_description(uid['ts_eight_digit_string_checksum'][7])
    lfn.put_uuid(uid['ts_eight_digit_string_checksum'][0])
    lfn.put_ruid(self.uid['ts_update_free_space_upon_rm'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_eight_digit_string_checksum',conf, ifn, dfn, bifn, lfn))
  
    return s

def ts_update_used_space_upon_pd(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_update_used_space_upon_pd'][6])
    lfn.put_description(uid['ts_update_used_space_upon_pd'][7])
    lfn.put_uuid(uid['ts_update_used_space_upon_pd'][0])
    lfn.put_ruid(self.uid['ts_update_used_space_upon_pd'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_update_used_space_upon_pd',conf, ifn, dfn, bifn, lfn))

    return s

def ts_unsupported_protocols(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_unsupported_protocols'][6])
    lfn.put_description(uid['ts_unsupported_protocols'][7])
    lfn.put_uuid(uid['ts_unsupported_protocols'][0])
    lfn.put_ruid(self.uid['ts_unsupported_protocols'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_unsupported_protocols',conf, ifn, dfn, bifn, lfn))

    return s

def ts_both_sup_and_unsup_protocols(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_both_sup_and_unsup_protocols'][6])
    lfn.put_description(uid['ts_both_sup_and_unsup_protocols'][7])
    lfn.put_uuid(uid['ts_both_sup_and_unsup_protocols'][0])
    lfn.put_ruid(self.uid['ts_both_sup_and_unsup_protocols'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_both_sup_and_unsup_protocols',conf, ifn, dfn, bifn, lfn, prt = 'gsiftp,file'))

    return s

def ts_non_ascii_chars(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_non_ascii_chars'][6])
    lfn.put_description(uid['ts_non_ascii_chars'][7])
    lfn.put_uuid(uid['ts_non_ascii_chars'][0])
    lfn.put_ruid(self.uid['ts_non_ascii_chars'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_non_ascii_chars', conf, ifn, dfn, bifn, lfn))

    return s

def ts_storm_backend_age(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_storm_backend_age'][6])
    lfn.put_description(uid['ts_storm_backend_age'][7])
    lfn.put_uuid(uid['ts_storm_backend_age'][0])
    lfn.put_ruid(self.uid['ts_storm_backend_age'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_storm_backend_age', conf, ifn, dfn, bifn, lfn))

    return s

def ts_storm_database_password(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_storm_database_password'][6])
    lfn.put_description(uid['ts_storm_database_password'][7])
    lfn.put_uuid(uid['ts_storm_database_password'][0])
    lfn.put_ruid(self.uid['ts_storm_database_password'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_storm_database_password', conf, ifn, dfn, bifn, lfn))

    return s

def ts_storm_gridhttps_authorization_denied(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_storm_gridhttps_authorization_denied'][6])
    lfn.put_description(uid['ts_storm_gridhttps_authorization_denied'][7])
    lfn.put_uuid(uid['ts_storm_gridhttps_authorization_denied'][0])
    lfn.put_ruid(self.uid['ts_storm_gridhttps_authorization_denied'][3])
    lfn.flush_file()

    s.addTest(re.RegressionTest('test_storm_gridhttps_authorization_denied', conf, ifn, dfn, bifn, lfn))

    return s
