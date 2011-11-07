#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.test import service_conf as sc

def backend_server_status_rt(conf, lfn):
  s = unittest.TestSuite()
  s.addTest(sc.RegressionConfigurationTest('test_backend_server_status', conf, lfn))

  return s

def backend_logrotate_conf_rt(conf, lfn):
  s = unittest.TestSuite()
  s.addTest(sc.RegressionConfigurationTest('test_backend_logrotate_file', conf, lfn))

  return s

def backend_cron_conf_rt(conf, lfn):
  s = unittest.TestSuite()
  s.addTest(sc.RegressionConfigurationTest('test_backend_cron_file', conf, lfn))

  return s

def backend_gridhttps_rt(conf, lfn):
  s = unittest.TestSuite()
  s.addTest(sc.RegressionConfigurationTest('test_backend_gridhttps', conf, lfn))

  return s

def yaim_version_file_rt(conf, lfn):
  s = unittest.TestSuite()
  s.addTest(sc.RegressionConfigurationTest('test_yaim_version_file', conf, lfn))

  return s

def gridhttps_plugin_links_rt(conf, lfn):
  s = unittest.TestSuite()
  s.addTest(sc.RegressionConfigurationTest('test_gridhttps_plugin_links', conf, lfn))

  return s

def size_in_namespace_file_rt(conf, lfn):
  s = unittest.TestSuite()
  s.addTest(sc.RegressionConfigurationTest('test_size_in_namespace_file', conf, lfn))

  return s

def mysql_connector_java_links_rt(conf, lfn):
  s = unittest.TestSuite()
  s.addTest(sc.RegressionConfigurationTest('test_mysql_connector_java_links', conf, lfn))

  return s
