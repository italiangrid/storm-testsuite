__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional import functionalities as fu
from tstorm.tests.functional import https
from tstorm.tests.atomic import atomics
from tstorm.tests import utilities 


def ts_cksm(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_cksm'][5])
    lfn.put_description(uid['ts_cksm'[6])
    lfn.put_uuid(uid['ts_cksm'][0])
    lfn.put_output()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_cksm',conf, ifn, dfn, bifn, lfn)) 
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))

    return s

def ts_dt(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_dt'][5])
    lfn.put_description(uid['ts_dt'][6])
    lfn.put_uuid(uid['ts_dt'][0])
    lfn.put_output()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_out_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_out_exist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_in_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_in_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))

    return s

def ts_https_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_https_voms'][5])
    lfn.put_description(uid['ts_https_voms'][6])
    lfn.put_uuid(uid['ts_https_voms'][0])
    lfn.put_output()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_outbound_https_voms', conf, ifn, dfn, bifn, 'https', lfn, voms = True))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https_voms', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_outbound_https_voms_exist_file', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_voms', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_voms_no_auth', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(https.HttpsTest('test_direct_transfer_inbound_https_voms_unexist_file', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(https.HttpsTest('test_srm_transfer_inbound_https_voms',conf, ifn, dfn, bifn, 'https', lfn, voms = True))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))

    return s

def ts_cw(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_cw'][5])
    lfn.put_description(uid['ts_cw'][6])
    lfn.put_uuid(uid['ts_cw'][0])
    lfn.put_output()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_in',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_unexist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))

    return s
