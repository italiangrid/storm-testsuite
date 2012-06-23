__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional import functionalities as fu
from tstorm.tests.functional import https
from tstorm.tests.atomic import atomics
from tstorm.tests import utilities 


def ts_cksm(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(fu.FunctionalitiesTest('test_cksm',conf, ifn, dfn, bifn, uid, lfn)) 
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_dt(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_out_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_out_exist_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_in_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_in_unexist_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_https_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https_voms', conf, ifn, dfn, bifn, 'https', uid, lfn, voms = True))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https_voms', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https_voms_exist_file', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_voms', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_voms_no_auth', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_voms_unexist_file', conf, ifn, dfn, bifn, 'https', uid, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_inbound_https_voms',conf, ifn, dfn, bifn, 'https', uid, lfn, voms = True))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))

    return s

def ts_cw(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_unexist_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_exist_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_at',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_unexist_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_unexist_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))

    return s
