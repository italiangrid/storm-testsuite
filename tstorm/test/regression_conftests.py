#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.test import service_conf as sc

def backend_server_status_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_server_status', conf, uid, lfn))

    return s

def backend_logrotate_file_rt(conf, id, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_logrotate_file', conf, uid, lfn))

    return s

def backend_cron_file_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_cron_file', conf, uid lfn))

    return s

def backend_gridhttps_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_gridhttps', conf, uid, lfn))

    return s

def yaim_version_file_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_yaim_version_file', conf, uid, lfn))

    return s

def gridhttps_plugin_links_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_gridhttps_plugin_links', conf, uid, lfn))

    return s

def size_in_namespace_file_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_size_in_namespace_file', conf, uid, lfn))

    return s

def mysql_connector_java_links_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_mysql_connector_java_links', conf, uid, lfn))

    return s

def backend_server_name_status_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_server_name_status', conf, uid, lfn))

    return s

def mysql_storage_space_update_rt(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_mysql_storage_space_update', conf, uid, lfn))

    return s
