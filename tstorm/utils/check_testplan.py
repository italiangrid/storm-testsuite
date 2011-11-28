import sys
import os

class CheckTestplan:
    def __init__(self):
      self.key_word = 'test_plan'
      self.test_plan_categories = ['common_tests',
                                  'basic_tests',
                                  'regression_tests',
                                  'basic_tests_novoms',
                                  'regression_conftests',
                                  'regression_ldaptests',
                                  'tape_tests']
      self.methods = {
                     'cksm_ts': 'bt.cksm_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'https_ts': 'btnv.https_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'https_voms_ts': 'bt.https_voms_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'cs_ts': 'bt.cs_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'cw_ts': 'bt.cw_ts(tfn,ifn,dfn,back_ifn, lfn)', 
                     'eight_digit_string_checksum_ts': 'rt.eight_digit_string_checksum_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'non_ascii_chars_ts': 'rt.non_ascii_chars_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'unsupported_protocols_ts': 'rt.unsupported_protocols_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'dt_ts': 'bt.dt_ts(tfn,ifn,dfn,back_ifn, lfn)', 
                     'http_ts': 'btnv.http_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'glue_info_ts': 'rlt.glue_info_ts(tfn, lfn)',
                     'glue_storage_share_capacity_ts': 'rlt.glue_storage_share_capacity_ts(tfn, lfn)',
                     'glue_available_space_info_service_ts': 'rlt.glue_available_space_info_service_ts(tfn, lfn)',
                     'glue_available_space_ts': 'rlt.glue_available_space_ts(tfn, lfn)',
                     'glue_used_space_ts': 'rlt.glue_used_space_ts(tfn, lfn)',
                     'size_ts': 'rlt.size_ts(tfn, lfn)',
                     'update_used_space_upon_pd_ts': 'rt.update_used_space_upon_pd_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'update_free_space_upon_rm_ts': 'rt.update_free_space_upon_rm_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'storm_backend_age_ts': 'rt.storm_backend_age_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'conf_ts': 'cts.conf_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'access_tape_ts': 'tt.access_tape_ts(tfn,ifn,dfn,back_ifn, lfn)',
                     'backend_server_status_rt': 'rct.backend_server_status_rt(tfn, lfn)',
                     'backend_cron_conf_rt': 'rct.backend_cron_conf_rt(tfn, lfn)',
                     'backend_logrotate_conf_rt': 'rct.backend_logrotate_conf_rt(tfn, lfn)',
                     'backend_gridhttps_rt': 'rct.backend_gridhttps_rt(tfn, lfn)',
                     'yaim_version_file_rt': 'rct.yaim_version_file_rt(tfn, lfn)',
                     'gridhttps_plugin_links_rt': 'rct.gridhttps_plugin_links_rt(tfn, lfn)',
                     'size_in_namespace_file_rt': 'rct.size_in_namespace_file_rt(tfn, lfn)',
                     'mysql_connector_java_links_rt': 'rct.mysql_connector_java_links_rt(tfn, lfn)'
                     }   
      self.tests_type = {
                        'novoms':['common_tests',
                                  'basic_tests_novoms',
                                  'regression_ldaptests'],
                        'voms':['common_tests',
                                'basic_tests',
                                'regression_tests',
                                 'regression_ldaptests',
                                 'tape_tests'],
                        'conf':['regression_conftests',
                                'regression_ldaptests']
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
