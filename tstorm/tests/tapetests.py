#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.test import tape as tp
from tstorm.test import utilities as ut

def access_tape_ts(conf, ifn, dfn, bifn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn))
    s.addTest(tp.TapeTest('test_verify_tsa2',conf, ifn, dfn, bifn))
    s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn))

    return s
