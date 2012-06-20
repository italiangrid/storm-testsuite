__author__ = 'Elisabetta Ronchieri'

import sys
import os
import simplejson
from tstorm.utils import utils
from tstorm.utils import settings

class MapTestsIds:
    def __init__(self):
        self.atomics_tests = {
            "test_dcache_ping":['2076cb',
                False,'',
                'SRM PING',
                'Verify ping operation'],
            "test_storm_ping":['6d06c2',
                False,'',
                'SRM PING',
                'Verify ping operation'],
            "test_storm_ping_wo":['2c2f66',
                False,'',
                'SRM PING',
                'Verify ping operation with wrong option'],
            "test_storm_gtp":['882900',
                False,'',
                'SRM GET TRANSFER PROTOCOLS',
                'Verify gtp operation'],
            "test_storm_gtp_wo":['6d69e7',
                False,'',
                'SRM GET TRANSFER PROTOCOLS',
                'Verify gtp operation with wrong option'],
            "test_ls_unexist_file":['469b32',
                False,'',
                'SRM LS',
                'Verify ls operation on a file that does not exist'],
            "test_ls_unexist_dir":['4a153e',
                False,'',
                'SRM LS',
                'Verify ls operation on a directory that does not exist'],
            "test_mkdir_dir":['d55993',
                False,'',
                'SRM MKDIR',
                'Verify mkdir operation on a directory'],
            "test_mkdir_exist_dir":['74a033',
                False,'',
                'SRM MKDIR',
                'Verify mkdir operation on a directory that already exists'],
            "test_ls_dir":['0837ae',
                False,'',
                'SRM LS',
                'Verify ls operation on a directory that exists'],
            "test_cp_bt":['037104',
                False,'',
                'SRM CP',
                'Verify cp operation of a given file on a given storage'],
            "test_ls_file":['3d6062',
                False,'',
                'SRM LS',
                'Verify ls operation on a file that exists'],
            "test_cp_at":['a61b97',
                False,'',
                'SRM CP',
                'Verify cp operation of a given file locally'],
            "test_rm_file":['44d230',
                False,'',
                'SRM RM',
                'Verify rm operation of a given file'],
            "test_rm_unexist_file":['b76fcf',
                False,'',
                'SRM RM',
                'Verify rm operation of a file that does not exist'],
            "test_rm_dir":['2d8030',
                False,'',
                'SRM RMDIR',
                'Verify rmdir operation of a given directory'],
            "test_rm_unexist_dir":['5333af',
                False,'',
                'SRM RMDIR',
                'Verify rmdir operation of a directory that does not exist'],
            "ts_ping":['c50037',
                True,'',
                'SRM PING',
                'Verify ping operation',
                'at.ts_ping(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_ping_wo":['b91203',
                True,'',
                'SRM PING',
                'Verify ping operation with wrong option',
                'at.ts_ping_wo(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_gtp":['5eb930',
                True,'',
                'SRM GET TRANSFER PROTOCOLS',
                'Verify gtp operation',
                'at.ts_gtp(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_gtp_wo":['79a112',
                True,'',
                'SRM GET TRANSFER PROTOCOLS',
                'Verify gtp operation',
                'at.ts_gtp_wo(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_ls_unexist_file":['ec478e',
                True,'',
                'SRM LS',
                'Verify ls operation on a file that does not exist',
                'at.ts_ls_unexist_file(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_mkdir":['8c5821',
                False,'',
                'SRM MKDIR',
                'Verify mkdir operation on a directory',
                'at.ts_mkdir(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_mkdir_exist":['8ba9b4',
                False,'',
                'SRM MKDIR',
                'Verify mkdir operation on a directory that already exists',
                'at.ts_mkdir_exist(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_ls_dir":['068ab0',
                False,'',
                'SRM LS',
                'Verify ls operation on a directory that exists',
                'at.ts_ls_dir(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_cp_out":['2a7bc0',
                False,'',
                'SRM CP',
                'Verify cp operation of a given file on a given storage',
                'at.ts_cp_out(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_ls_file":['184ab3',
                False,'',
                'SRM LS',
                'Verify ls operation on a file that exists',
                'at.ts_ls_file(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_rm_file":['b266f2',
                False,'',
                'SRM RM',
                'Verify rm operation of a given file',
                'at.ts_rm_file(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_rm_unexist_dir":['f1efe5',
                False,'',
                'SRM RMDIR',
                'Verify rmdir operation of a directory that does not exist',
                'at.ts_rm_unexist_dir(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_cp_in":['44cf98',
                False,'',
                'SRM CP',
                'TO BE DESCRIBED',
                'at.ts_cp_in(tfn,ifn,dfn,back_ifn, uid, lfn)']}

        self.functionalities_tests = {
            "test_cksm":['eea4be',
                False,'',
                'CKSUM',
                'Verify that the checksum is calculated for the transferred ' +
                'file using the gsiftp protocol'],
            "test_data_transfer_out_file":['4d0ea9',
                False,'',
                'DATA TRANSFER OUT',
                'Verify that the file has been transferred'],
            "test_data_transfer_out_exist_file":['75afce',
                False,'',
                'DATA TRANSFER OUT',
                'Verify that the file has not been transferred because it ' +
                'already exists'],
            "test_data_transfer_in_file":['9011fd',
                False,'',
                'DATA TRANSFER IN',
                'Verify that the file has been transferred back'],
            "test_data_transfer_in_unexist_file":['8e34f5',
                False,'',
                'DATA TRANSFER IN',
                'Verify that the file has not been transferred back because ' +
                'it does not exit'],
            "test_srm_transfer_outbound_https_voms":['aea1bc',
                False,'',
                'SRM TRANSFER OUTBOUND HTTPS',
                'Verify that the file has been transferred back by using ' +
                'https with voms'],
            "test_direct_transfer_outbound_https_voms":['21d919',
                False,'',
                'DIRECT TRANSFER OUTBOUND HTTPS',
                'Verify that the file has been transferred by using https ' +
                'with voms'],
            "test_direct_transfer_outbound_https_voms_exist_file":['8b5ba0',
                False,'',
                'DIRECT TRANSFER OUTBOUND HTTPS',
                'Verify that the file has been transferred by using https ' +
                'with voms when file exists'],
            "test_direct_transfer_inbound_https_voms":['ab1064',
                False,'',
                'DIRECT TRANSFER INBOUND HTTPS',
                'Verify that the file has been transferred back by using ' +
                'https with voms'],
            "test_direct_transfer_inbound_https_voms_no_auth":['d60cc0',
                False,'',
                'DIRECT TRANSFER INBOUND HTTPS',
                'Verify that the file has been transferred back by using ' +
                'https with voms without authorization'],
            "test_direct_transfer_inbound_https_voms_unexist_file":['bd37f7',
                False,'',
                'DIRECT TRANSFER INBOUND HTTPS',
                'Verify that the file has been transferred back by using ' +
                'https with voms when file does not exist'],
            "test_srm_transfer_inbound_https_voms":['e94e78',
                False,'',
                'SRM TRANSFER INBOUND HTTPS',
                'Verify that the file has been transferred back by using ' +
                'https with voms'],
            "ts_cksm":['b8ff21',
                False,'',
                'CKSUM',
                'Verify that the checksum is calculated for the transferred ' +
                'file using the gsiftp protocol',
                'ft.ts_cksm(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_dt":['cda37a',
                False,'',
                'DATA TRANSDER OUT IN USING GSIFTP',
                'Verify that a given file can be transferred out and in',
                'ft.ts_dt(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_https_voms":['c976b0',
                False,'',
                'DATA TRANSDER OUT IN USING HTTPS',
                'Verify that a given file can be transferred out and in',
                'ft.ts_https_voms(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_cw":['e4a8c7',
                False,'',
                'SRM OPERATIONS',
                'Verify that a given file can be transferred out and in',
                'ft.ts_cw(tfn,ifn,dfn,back_ifn, uid, lfn)']}

        self.functionalities_no_voms_tests = {
            "test_srm_transfer_outbound_http":['4244ec',
                False,'',
                'SRM TRANSFER OUTBOUND HTTP',
                'Verify that the file has been transferred by using the ' +
                'http protocol'],
            "test_direct_transfer_outbound_http":['6967f9',
                False,'',
                'DIRECT TRANSFER OUTBOUND HTTP',
                'Verify that the file has been transferred by using http'],
            "test_direct_transfer_outbound_http_exist_file":['45880a',
                False,'',
                'DIRECT TRANSFER OUTBOUND HTTP',
                'Verify that the file has been transferred by using http ' +
                'when file exists'],
            "test_direct_transfer_inbound_http":['fd0f95',
                False,'',
                'DIRECT TRANSFER INBOUND HTTP',
                'Verify that the file has been transferred back by using ' +
                'http'],
            "test_direct_transfer_inbound_http_unexist_file":['b2fd90',
                False,'',
                'DIRECT TRANSFER INBOUND HTTP',
                'Verify that the file has not been transferred back by using ' +
                'http, when file does not exist'],
            "test_srm_transfer_inbound_http":['39612c',
                False,'',
                'SRM TRANSFER INBOUND HTTP',
                'Verify that the file has been transferred back by using ' +
                'http'],
            "test_srm_transfer_outbound_https":['bbddf2',
                False,'',
                'SRM TRANSFER OUTBOUND HTTPS',
                'Verify that the file has been transferred by using https'],
            "test_direct_transfer_outbound_https":['f92c33',
                False,'',
                'DIRECT TRANSFER OUTBOUND HTTPS',
                'Verify that the file has been transferred by using https'],
            "test_direct_transfer_outbound_https_exist_file":['d9d057',
                False,'',
                'DIRECT TRANSFER OUTBOUND HTTPS',
                'Verify that the file has been transferred by using https ' +
                'when the file exists'],
            "test_direct_transfer_inbound_https_no_auth":['6db50f',
                False,'',
                'DIRECT TRANSFER INBOUND HTTPS',
                'Verify that the file has been transferred back by using ' +
                'https without authorization'],
            "test_direct_transfer_inbound_https_unexist_file":['acea33',
                False,'',
                'DIRECT TRANSFER INBOUND HTTPS',
                'Verify that the file has been transferred back by using ' +
                'https when file does not exist'],
            "test_srm_transfer_inbound_https":['47d6d5',
                False,'',
                'SRM TRANSFER INBOUND HTTPS',
                'Verify that the file has been transferred back by using ' +
                'https'],
            "ts_http":['32429c',
                False,'',
                'DATA TRANSFER USING HTTP',
                'Verify transferring operation without voms',
                'ftnv.ts_http(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_https":['4188c4',
                False,'',
                'DATA TRANSFER USING HTTPS',
                'Verify transferring operation without voms',
                'ftnv.ts_https(tfn,ifn,dfn,back_ifn, uid, lfn)']}

        self.regressions_tests = {
            "test_eight_digit_string_checksum":['244fca',
                False,'',
                'COMPARISON BUG IN LCG-CR COPYING TO STORM',
                'The StoRM GridFTP component stores the checksum value ' +
                'computed during the file transfer as a long number, ' +
                'discarding in this way leading zeroes. The default ADLER32 ' +
                'checksum match algorithm considers checksum values as ' +
                'strings so the leading zeroes matters'],
            "test_update_free_space_upon_rm":['b9aa3c',
                False,'',
                'INCORRECT INFORMATION PUBLISHED BY STORM',
                'StoRM does not publish correctly values for used and free ' +
                'space on the  BDII due to a bug in the update of the free ' + 
                'space after the the srmRm operation'],
            "test_update_used_space_upon_pd":['b740fb',
                False,'',
                'STORM BUG: SPACE TOKEN USED SPACE IS NOT UPDATE',
                'StoRM does not provides updated used space value for Space ' +
                'Token due to a bug in the update of the used space after ' +
                'the srmPutDone operation'],
            "test_unsupported_protocols":['b0ca16',
                False,'',
                'STORM BUG: SRM TRANSFER COMMANDS DOES NOT REPORT ERRONEOUS ' +
                'PROTOCOL REQUESTS',
                'StoRM does not returns SRM_NOT_SUPPORTED error code when ' +  
                'file transfer operation (srmPrepareToPut,srmPrepareToGet,' +
                'srmBringOnline) are called providing a list of not ' +
                'supported desired transfer protocols to a bug in the ' +  
                'management of file transfer operation. StoRM does not ' +
                'verifies if the provided protocols are supported'],
            "test_both_sup_and_unsup_protocols":['',
                False,'',
                'STORM FRONTEND PRODUCES HUGE LOG FILE WHEN MANAGING ' +
                'REQUESTS THAT CONTAIN SUPPORTED PROTOCOLS',
                'StoRM produced huge log file when file transfer ' +
                'operation (srmPrepareToPut,srmPrepareToGet,' +
                'srmBringOnline) are called with a list of desired ' +
                'transfered protocols'],
            "test_non_ascii_chars":['09829e',
                False,'',
                'STORM BUG: REQUEST WITH AUTHORIZATION ID PARAMETERS WITH ' +
                'NON ASCII CHARACTERS MAKES FE CRASH',
                'StoRM Frontend crashes when managing asynchronous requests ' +
                'providing string parameters containing non ASCII characters'],
            "test_storm_backend_age":['b76e61',
                False,'',
                'WRONG STORM BACKEND AGE RETURNED BY SRM PING',
                'Wrong the StoRM backend age returned by the command srm ' +
                'ping'],
            "test_storm_database_password":['0b20a0',
                False,'',
                'ERROR IN LOADING DATABASE PASSWORD',
                'StoRM Backend Server does not load database password ' +
                'correctly when its values is not the default one'],
            "test_storm_gridhttps_authorization_denied":['d58db9',
                False,'',
                'AUTHORIZATION REST SERVICE DENY AUTHORIZATION',
                'StoRM Backend Gridhttps does not work if the SA ' +
                'accesspoint is not included in the SA root path'],
            "test_storm_backend_dao_null_pointer":['',
                False,'',
                'TO DO',
                'TO BE SPECIFIED'],
            "ts_update_free_space_upon_rm":['341355',
                False,'',
                'INCORRECT INFORMATION PUBLISHED BY STORM',
                'StoRM does not publish correctly values for used and free ' +
                'space on the  BDII due to a bug in the update of the free ' +
                'space after the the srmRm operation',
                'rt.ts_update_free_space_upon_rm(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_eight_digit_string_checksum":['5cd728',
                False,'',
                'COMPARISON BUG IN LCG-CR COPYING TO STORM',
                'The StoRM GridFTP component stores the checksum value ' +
                'computed during the file transfer as a long number, ' +
                'discarding in this way leading zeroes. The default ADLER32 ' +
                'checksum match algorithm considers checksum values as ' +
                'strings so the leading zeroes matters',
                'rt.ts_eight_digit_string_checksum(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_update_used_space_upon_pd":['c971fb',
                False,'',
                'STORM BUG: SPACE TOKEN USED SPACE IS NOT UPDATE',
                'StoRM does not provides updated used space value for Space ' +
                'Token due to a bug in the update of the used space after ' +
                'the srmPutDone operation',
                'rt.ts_update_used_space_upon_pd(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_unsupported_protocols":['5a9532',
                False,'',
                'STORM BUG: SRM TRANSFER COMMANDS DOES NOT REPORT ERRONEOUS ' +
                'PROTOCOL REQUESTS',
                'StoRM does not returns SRM_NOT_SUPPORTED error code when ' +
                'file transfer operation (srmPrepareToPut,srmPrepareToGet,' +
                'srmBringOnline) are called providing a list of not ' +
                'supported desired transfer protocols to a bug in the ' +
                'management of file transfer operation. StoRM does not ' +
                'verifies if the provided protocols are supported',
                'rt.ts_unsupported_protocols(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_both_sup_and_unsup_protocols":['',
                False,'',
                'STORM FRONTEND PRODUCES HUGE LOG FILE WHEN MANAGING ' +
                'REQUESTS THAT CONTAIN SUPPORTED PROTOCOLS',
                'StoRM produced huge log file when file transfer ' +
                'operation (srmPrepareToPut,srmPrepareToGet,' +
                'srmBringOnline) are called with a list of desired ' +
                'transfered protocols',
                ''],
            "ts_non_ascii_chars":['2f6fe9',
                False,'',
                'STORM BUG: REQUEST WITH AUTHORIZATION ID PARAMETERS WITH ' +
                'NON ASCII CHARACTERS MAKES FE CRASH',
                'StoRM Frontend crashes when managing asynchronous requests ' +
                'providing string parameters containing non ASCII characters',
                'rt.ts_non_ascii_chars(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_storm_backend_age":['915129',
                False,'',
                'WRONG STORM BACKEND AGE RETURNED BY SRM PING',
                'Wrong the StoRM backend age returned by the command srm ' +
                'ping',
                'rt.ts_storm_backend_age(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_storm_database_password":['402816',
                False,'',
                'ERROR IN LOADING DATABASE PASSWORD',
                'StoRM Backend Server does not load database password ' +
                'correctly when its values is not the default one',
                'rt.ts_storm_database_password(tfn,ifn,dfn,back_ifn, uid, lfn)'],
            "ts_storm_gridhttps_authorization_denied":['221160',
                False,'',
                'AUTHORIZATION REST SERVICE DENY AUTHORIZATION',
                'StoRM Backend Gridhttps does not work if the SA ' +
                'accesspoint is not included in the SA root path',
                'rt.ts_storm_gridhttps_authorization_denied(tfn,ifn,dfn,back_ifn, uid, lfn)']
            }

        self.regressions_no_voms_tests = {
            "test_get_space_metadata_failure":['6e21ed',
                False,'',
                'GET SPACE METADATA FAILURE WITHOUT VOMS EXTENSIONS',
                'StoRM Backend Server returns an exception when it receives ' +
                'a GetSpaceMetadata request without voms extension'],
            "ts_get_space_metadata_failure":['',
                False,'',
                'GET SPACE METADATA FAILURE WITHOUT VOMS EXTENSIONS',
                'StoRM Backend Server returns an exception when it receives ' +
                'a GetSpaceMetadata request without voms extension',
                'rtnv.ts_get_space_metadata_failure(tfn,ifn,dfn,back_ifn, uid, lfn)']
            }
 
        self.regressions_conf_tests = {
            "test_backend_server_status":['1fee07',
                False,'',
                'EXTRA STORM BACKEND SERVICE INFORMATION RETURNED DURING THE ' +
                'EXECUTION OF STATUS',
                'Extra information are returned by storm backend server init ' +
                'script during the execution of status'],
            "test_backend_logrotate_file":['ad63ac',
                False,'',
                'STORN BACKEND LOGROTATE FILE POINTS TO NON EXISTING FILE',
                'StoRM Backend logrotate file points to non existing file'],
            "test_backend_cron_file":['71272d',
                False,'',
                'STORM BACKEND DOES NOT ROTATE LOG FILES',
                'StoRM Backend does not rotate log files'],
            "test_backend_gridhttps":['09a5b7',
                False,'',
                'DEFAULT GRIDHTTPS SERVER PORT NUMBER CONFLICTS WITH BACKEND ' +
                'DEFAULT XMLRPC PORT NUMBER',
                'Default GridHTTPs server port number conflicts with Backend ' +
                'default xmlrpc port number'],
            "test_yaim_version_file":['b57772',
                False,'',
                'WRONG VERSION IN THE YAIM-VERSION FILE',
                'Wrong version in the yaim-storm file'],
            "test_size_in_namespace_file":['c23e05',
                False,'',
                'WRONG SETTINGS OF SIZE IN NAMESPACE.XML',
                'Wrong settings of size in namespace.xml'],
            "test_gridhttps_plugin_links":['84e55b',
                False,'',
                'REMOVED GRIDHTTPS PLUGIN LINKS DURING UPGRADE FROM 1.7.0 to ' +
                '1.7.1',
                'Removed gridhttpds plugin links during upgrade from 1.7.0 to ' +
                '1.7.1'],
            "test_backend_server_name_status":['e055f5',
                False,'',
                'WRONG STORM BACKEND SERVER NAME RETURNED DURING THE ' +
                'EXECUTION OF STATUS',
                'StoRM Backend Server name is wrong'],
            "test_mysql_storage_space_update":['efacfe',
                False,'',
                'NO UPDATING OF STORAGE SPACE IN DB AFTER A TOTAL ONLINE ' + 
                'SIZE CHANGE IN THE NAMESPACE.XML',
                'When the TotalOnlineSize value has changed in the ' +
                'namespace.xml, the storm-backend-server process does not ' +
                'update the  corrispondent field in the storage_space table ' +
                'of the storm_be_ISAM  database'],
            "test_mysql_connector_java_links":['ad7c8b',
                False,'',
                'MYSQL-CONNECTOR-JAVA DOWNLOADING FAILURE',
                'mysql-connector-java is not downloaded due to an issue in ' +
                'its owner repository'],
            "test_frontend_logrotate_output":['74d14a',
                False,'',
                'TO DO',
                'TO .. DO'],
            "test_backend_logrotate_output":['3ef792',
                False,'',
                'TO DO',
                'TO ..  DO'],
            "test_backend_restart_failure":['bdddd0',
                False,'',
                'TO DO',
                'TO .. DO'],
            "ts_backend_server_status":['4c09b6',
                False,'',
                'EXTRA STORM BACKEND SERVICE INFORMATION RETURNED DURING THE ' +
                'EXECUTION OF STATUS',
                'Extra information are returned by storm backend server init ' +
                'script during the execution of status',
                'rct.ts_backend_server_status(tfn, uid, lfn)'],
            "ts_backend_logrotate_file":['33895c',
                False,'',
                'STORN BACKEND LOGROTATE FILE POINTS TO NON EXISTING FILE',
                'StoRM Backend logrotate file points to non existing file',
                'rct.ts_backend_logrotate_file(tfn, uid, lfn)'],
            "ts_backend_cron_file":['',
                False,'',
                'STORM BACKEND DOES NOT ROTATE LOG FILES',
                'StoRM Backend does not rotate log files',
                'rct.ts_backend_cron_file(tfn, uid, lfn)'],
            "ts_backend_gridhttps":['591891',
                False,'',
                'DEFAULT GRIDHTTPS SERVER PORT NUMBER CONFLICTS WITH BACKEND ' +
                'DEFAULT XMLRPC PORT NUMBER',
                'Default GridHTTPs server port number conflicts with Backend ' +
                'default xmlrpc port number',
                'rct.ts_backend_gridhttps(tfn, uid, lfn)'],
            "ts_yaim_version_file":['813214',
                False,'',
                'WRONG VERSION IN THE YAIM-VERSION FILE',
                'Wrong version in the yaim-storm file',
                'rct.ts_yaim_version_file(tfn, uid, lfn)'],
            "ts_size_in_namespace_file":['c99e16',
                False,'',
                'WRONG SETTINGS OF SIZE IN NAMESPACE.XML',
                'Wrong settings of size in namespace.xml',
                'rct.ts_size_in_namespace_file(tfn, uid, lfn)'],
            "ts_gridhttps_plugin_links":['1f8a8a',
                False,'',
                'REMOVED GRIDHTTPS PLUGIN LINKS DURING UPGRADE FROM 1.7.0 to ' +
                '1.7.1',
                'Removed gridhttpds plugin links during upgrade from 1.7.0 to ' +
                '1.7.1',
                'rct.ts_gridhttps_plugin_links(tfn, uid, lfn)'],
            "ts_backend_server_name_status":['842319',
                False,'',
                'WRONG STORM BACKEND SERVER NAME RETURNED DURING THE ' +
                'EXECUTION OF STATUS',
                'StoRM Backend Server name is wrong',
                'rct.ts_backend_server_name_status(tfn, uid, lfn)'],
            "ts_mysql_connector_java_links":['a61eb8',
                False,'',
                'MYSQL-CONNECTOR-JAVA DOWNLOADING FAILURE',
                'mysql-connector-java is not downloaded due to an issue in ' +
                'its owner repository',
                'rct.ts_mysql_connector_java_links(tfn, uid, lfn)'],
            "ts_mysql_storage_space_update":['',
                False,'',
                'NO UPDATING OF STORAGE SPACE IN DB AFTER A TOTAL ONLINE ' +
                'SIZE CHANGE IN THE NAMESPACE.XML',
                'When the TotalOnlineSize value has changed in the ' +
                'namespace.xml, the storm-backend-server process does not ' +
                'update the  corrispondent field in the storage_space table ' +
                'of the storm_be_ISAM  database',
                'rct.ts_mysql_storage_space_update(tfn, uid, lfn)']
            }

        self.regressions_ldap_tests = {
            "test_glue_service":['6ec220',
                False,'',
                'STORM BUG: GLUESERVICENAME AND GLUESERVIVETYPE CONTAIN ' +
                'WRONG VALUES',
                'Yaim-Storm for GLUE2 configuration called a worng script ' +
                'setting wrong values in the GlueServiceName and ' +
                'GlueServiceType attributes of the GLUE1.3 schema'],
            "test_glue_available_space_info_service":['2f6695',
                False,'',
                'INFO SERVICE ALWAYS RETURNS A ZERO AVAILABLE SPACE',
                'Info Service always returns a zero available space'],
            "test_glue_available_space":['884d3b',
                False,'',
                'WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB',
                'Wrong calculation of SA_AVAILABLE_SPACE'],
            "test_glue_used_space":['50155e',
                False,'',
                'WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB',
                'Wrong calculation of SA_USED_SPACE'],
            "test_size":['ca2419',
                False,'',
                'GET_SIZE INCORRECTLY HANDLES THE INFO',
                'Wrong calculation of SA_USED_SPACE'],
            "test_info_service_failure":['82dc47',
                False,'',
                'REST INFO SERVICE FAILURE',
                'Rest info service fails when non-mandatory parameters are ' +
                'missing'],
            "test_gluetwo_storage_share_capacity":['aae0b5',
                False,'',
                'GLUE2 GLUE2STORAGESHARECAPACITY* SIZES ALWAYS ZERO',
                'Glue2 GLUE2StorageShareCapacity* sizes always 0'],
            "test_gluetwo_endpoint_undefined":['9cc43b',
                False,'',
                'STORM BUG: GLUE2ENDPOINTCAPABILITY AND ' +
                'GLUE2ENDPOINTINTERFACENAME CONTAIN WRONG VALUES',
                'Yaim-Storm for GLUE2 configuration set wrong values in the ' +
                'GLUE2EndpointCapability and GLUE2EndpointInterfaceName ' +
                'attributes of the GLUE2.0 schema'],
            "test_gluetwo_storage_undefined":['14c174',
                False,'',
                'STORM BUG: GLUE2STORAGESHAREACCESSMODE',
                'Yaim-Storm for GLUE2 configuration set wrong values in the ' +
                'GLUE2StorageAccessMode attribute of the GLUE2.0 schema'],
            "test_gluetwo_endpoint":['eecdc3',
                False,'',
                'STORM BUG: GLUE2ENDPOINTCAPABILITY AND ' +
                'GLUE2ENDPOINTINTERFACENAME CONTAIN WRONG VALUES',
                'Yaim-Storm for GLUE2 configuration set wrong values in the ' +
                'GLUE2EndpointCapability and GLUE2EndpointInterfaceName ' +
                'attributes of the GLUE2.0 schema'],
            "ts_glue_service":['1dffdd',
                False,'',
                'STORM BUG: GLUESERVICENAME AND GLUESERVIVETYPE CONTAIN ' +
                'WRONG VALUES',
                'Yaim-Storm for GLUE2 configuration called a worng script ' +
                'setting wrong values in the GlueServiceName and ' +
                'GlueServiceType attributes of the GLUE1.3 schema',
                'rlt.ts_glue_service(tfn, uid, lfn)'],
            "ts_glue_available_space_info_service":['bf5904',
                False,'',
                'INFO SERVICE ALWAYS RETURNS A ZERO AVAILABLE SPACE',
                'Info Service always returns a zero available space',
                'rlt.ts_glue_available_space_info_service(tfn, uid, lfn)'],
            "ts_glue_available_space":['138620',
                False,'',
                'WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB',
                'Wrong calculation of SA_AVAILABLE_SPACE',
                'rlt.ts_glue_available_space(tfn, uid, lfn)'],
            "ts_glue_used_space":['c860c9',
                False,'',
                'WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB',
                'Wrong calculation of SA_USED_SPACE',
                'rlt.ts_glue_used_space(tfn, uid, lfn)'],
            "ts_size":['449568',
                False,'',
                'GET_SIZE INCORRECTLY HANDLES THE INFO',
                'Wrong calculation of SA_USED_SPACE',
                'rlt.ts_size(tfn, uid, lfn)'],
            "ts_info_service_failure":['59de9f',
                False,'',
                'REST INFO SERVICE FAILURE',
                'Rest info service fails when non-mandatory parameters are ' +
                'missing',
                'rlt.ts_info_service_failure(tfn, uid, lfn)'],
            "ts_gluetwo_storage_share_capacity":['3d2509',
                False,'',
                'GLUE2 GLUE2STORAGESHARECAPACITY* SIZES ALWAYS ZERO',
                'Glue2 GLUE2StorageShareCapacity* sizes always 0',
                'rlt.ts_gluetwo_storage_share_capacity(tfn, uid, lfn)'],
            "ts_gluetwo_endpoint_undefined":['29dacc',
                False,'',
                'STORM BUG: GLUE2ENDPOINTCAPABILITY AND ' +
                'GLUE2ENDPOINTINTERFACENAME CONTAIN WRONG VALUES',
                'Yaim-Storm for GLUE2 configuration set wrong values in the ' +
                'GLUE2EndpointCapability and GLUE2EndpointInterfaceName ' +
                'attributes of the GLUE2.0 schema',
                'rlt.ts_gluetwo_endpoint_undefined(tfn, uid, lfn)'],
            "ts_gluetwo_storage_undefined":['43a843',
                False,'',
                'STORM BUG: GLUE2STORAGESHAREACCESSMODE',
                'Yaim-Storm for GLUE2 configuration set wrong values in the ' +
                'GLUE2StorageAccessMode attribute of the GLUE2.0 schema',
                'rlt.ts_gluetwo_storage_undefined(tfn, uid, lfn)'],
            "ts_gluetwo_endpoint":['29dacc',
                False,'',
                'STORM BUG: GLUE2ENDPOINTCAPABILITY AND ' +
                'GLUE2ENDPOINTINTERFACENAME CONTAIN WRONG VALUES',
                'Yaim-Storm for GLUE2 configuration set wrong values in the ' +
                'GLUE2EndpointCapability and GLUE2EndpointInterfaceName ' +
                'attributes of the GLUE2.0 schema',
                'rlt.ts_gluetwo_endpoint_undefined(tfn, uid, lfn)']
            }
 
        self.common_tests = {
            "test_settings":['8b4923',
                False,'',
                'CONFIGURATION INI FILE CORRECTNESS',
                'Verify the content of test ini file'],
            "test_dd":['487f17',
                False,'',
                'CREATE A FILE OF A GIVEN SIZE',
                'Verify the creation of a file with a given size'],
            "test_cr_lf":['d336a7',
                False,'',
                'CREATE A FILE WITH A CHAR',
                'Verify the creation of a file with a char'],
            "test_rm_lf":['1c0731',
                False,'',
                'DELETE A LOCAL FILE',
                'Verify the deletion of a local file'],
            "ts_conf":['',
                False,'',
                'CONFIGURATION INI FILE CORRECTNESS',
                'Verify the content of test ini file',
                'cts.ts_conf(tfn,ifn,dfn,back_ifn, uid, lfn)']
            }

        self.categories_tests = {
            'atomics_tests':('AT',False),
            'functionalities_tests':('ST',False),
            'functionalities_no_voms_tests':('ST',False),
            'regressions_tests':('ST',True), 
            'regressions_no_voms_tests':('ST',True),
            'regressions_conf_tests':('DT',True), 
            'regressions_ldap_tests':('DT',True),
            'common_tests':('UT',False)
            }

    def __get_test_detail(self, test_name):
        '''Returns a tuple containing test detail'''

        for key, value in self.categories_tests.items():
            if test_name in eval('self.' + key).keys():
                v = value
                break

        return v

    def __get_all_tests(self):
        '''Returns a dictionary containing all categories tests'''

        all_tests = {}

        for key, value in self.categories_tests.items():
            all_tests.update(eval('self.' + key))

        return all_tests

    def __get_tests_lists(self):
        '''Returns a dictionary containing a map between test and id'''

        test_ids = {}

        for key, value in self.__get_all_tests().items():
            id = ''
            if value[0] == '':
                uuid = utils.get_uuid()
                if len(uuid) > 6:
                    id = uuid[:6]
                else:
                    id = uuid
            else:
                id = value[0]
 
            test_detail = self.__get_test_detail(key)

            if 'ts_' in key:
                test_ids[key] = [id, test_detail[0], test_detail[1], value[1], value[2], value[3], value[4], value[5]]
            else:
                test_ids[key] = [id, test_detail[0], test_detail[1], value[1], value[2], value[3], value[4]]
                
        return test_ids

    def __set_map_file_entry(self, map_len, current_index, file_index, key, value):
        '''Set an entry in the map file'''

        tm ='[\n'
        for x in value:
            if type(x).__name__ == 'str':
                tm = tm + '    "' + x + '"'
            elif type(x).__name__ == 'bool':
                tm = tm + '    ' + str(x).lower()
            if value.index(x) == len(value)-1:
                tm = tm + '\n    ]'
                #print ' %s %s = %s' % (str(value.index(x)), str(len(value)-1), tm)
            else:
                tm = tm + ',\n'
                #print ' %s %s != %s' % (str(value.index(x)), str(len(value)-1), tm)

        if map_len == current_index:
            file_index.write('  "' + key + '":' + tm + '\n')
        else:
            file_index.write('  "' + key + '":' + tm + ',\n')

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

    def create_new_map_file(self):
        '''Creates a json file containing ts name as key, and a tuple 
           (<id>, <type of test>, Boolean, Boolean, <name>, <description>, <r>)
           as value'''

        map_tests_ids = self.__get_tests_lists()

        configuration_path = settings.get_configuration_path()
        destination_file=configuration_path + 'map_tests_ids.json'
        df = open(destination_file, 'a')
        df.write('{\n')

        a=0
        for x in map_tests_ids.keys():
            self.__set_map_file_entry(len(map_tests_ids), a+1, df, x, map_tests_ids[x])
            a+=1

        df.write('}\n')
        df.close()

        self.verify_map_file(destination_file)

    def modify_new_map_file(self):
        '''Modifies a json file containing test as key, and id as value'''

        map_tests_ids = self.__get_tests_lists()

        source_file = settings.get_configuration_file(file_name = 'map_tests_ids.json')
        source_tests_ids_info = self.verify_map_file(source_file)
        destination_file = settings.get_configuration_path(file_name = source_file) + '/map_tests_ids.json.tmp'
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
