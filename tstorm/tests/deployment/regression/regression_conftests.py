__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment.regression import service_configuration as sc

def ts_backend_server_status(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_server_status', conf, uid, lfn))

    return s

def ts_backend_logrotate_file(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_logrotate_file', conf, uid, lfn))

    return s

def ts_backend_cron_file(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_cron_file', conf, uid, lfn))

    return s

def ts_backend_gridhttps(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_gridhttps', conf, uid, lfn))

    return s

def ts_yaim_version_file(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_yaim_version_file', conf, uid, lfn))

    return s

def ts_gridhttps_plugin_links(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_gridhttps_plugin_links', conf, uid, lfn))

    return s

def ts_size_in_namespace_file(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_size_in_namespace_file', conf, uid, lfn))

    return s

def ts_mysql_connector_java_links(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_mysql_connector_java_links', conf, uid, lfn))

    return s

def ts_backend_server_name_status(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_server_name_status', conf, uid, lfn))

    return s

def ts_mysql_storage_space_update(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_mysql_storage_space_update', conf, uid, lfn))

    return s
