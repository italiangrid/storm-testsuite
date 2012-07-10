__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional import https as h
from tstorm.tests.functional import functionalities as fu
from tstorm.tests import utilities as ut

def ts_http(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_http'][6])
    lfn.put_description(uid['ts_http'][7])
    lfn.put_uuid(uid['ts_http'][0])
    lfn.flush_file()

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

    lfn.put_name(uid['ts_https'][6])
    lfn.put_description(uid['ts_https'][7])
    lfn.put_uuid(uid['ts_https'][0])
    lfn.flush_file()

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
