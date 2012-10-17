__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.load import loads
from tstorm.tests import utilities

def ts_storm_get_transfer_protocols(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(loads.LoadsTest('test_storm_get_transfer_protocols',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_ls_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(load.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
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
    s.addTest(laods.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
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

def ts_storm_cp_out(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_ls_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_rm_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(loads.LoadsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_storm_cp_in(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_storm_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_storm_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_storm_cp_in',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_storm_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_storm_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s
