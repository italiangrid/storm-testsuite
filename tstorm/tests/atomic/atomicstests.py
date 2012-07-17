__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.atomic import atomics
from tstorm.tests import utilities

def ts_dcache_ping(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_dcache_ping',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_ping(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_ping',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_ping_wo(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_ping_wo',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_gtp(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_gtp',conf, ifn, dfn, bifn, lfn))
    return s

def ts_storm_gtp_wo(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_gtp_wo',conf, ifn, dfn, bifn, lfn))
    return s

def ts_lcg_ls_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    return s

def ts_lcg_ls_unexist_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_dcache_mkdir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_dcache_mkdir_exist(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_dcache_rm_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_lcg_ls_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    return s

def ts_lcg_cp_out(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_lcg_ls_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_dcache_rm_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_dcache_rm_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    #s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_unexist_file',conf, ifn, dfn, bifn, lfn)) 
    #s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_dcache_rm_unexist_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    #s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_unexist_dir',conf, ifn, dfn, bifn, lfn))
    #s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s

def ts_lcg_cp_in(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_in',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    return s
