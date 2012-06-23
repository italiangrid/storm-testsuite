__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests import utilities

def ts_conf(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_settings', conf, ifn, dfn, bifn, uid, lfn))

    return s
