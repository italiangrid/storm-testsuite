__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment.regression import service_configuration as sc

def ts_backend_server_status(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_server_status', conf, lfn))
    return s

def ts_backend_logrotate_file(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_logrotate_file', conf, lfn))
    return s

def ts_backend_cron_file(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_cron_file', conf, lfn))
    return s

def ts_backend_gridhttps(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_gridhttps', conf, lfn))
    return s

def ts_yaim_version_file(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_yaim_version_file', conf, lfn))
    return s

def ts_gridhttps_plugin_links(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_gridhttps_plugin_links', conf, lfn))
    return s

def ts_size_in_namespace_file(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_size_in_namespace_file', conf, lfn))
    return s

def ts_mysql_connector_java_links(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_mysql_connector_java_links', conf, lfn))
    return s

def ts_backend_server_name_status(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_backend_server_name_status', conf, lfn))
    return s

def ts_mysql_storage_space_update(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_mysql_storage_space_update', conf, lfn))
    return s

def ts_path_authz_db(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_path_authz_db', conf, lfn))
    return s

def ts_storm_backend_service_crashes_on_gpfs(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_storm_backend_service_crashes_on_gpfs', conf, lfn))
    return s

def ts_configuration_folders_permissions(conf, lfn):
    s = unittest.TestSuite()
    s.addTest(sc.RegressionConfigurationTest('test_configuration_folders_permissions', conf, lfn))
    return s
