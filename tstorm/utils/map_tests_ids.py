#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import sys
import os
import simplejson
from tstorm.utils import utils
from tstorm.utils import settings

class MapTestsIds:
    def __init__(self):
        self.atomics_tests = {
            "test_dcache_ping":"",
            "test_storm_ping":"",
            "test_ls_unexist_file":"",
            "test_ls_unexist_dir":"",
            "test_mkdir_dir":"",
            "test_mkdir_exist_dir":"",
            "test_ls_dir":"",
            "test_cp_bt":"",
            "test_ls_file":"",
            "test_cp_at":"",
            "test_rm_file":"",
            "test_rm_unexist_file":"",
            "test_rm_dir":"",
            "test_rm_unexist_dir":""}

        self.functionalities_tests = {
            "test_cksm":"",
            "test_data_transfer_out_file":"",
            "test_data_transfer_out_exist_file":"",
            "test_data_transfer_in_file":"",
            "test_data_transfer_in_unexist_file":""}

        self.regressions_tests = {
            "test_eight_digit_string_checksum":"",
            "test_update_free_space_upon_rm":"",
            "test_update_used_space_upon_pd":"",
            "test_unsupported_protocols":"",
            "test_non_ascii_chars":"",
            "test_storm_backend_age":"",
            "test_get_space_metadata_failure":""}
 
        self.regressions_conf_tests = {
            "test_backend_server_status":"",
            "test_backend_logrotate_file":"",
            "test_backend_cron_file":"",
            "test_backend_gridhttps":"",
            "test_yaim_version_file":"",
            "test_size_in_namespace_file":"",
            "test_gridhttps_plugin_links":"",
            "test_backend_server_name_status":"",
            "test_mysql_storage_space_update":"",
            "test_mysql_connector_java_links":""}

        self.regressions_ldap_tests = {
            "test_glue_service":"",
            "test_gluetwo_storage_share_capacity":"",
            "test_glue_available_space_info_service":"",
            "test_glue_available_space":"",
            "test_glue_used_space":"",
            "test_size":"",
            "test_info_service_failure":"",
            "test_gluetwo_endpoint_undefined":"",
            "test_gluetwo_storage_undefined":"",
            "test_gluetwo_endpoint":""}
 
        self.https_tests = {
            "test_srm_transfer_outbound_http":"",
            "test_direct_transfer_outbound_http":"",
            "test_direct_transfer_outbound_http_exist_file":"",
            "test_direct_transfer_inbound_http":"",
            "test_direct_transfer_inbound_http_unexist_file":"",
            "test_srm_transfer_inbound_http":"",
            "test_srm_transfer_outbound_https":"",
            "test_direct_transfer_outbound_https":"",
            "test_direct_transfer_outbound_https_exist_file":"",
            "test_direct_transfer_inbound_https_no_auth":"",
            "test_direct_transfer_inbound_https_unexist_file":"",
            "test_srm_transfer_inbound_https":"",
            "test_srm_transfer_outbound_https_voms":"",
            "test_direct_transfer_outbound_https_voms":"",
            "test_direct_transfer_outbound_https_voms_exist_file":"",
            "test_direct_transfer_inbound_https_voms":"",
            "test_direct_transfer_inbound_https_voms_no_auth":"",
            "test_direct_transfer_inbound_https_voms_unexist_file":"",
            "test_srm_transfer_inbound_https_voms":""}
 
        self.utilities_tests = {
            "test_settings":"",
            "test_dd":"",
            "test_cr_lf":"",
            "test_rm_lf":""}

        self.categories_tests = [
            'atomics_tests', 'functionalities_tests', 'regressions_tests',
            'regressions_conf_tests', 'regressions_ldap_tests', 'https_tests',
            'utilities_tests'
            ]

    def __get_all_tests(self):
        '''Returns a dictionary containing all categories tests'''

        all_tests = {}
        
        for x in self.categories_tests:
            all_tests.update(eval('self.' + x))
        
        return all_tests

    def __get_tests_ids(self):
        '''Returns a dictionary containing a map between test and id'''

        test_ids = {}

        for x in self.__get_all_tests().keys():
            uuid = utils.get_uuid()
            if len(uuid) > 6:
                test_ids[x] = uuid[:6]
            else:
                test_ids[x] = uuid

        return test_ids

    def __set_map_file_entry(self, map_len, current_index, file_index, key, value):
        '''Set an entry in the map file'''

        if map_len == current_index:
            file_index.write('  "' + key + '":"' + value + '"\n')
        else:
            file_index.write('  "' + key + '":"' + value + '",\n')

    def verify_map_file(self, file_name):
        '''Verifies the corretness of the file in json format'''

        tests_ids_info = {}

        try:
            #tp_info = json.read(open(conffile,'r').read())
            tests_ids_info = simplejson.load(open(file_name,'r'))
        except ValueError, e:
            #dbglog("No stfunc.conf file found or wrong json syntax")
            print "wrong conf file"
            sys.exit(2)
            #raise SystemExit(e) 
        #except (IOError,simplejson.ReadException):
            #dbglog("No stfunc.conf file found or wrong json syntax")
            #print "wrong conf file"
            #sys.exit(2)

        return tests_ids_info
 
    def create_map_file(self):
        '''Creates a json file containing test as key, and id as value'''

        map_tests_ids = self.__get_tests_ids()

        configuration_path = settings.get_configuration_path()
        destination_file=configuration_path + 'map_tests_ids.json'
        df = open(destination_file, 'a')
        df.write('{\n')

        a=0
        for x in map_tests_ids.keys():
            self.__set_map_file_entry(len(map_tests_ids), a+1, df, x, map_tests_ids[x])

        df.write('}\n')
        df.close()

        self.verify_map_file(destination_file)

    def modify_map_file(self):
        '''Modifies a json file containing test as key, and id as value'''

        map_tests_ids = self.__get_tests_ids()

        configuration_path = settings.get_configuration_path()
        source_file = configuration_path + 'map_tests_ids.json'
        source_tests_ids_info = self.verify_map_file(source_file)
        destination_file = configuration_path + 'map_tests_ids.json.tmp'
        df = open(destination_file, 'a')
        df.write('{\n')

        a=0
        for x in map_tests_ids.keys():
            if x in source_tests_ids_info.keys():
                self.__set_map_file_entry(len(map_tests_ids), a+1, df, x, source_tests_ids_info[x])
            else:
                self.__set_map_file_entry(len(map_tests_ids), a+1, df, x, map_tests_ids[x])
            a+=1

        df.write('}\n')
        df.close()

        self.verify_map_file(destination_file)

        os.rename(destination_file, source_file)
