__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment.regression import service_configuration as sc

def ts_backend_server_status(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_backend_server_status'][6])
    lfn.put_description(uid['ts_backend_server_status'][7])
    lfn.put_uuid(uid['ts_backend_server_status'][0])
    lfn.put_ruid(uid['ts_backend_server_status'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_backend_server_status', conf, lfn))

    return s

def ts_backend_logrotate_file(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_backend_logrotate_file'][6])
    lfn.put_description(uid['ts_backend_logrotate_file'][7])
    lfn.put_uuid(uid['ts_backend_logrotate_file'][0])
    lfn.put_ruid(uid['ts_backend_logrotate_file'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_backend_logrotate_file', conf, lfn))

    return s

def ts_backend_cron_file(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_backend_cron_file'][6])
    lfn.put_description(uid['ts_backend_cron_file'][7])
    lfn.put_uuid(uid['ts_backend_cron_file'][0])
    lfn.put_ruid(uid['ts_backend_cron_file'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_backend_cron_file', conf, lfn))

    return s

def ts_backend_gridhttps(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_backend_gridhttps'][6])
    lfn.put_description(uid['ts_backend_gridhttps'][7])
    lfn.put_uuid(uid['ts_backend_gridhttps'][0])
    lfn.put_ruid(uid['ts_backend_gridhttps'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_backend_gridhttps', conf, lfn))

    return s

def ts_yaim_version_file(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_yaim_version_file'][6])
    lfn.put_description(uid['ts_yaim_version_file'][7])
    lfn.put_uuid(uid['ts_yaim_version_file'][0])
    lfn.put_ruid(uid['ts_yaim_version_file'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_yaim_version_file', conf, lfn))

    return s

def ts_gridhttps_plugin_links(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_gridhttps_plugin_links'][6])
    lfn.put_description(uid['ts_gridhttps_plugin_links'][7])
    lfn.put_uuid(uid['ts_gridhttps_plugin_links'][0])
    lfn.put_ruid(uid['ts_gridhttps_plugin_links'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_gridhttps_plugin_links', conf, lfn))

    return s

def ts_size_in_namespace_file(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_size_in_namespace_file'][6])
    lfn.put_description(uid['ts_size_in_namespace_file'][7])
    lfn.put_uuid(uid['ts_size_in_namespace_file'][0])
    lfn.put_ruid(uid['ts_size_in_namespace_file'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_size_in_namespace_file', conf, lfn))

    return s

def ts_mysql_connector_java_links(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_mysql_connector_java_links'][6])
    lfn.put_description(uid['ts_mysql_connector_java_links'][7])
    lfn.put_uuid(uid['ts_mysql_connector_java_links'][0])
    lfn.put_ruid(uid['ts_mysql_connector_java_links'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_mysql_connector_java_links', conf, lfn))

    return s

def ts_backend_server_name_status(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_backend_server_name_status'][6])
    lfn.put_description(uid['ts_backend_server_name_status'][7])
    lfn.put_uuid(uid['ts_backend_server_name_status'][0])
    lfn.put_ruid(uid['ts_backend_server_name_status'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_backend_server_name_status', conf, lfn))

    return s

def ts_mysql_storage_space_update(conf, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_mysql_storage_space_update'][6])
    lfn.put_description(uid['ts_mysql_storage_space_update'][7])
    lfn.put_uuid(uid['ts_mysql_storage_space_update'][0])
    lfn.put_ruid(uid['ts_mysql_storage_space_update'][3])
    lfn.put_output()
    s.addTest(sc.RegressionConfigurationTest('test_mysql_storage_space_update', conf, lfn))

    return s
