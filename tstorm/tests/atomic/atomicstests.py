__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.atomic import atomics
from tstorm.tests import utilities

def ts_storm_ping(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_storm_ping'][6])
    lfn.put_description(uid['ts_storm_ping'][7])
    lfn.put_uuid(uid['ts_storm_ping'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(atomics.AtomicsTest('test_storm_ping',conf, ifn, dfn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_storm_ping_wo(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_storm_ping_wo'][6])
    lfn.put_description(uid['ts_storm_ping_wo'][7])
    lfn.put_uuid(uid['ts_storm_ping_wo'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(atomics.AtomicsTest('test_storm_ping_wo',conf, ifn, dfn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_storm_gtp(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_storm_gtp'][6])
    lfn.put_description(uid['ts_storm_gtp'][7])
    lfn.put_uuid(uid['ts_storm_gtp'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(atomics.AtomicsTest('test_storm_gtp',conf, ifn, dfn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_storm_gtp_wo(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_storm_gtp_wo'][6])
    lfn.put_description(uid['ts_storm_gtp_wo'][7])
    lfn.put_uuid(uid['ts_storm_gtp_wo'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(atomics.AtomicsTest('test_storm_gtp_wo',conf, ifn, dfn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_lcg_ls_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_lcg_ls_unexist_file'][6])
    lfn.put_description(uid['ts_lcg_ls_unexist_file'][7])
    lfn.put_uuid(uid['ts_lcg_ls_unexist_file'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_dcache_mkdir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_dcache_mkdir'][6])
    lfn.put_description(uid['ts_dcache_mkdir'][7])
    lfn.put_uuid(uid['ts_dcache_mkdir'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_dcache_mkdir_exist(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_dcache_mkdir_exist'][6])
    lfn.put_description(uid['ts_dcache_mkdir_exist'][7])
    lfn.put_uuid(uid['ts_dcache_mkdir_exist'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_lcg_ls_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_lcg_ls_dir'][6])
    lfn.put_description(uid['ts_lcg_ls_dir'][7])
    lfn.put_uuid(uid['ts_lcg_ls_dir'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_mkdir_exist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_lcg_cp_out(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_lcg_cp_out'][6])
    lfn.put_description(uid['ts_lcg_cp_out'][7])
    lfn.put_uuid(uid['ts_lcg_cp_out'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_lcg_ls_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_lcg_ls_file'][6])
    lfn.put_description(uid['ts_lcg_ls_file'][7])
    lfn.put_uuid(uid['ts_lcg_ls_file'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_dcache_rm_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_dcache_rm_file'][6])
    lfn.put_description(uid['ts_dcache_rm_file'][7])
    lfn.put_uuid(uid['ts_dcache_rm_file'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_dcache_rm_unexist_file(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_dcache_rm_unexist_file'][6])
    lfn.put_description(uid['ts_dcache_rm_unexist_file'][7])
    lfn.put_uuid(uid['ts_dcache_rm_unexist_file'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_unexist_file',conf, ifn, dfn, bifn, lfn)) 
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_dcache_rm_unexist_dir(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_dcache_rm_unexist_dir'][6])
    lfn.put_description(uid['ts_dcache_rm_unexist_dir'][7])
    lfn.put_uuid(uid['ts_dcache_rm_unexist_dir'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_unexist_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    lfn.put_prologue()

    return s

def ts_lcg_cp_in(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_lcg_cp_in'][6])
    lfn.put_description(uid['ts_lcg_cp_in'][7])
    lfn.put_uuid(uid['ts_lcg_cp_in'][0])
    lfn.put_output()
    lfn.flush_file()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_ls_unexist_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_out',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_lcg_cp_in',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_file',conf, ifn, dfn, bifn, lfn))
    s.addTest(atomics.AtomicsTest('test_dcache_rm_dir',conf, ifn, dfn, bifn, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, lfn))
    lfn.put_prologue()

    return s
