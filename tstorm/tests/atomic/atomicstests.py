__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.atomic import atomics
from tstorm.tests import utilities as ut

#def cs_ts(conf, ifn, dfn, bifn, uid, lfn):
def ping_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_ping',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ping_wo_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_ping_wo',conf, ifn, dfn, bifn, uid, lfn))
    return s

def gtp_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_gtp',conf, ifn, dfn, bifn, uid, lfn))
    return s

def gtp_wo_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(atomics.AtomicsTest('test_storm_gtp_wo',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ls_unexist_file_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_unexist_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def mkdir_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def mkdir_exist_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_exist_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ls_dir_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_mkdir_exist_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def cp_out_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ls_file_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def rm_file_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn)) 
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_ls_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def rm_unexist_file_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_unexist_file',conf, ifn, dfn, bifn, uid, lfn)) 
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def rm_unexist_dir_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_unexist_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s

def cp_in_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_bt',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_cp_at',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_file',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(atomics.AtomicsTest('test_rm_dir',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn, uid, lfn))
    return s
