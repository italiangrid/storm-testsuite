__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional import https as h
from tstorm.tests.functional import functionalities as fu
from tstorm.tests import utilities as ut

def ts_http(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_cr_lf',conf, ifn, bifn, lfn))
    s.addTest(h.HttpsTest('test_srm_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_outbound_http', conf, ifn, dfn, bifn, 'http', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_outbound_http_exist_file', conf, ifn, dfn, bifn, 'http', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_inbound_http', conf, ifn, dfn, bifn, 'http', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_inbound_http_unexist_file', conf, ifn, dfn, bifn, 'http', lfn))
    s.addTest(h.HttpsTest('test_srm_transfer_inbound_http',conf, ifn, dfn, bifn, 'http', lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_https(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_cr_lf',conf, ifn, bifn, lfn))
    s.addTest(h.HttpsTest('test_srm_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_outbound_https', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_outbound_https_exist_file', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_inbound_https', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_inbound_https_no_auth', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_inbound_https_unexist_file', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_srm_transfer_inbound_https',conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s
