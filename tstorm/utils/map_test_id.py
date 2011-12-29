#!/usr/bin/python

import sys
import os
#import json
import simplejson
from tstorm.utils import utils

class MapTestId:
    def __init__(self):
        self.atomics_test = {
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

        self.functionalities_test = {
            "test_cksm":"",
            "test_data_transfer_out_file":"",
            "test_data_transfer_out_exist_file":"",
            "test_data_transfer_in_file":"",
            "test_data_transfer_in_unexist_file":""}

        self.regression_test = {
            "test_eight_digit_string_checksum":"",
            "test_update_free_space_upon_rm":"",
            "test_update_used_space_upon_pd":"",
            "test_unsupported_protocols":"",
            "test_non_ascii_chars":"",
            "test_storm_backend_age":"",
            "test_get_space_metadata_failure":""}
 
        self.regression_conf_test = {
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

        self.regression_ldap_test = {
            "test_gluetwo_service":"",
            "test_gluetwo_storage_share_capacity":"",
            "test_glue_available_space_info_service":"",
            "test_glue_available_space":"",
            "test_glue_used_space":"",
            "test_size":"",
            "test_info_service_failure":"",
            "test_gluetwo_endpoint_undefined":"",
            "test_gluetwo_storage_undefined":"",
            "test_gluetwo_endpoint":""}
 
        self.https_test = {
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
 
        self.utilities_test = {
            "test_settings":"",
            "test_dd":"",
            "test_cr_lf":"",
            "test_rm_lf":""}

    def get_test_id(self):
        test_id = {}
        for x in self.atomics_test.keys():
            test_id[x] = utils.get_uuid()
        for x in self.functionalities_test.keys():
            test_id[x] = utils.get_uuid()
        for x in self.regression_test.keys():
            test_id[x] = utils.get_uuid()
        for x in self.regression_conf_test.keys():
            test_id[x] = utils.get_uuid()
        for x in self.regression_ldap_test.keys():
            test_id[x] = utils.get_uuid()
        for x in self.https_test.keys():
            test_id[x] = utils.get_uuid()
        for x in self.utilities_test.keys():
            test_id[x] = utils.get_uuid()
        return test_id

    def create_map_test_id(self):
        map_test_id = self.get_test_id()

        dirname=os.path.dirname(sys.argv[0])
        configpath = os.path.join(dirname, "../", ".")
        conffile=configpath+'./etc/tstorm/map_test_id.json'
        sf = open(conffile, 'a')
        sf.write('{\n')

        a=0
        for x in map_test_id.keys():
            if len(map_test_id) == a+1:
                sf.write('  "' + x + '":"' + map_test_id[x][:6] + '"\n')
            else:
                sf.write('  "' + x + '":"' + map_test_id[x][:6] + '",\n')
            a+=1
        sf.write('}\n')
        sf.close()

        try:
            #tp_info=json.read(open(conffile,'r').read())
            tp_info=simplejson.load(open(conffile,'r'))
        except ValueError, e:
            #dbglog("No stfunc.conf file found or wrong json syntax")
            print "wrong conf file"
            sys.exit(2)
            #raise SystemExit(e) 
        #except (IOError,simplejson.ReadException):
            #dbglog("No stfunc.conf file found or wrong json syntax")
            #print "wrong conf file"
            #sys.exit(2)
