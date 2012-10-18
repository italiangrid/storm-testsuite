__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.atomic import atomics
from tstorm.tests.load import loads
from tstorm.tests import utilities

def ts_storm_get_transfer_protocols(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_get_transfer_protocols',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_ls_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_ls_unexist_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_rm_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_rm_unexist_file',conf, ifn, dfn, bifn, lfn))         
    return s

def ts_storm_rm_unexist_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_rm_unexist_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_mkdir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_mkdir_exist(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_rm_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_ls_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_prepare_to_put(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_prepare_to_put',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_fake_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_prepare_to_put_exist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_prepare_to_put_exist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_put_done(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_put_done',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_fake_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_ls_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_prepare_to_put',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_fake_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_rm_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_prepare_to_put',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_fake_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_prepare_to_get(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_prepare_to_get',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_prepare_to_get_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_prepare_to_get_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_release_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_release_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s
