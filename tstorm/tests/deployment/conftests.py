__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment import conf

def ts_yaim_storm_pepc_resourceid_variable(config, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_yaim_storm_pepc_resourceid_variable', config, uid, lfn))
    return s

def ts_gridhttps_certificates_folder_added(config, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_gridhttps_certificates_folder_added', config, uid, lfn))
    return s

def ts_gridhttps_conf_folder_ownership(config, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_gridhttps_conf_folder_ownership', config, uid, lfn))
    return s

def ts_yaim_dn_regex_variable_added(config, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_yaim_dn_regex_variable_added', config, uid, lfn))
    return s

def ts_yaim_anonymous_access_added(config, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_yaim_anonymous_access_added', config, uid, lfn))
    return s
