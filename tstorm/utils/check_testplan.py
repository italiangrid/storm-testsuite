#!/usr/bin/python

import sys
import os

class CheckTestplan:
    def __init__(self):
        self.key_word = 'test_plan'
        self.test_plan_categories = ['common_tests',
            'basic_tests',
            'regression_tests',
            'regression_tests_novoms',
            'basic_tests_novoms',
            'regression_conftests',
            'regression_ldaptests',
            'tape_tests']
        self.methods = {
            'cksm_ts': 'bt.cksm_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'https_ts': 'btnv.https_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'https_voms_ts': 'bt.https_voms_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ping_ts': 'bt.ping_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'cw_ts': 'bt.cw_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'gtp_ts': 'bt.gtp_ts(tfn,ifn,dfn,back_ifn, uid, lfn)', 
            'eight_digit_string_checksum_ts': 'rt.eight_digit_string_checksum_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'non_ascii_chars_ts': 'rt.non_ascii_chars_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'unsupported_protocols_ts': 'rt.unsupported_protocols_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'dt_ts': 'bt.dt_ts(tfn,ifn,dfn,back_ifn, uid, lfn)', 
            'http_ts': 'btnv.http_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'glue_service_ts': 'rlt.glue_service_ts(tfn, uid, lfn)',
            'gluetwo_storage_share_capacity_ts': 'rlt.gluetwo_storage_share_capacity_ts(tfn, uid, lfn)',
            'glue_available_space_info_service_ts': 'rlt.glue_available_space_info_service_ts(tfn, uid, lfn)',
            'glue_available_space_ts': 'rlt.glue_available_space_ts(tfn, uid, lfn)',
            'glue_used_space_ts': 'rlt.glue_used_space_ts(tfn, uid, lfn)',
            'size_ts': 'rlt.size_ts(tfn, uid, lfn)',
            'info_service_failure_ts': 'rlt.info_service_failure_ts(tfn, uid, lfn)',
            'gluetwo_endpoint_undefined_ts': 'rlt.gluetwo_endpoint_undefined_ts(tfn, uid, lfn)',
            'gluetwo_storage_undefined_ts': 'rlt.gluetwo_storage_undefined_ts(tfn, uid, lfn)',
            'gluetwo_endpoint_ts': 'rlt.gluetwo_endpoint_ts(tfn, uid, lfn)',
            'update_used_space_upon_pd_ts': 'rt.update_used_space_upon_pd_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'update_free_space_upon_rm_ts': 'rt.update_free_space_upon_rm_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'storm_database_password':'rt.storm_database_password_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'storm_gridhttps_authorization_denied':'rt.storm_gridhttps_authorization_denied_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'storm_backend_age_ts': 'rt.storm_backend_age_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'get_space_metadata_failure_ts':'rtnv.get_space_metadata_failure_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'conf_ts': 'cts.conf_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'access_tape_ts': 'tt.access_tape_ts(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'backend_server_status_rt': 'rct.backend_server_status_rt(tfn, uid, lfn)',
            'backend_server_name_status_rt': 'rct.backend_server_name_status_rt(tfn, uid, lfn)',
            'backend_cron_file_rt': 'rct.backend_cron_file_rt(tfn, uid, lfn)',
            'backend_logrotate_file_rt': 'rct.backend_logrotate_file_rt(tfn, uid, lfn)',
            'backend_gridhttps_rt': 'rct.backend_gridhttps_rt(tfn, uid, lfn)',
            'yaim_version_file_rt': 'rct.yaim_version_file_rt(tfn, uid, lfn)',
            'gridhttps_plugin_links_rt': 'rct.gridhttps_plugin_links_rt(tfn, uid, lfn)',
            'size_in_namespace_file_rt': 'rct.size_in_namespace_file_rt(tfn, uid, lfn)',
            'mysql_connector_java_links_rt': 'rct.mysql_connector_java_links_rt(tfn, uid, lfn)',
            'mysql_storage_space_update_rt':'rct.mysql_storage_space_update_rt(tfn, uid, lfn)'
            }   
        self.tests_type = {
            'novoms':['common_tests',
                'basic_tests_novoms',
                'regression_tests_novoms'],
            'voms':['common_tests',
                'basic_tests',
                'regression_tests',
                'tape_tests'],
            'conf':['regression_ldaptests',
                'regression_conftests']
            } 

    def get_key_word(self):
        return self.key_word

    def get_test_plan_categories(self):
        return self.test_plan_categories

    def get_test_suites(self):
        return self.methods.keys()

    def get_methods(self):
        return self.methods

    def get_tests_type(self):
        return self.tests_type
