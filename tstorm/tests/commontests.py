#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests import utilities as ut

def conf_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(ut.UtilitiesTest('test_settings', conf, ifn, dfn, bifn, uid, lfn))

    return s
