#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.test import functionalities as fu
from tstorm.test import atomics
from tstorm.test import utilities as ut
from tstorm.test import https as h

def cs_ts(conf, ifn, dfn, bifn, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_ping',conf, ifn, dfn, bifn, lfn))

    return s

def cw_ts(conf, ifn, dfn, bifn, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_at',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_unexist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, lfn))
  
    return s

def cksm_ts(conf, ifn, dfn, bifn, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_cksm',conf, ifn, dfn, bifn, lfn)) 
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, lfn))

    return s

def dt_ts(conf, ifn, dfn, bifn, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_out_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_out_exist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_in_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_data_transfer_in_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(fu.FunctionalitiesTest('test_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, lfn))

    return s

def https_voms_ts(conf, ifn, dfn, bifn, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_cr_lf',conf, ifn, dfn, bifn, lfn))
    s.addTest(h.HttpsTest('test_srm_transfer_outbound_https_voms', conf, ifn, dfn, bifn, 'https', lfn, voms = True))
    s.addTest(h.HttpsTest('test_direct_transfer_outbound_https_voms', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_outbound_https_voms_exist_file', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_inbound_https_voms', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_inbound_https_voms_no_auth', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_direct_transfer_inbound_https_voms_unexist_file', conf, ifn, dfn, bifn, 'https', lfn))
    s.addTest(h.HttpsTest('test_srm_transfer_inbound_https_voms',conf, ifn, dfn, bifn, 'https', lfn, voms = True))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, lfn))

    return s
