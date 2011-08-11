#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.utils import settings as st
from tstorm.test import regression as re
from tstorm.test import functionalities as fu
from tstorm.test import utilities as ut
from tstorm.test import ldapquery as lq

def update_free_space_upon_rm(conf, ifn, dfn, bifn):
  s = unittest.TestSuite()
  s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn))
  s.addTest(re.RegressionTest('test_update_free_space_upon_rm',conf, ifn, dfn, bifn))
  s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn))

  return s

def eight_digit_string_checksum_rts(conf, ifn, dfn, bifn):
  s = unittest.TestSuite()
  s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn))
  s.addTest(re.RegressionTest('test_eight_digit_string_checksum',conf, ifn, dfn, bifn))
  s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn))
  
  return s

def update_used_space_upon_pd(conf, ifn, dfn, bifn):
  s = unittest.TestSuite()
  s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn))
  s.addTest(re.RegressionTest('test_update_used_space_upon_pd',conf, ifn, dfn, bifn))
  s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn))

  return s

def unsupported_protocols(conf, ifn, dfn, bifn):
  s = unittest.TestSuite()
  s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn))
  s.addTest(re.RegressionTest('test_unsupported_protocols',conf, ifn, dfn, bifn))
  s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn))

  return s

def protocols(conf, ifn, dfn, bifn):
  s = unittest.TestSuite()
  s.addTest(ut.UtilitiesTest('test_dd',conf, ifn, dfn, bifn))
  s.addTest(re.RegressionTest('test_both_sup_and_unsup_protocols',conf, ifn, dfn, bifn, 'gsiftp, file'))
  s.addTest(ut.UtilitiesTest('test_rm_lf',conf, ifn, dfn, bifn))

  return s

def glue_information(conf):
  s = unittest.TestSuite()
  s.addTest(lq.LdapTest('test_glue_service', conf))

  return s

def non_ascii_chars(conf, ifn, dfn, bifn):
  s = unittest.TestSuite()
  s.addTest(re.RegressionTest('test_non_ascii_chars', conf, ifn, dfn, bifn))
  s.addTest(fu.FunctionalitiesTest('test_storm_ping',conf, ifn, dfn, bifn)) 

  return s
