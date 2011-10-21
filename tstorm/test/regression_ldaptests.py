#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.test import regression as re
from tstorm.test import functionalities as fu
from tstorm.test import utilities as ut
from tstorm.test import ldapquery as lq

def glue_info_ts(conf):
  s = unittest.TestSuite()
  s.addTest(lq.LdapTest('test_glue_service', conf))

  return s

def glue_storage_share_capacity_ts(conf):
  s = unittest.TestSuite()
  s.addTest(lq.LdapTest('test_glue_storage_share_capacity', conf))

  return s
