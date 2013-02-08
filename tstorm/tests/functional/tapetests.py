__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional import tape
from tstorm.tests import utilities

def ts_access_tape_lcg(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, uid, lfn))
    s.addTest(tape.TapeTest('test_access_tape_lcg',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_access_tape_storm(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_dd',conf, ifn, bifn, uid, lfn))
    s.addTest(tape.TapeTest('test_access_tape_storm',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

#def ts_access_tape(conf, ifn, dfn, bifn):
#    s = unittest.TestSuite()
#    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn))
#    s.addTest(tp.TapeTest('test_access_tape',conf, ifn, dfn, bifn))
#    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn))

    return s
