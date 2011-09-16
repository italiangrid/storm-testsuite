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

def backend_gridhttps_ts():
  s = unittest.TestSuite()
  s.addTest(rec.RegressionConfigurationTest('test_backend_gridhttps'))

  return s

def yaim_version_file_ts():
  s = unittest.TestSuite()
  s.addTest(rec.RegressionConfigurationTest('test_yaim_version_file'))

  return s

def gridhttps_plugin_links_ts():
  s = unittest.TestSuite()
  s.addTest(rec.RegressionConfigurationTest('test_gridhttps_plugin_links'))

  return s

def size_in_namespace_file_ts():
  s = unittest.TestSuite()
  s.addTest(rec.RegressionConfigurationTest('test_size_in_namespace_file'))

  return s
