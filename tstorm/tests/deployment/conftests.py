__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment import conf

def ts_yaim_storm_pepc_resourceid_variable(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_yaim_storm_pepc_resourceid_variable', conf, uid, lfn))
    return s

def ts_emir_serp_added(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_emir_serp_added', conf, uid, lfn))
    return s

def ts_gridhttps_certificates_folder_added(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_gridhttps_certificates_folder_added', conf, uid, lfn))
    return s
