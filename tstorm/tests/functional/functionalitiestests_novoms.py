__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional import https 
from tstorm.tests.functional import functionalities as fu
from tstorm.tests import utilities 

def ts_srm_transfer_outbound_http(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_outbound_http(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_outbound_http_exist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_http_exist_file', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_inbound_http(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_inbound_http_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_http_unexist_file', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_srm_transfer_inbound_http(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_inbound_http',conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_http(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_http_exist_file', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_http', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_http_unexist_file', conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_inbound_http',conf, ifn, dfn, bifn, 'http', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_srm_transfer_outbound_https(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_outbound_https(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_outbound_https_exist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https_exist_file', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_inbound_https(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_inbound_https_no_auth(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_no_auth', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_direct_transfer_inbound_https_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_unexist_file', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_srm_transfer_inbound_https(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_inbound_https',conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_https(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https_exist_file', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_no_auth', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_unexist_file', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_inbound_https',conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s
