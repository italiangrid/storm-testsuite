#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.test import utilities as ut

def conf_ts(conf, lfn, ifn, dfn, bifn, lfn):
  s = unittest.TestSuite()
  s.addTest(ut.UtilitiesTest('test_settings', conf, lfn, ifn, dfn, bifn, lfn))

  return s
