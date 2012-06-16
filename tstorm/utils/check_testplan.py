import sys
import os

class CheckTestplan:
    def __init__(self):
        self.key_word = 'test_plan'
        self.test_plan_categories = ['common_tests',
            'atomic_tests',
            'functional_tests',
            'regression_tests',
            'regression_tests_novoms',
            'functional_tests_novoms',
            'regression_conftests',
            'regression_ldaptests',
            'tape_tests']
        self.methods = {
            'ts_ping': 'at.ts_ping(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_ping_wo': 'at.ts_ping_wo(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_gtp': 'at.ts_gtp(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_gtp_wo': 'at.ts_gtp_wo(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_ls_unexist_file': 'at.ts_ls_unexist_file(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_mkdir': 'at.ts_mkdir(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_mkdir_exist': 'at.ts_mkdir_exist(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_ls_dir': 'at.ts_ls_dir(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_cp_out': 'at.ts_cp_out(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_ls_file': 'at.ts_ls_file(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_rm_file': 'at.ts_rm_file(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_rm_unexist_dir': 'at.ts_rm_unexist_dir(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_cp_in': 'at.ts_cp_in(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_cksm': 'ft.ts_cksm(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_https': 'ftnv.ts_https(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_https_voms': 'ft.ts_https_voms(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_cw': 'ft.ts_cw(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_eight_digit_string_checksum': 'rt.ts_eight_digit_string_checksum(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_non_ascii_chars': 'rt.ts_non_ascii_charss(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_unsupported_protocols': 'rt.ts_unsupported_protocols(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_dt': 'ft.ts_dt(tfn,ifn,dfn,back_ifn, uid, lfn)', 
            'ts_http': 'ftnv.ts_http(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_update_used_space_upon_pd': 'rt.ts_update_used_space_upon_pd(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_update_free_space_upon_rm': 'rt.ts_update_free_space_upon_rm(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_storm_database_password':'rt.ts_storm_database_password(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_storm_gridhttps_authorization_denied':'rt.ts_storm_gridhttps_authorization_denied(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_storm_backend_age': 'rt.ts_storm_backend_age(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_get_space_metadata_failure':'rtnv.ts_get_space_metadata_failure(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_conf': 'cts.ts_conf(tfn,ifn,dfn,back_ifn, uid, lfn)',
            'ts_access_tape': 'tt.ts_access_tape(tfn,ifn,dfn,back_ifn, uid, lfn)',

            'ts_glue_service': 'rlt.ts_glue_service(tfn, uid, lfn)',
            'ts_gluetwo_storage_share_capacity': 'rlt.ts_gluetwo_storage_share_capacity(tfn, uid, lfn)',
            'ts_glue_available_space_info_service': 'rlt.ts_glue_available_space_info_service(tfn, uid, lfn)',
            'ts_glue_available_space': 'rlt.ts_glue_available_space(tfn, uid, lfn)',
            'ts_glue_used_space': 'rlt.ts_glue_used_space(tfn, uid, lfn)',
            'ts_size': 'rlt.ts_size(tfn, uid, lfn)',
            'ts_info_service_failure': 'rlt.ts_info_service_failure(tfn, uid, lfn)',
            'ts_gluetwo_endpoint_undefined': 'rlt.ts_gluetwo_endpoint_undefined(tfn, uid, lfn)',
            'ts_gluetwo_storage_undefined': 'rlt.ts_gluetwo_storage_undefined(tfn, uid, lfn)',
            'ts_gluetwo_endpoint': 'rlt.ts_gluetwo_endpoint(tfn, uid, lfn)',

            'ts_backend_server_status': 'rct.ts_backend_server_status(tfn, uid, lfn)',
            'ts_backend_server_name_status': 'rct.ts_backend_server_name_status(tfn, uid, lfn)',
            'ts_backend_cron_file': 'rct.ts_backend_cron_file(tfn, uid, lfn)',
            'ts_backend_logrotate_file': 'rct.ts_backend_logrotate_file(tfn, uid, lfn)',
            'ts_backend_gridhttps': 'rct.ts_backend_gridhttps(tfn, uid, lfn)',
            'ts_yaim_version_file': 'rct.ts_yaim_version_file(tfn, uid, lfn)',
            'ts_gridhttps_plugin_links': 'rct.ts_gridhttps_plugin_links(tfn, uid, lfn)',
            'ts_size_in_namespace_file': 'rct.ts_size_in_namespace_file(tfn, uid, lfn)',
            'ts_mysql_connector_java_links': 'rct.ts_mysql_connector_java_links(tfn, uid, lfn)',
            'ts_mysql_storage_space_update':'rct.ts_mysql_storage_space_update(tfn, uid, lfn)'
            }   
        self.tests_type = {
            'novoms':['common_tests',
                'functional_tests_novoms',
                'regression_tests_novoms'],
            'voms':['common_tests',
                'atomic_tests',
                'functional_tests',
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
