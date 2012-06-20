__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.atomic import atomics
from tstorm.tests import utilities

def ts_ping(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_ping',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_ping_wo(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_ping_wo',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_gtp(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_gtp',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_gtp_wo(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_gtp_wo',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_ls_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    #s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_unexist_file',conf, ifn, dfn, bifn, uid, lfn))
    #s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_mkdir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    #s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    #s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_mkdir_exist(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    #s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_exist_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    #s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_ls_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    #s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_exist_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    #s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_cp_out(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_ls_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_rm_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn)) 
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_rm_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_unexist_file',conf, ifn, dfn, bifn, uid, lfn)) 
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_rm_unexist_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_unexist_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_cp_in(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_at',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s
