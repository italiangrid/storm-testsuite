#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.test import regression_conf as rec

def backend_logrotate_conf_ts():
  s = unittest.TestSuite()
  s.addTest(rec.RegressionConfigurationTest('test_backend_logrotate_file'))

  return s

def backend_cron_conf_ts():
  s = unittest.TestSuite()
  s.addTest(rec.RegressionConfigurationTest('test_backend_cron_file'))

  return s
