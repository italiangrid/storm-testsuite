#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ls
from tstorm.utils import cp
from tstorm.utils import rm

class HttpsTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, prt, lfn, voms=False):
        super(HttpsTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.prt = prt
        self.bifn = bifn
        self.lfn = lfn
        self.voms = voms

    def test_srm_transfer_outbound_http(self):
        self.lfn.put_name('SRM TRANSFER OUTBOUND HTTP')
        des = '''Verify that the file has been transferred by using the http
protocol.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['http']['no_voms'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.ls_result = lcg_ls.get_output()
        self.assert_(self.ls_result['status'] == 'FAILURE')

        storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                    self.tsets['http']['no_voms'], self.dfn, self.prt)
        self.lfn.put_cmd(storm_ptp.get_command())
        self.ptp_result = storm_ptp.get_output()
        self.assert_(self.ptp_result['status'] == 'PASS')

        cp_curl = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL'])
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(False, True)
        self.assert_(self.curl_result['status'] == 'PASS')

        storm_pd = cp.StoRMPd(self.tsets['general']['endpoint'],
                   self.tsets['http']['no_voms'], self.dfn,
                   self.ptp_result['requestToken'])
        self.lfn.put_cmd(storm_pd.get_command())
        self.pd_result = storm_pd.get_output()
        self.assert_(self.pd_result['status'] == 'PASS')

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['http']['no_voms'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.ls_result = lcg_ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_outbound_http(self):
        self.lfn.put_name('DIRECT TRANSFER OUTBOUND HTTP')
        des = '''Verify that the file has been transferred by using http.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn + ts

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(False, True)
        self.assert_(self.curl_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_outbound_http_exist_file(self):
        self.lfn.put_name('DIRECT TRANSFER OUTBOUND HTTP')
        des = '''Verify that the file has been transferred by using http,
when file exists.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(False, True)
        self.assert_(self.curl_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_inbound_http(self):
        self.lfn.put_name('DIRECT TRANSFER INBOUND HTTP')
        des = '''Verify that the file has been transferred back by using http.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn
  
        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(False, False)
        self.assert_(self.curl_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_inbound_http_unexist_file(self):
        self.lfn.put_name('DIRECT TRANSFER INBOUND HTTP')
        des = '''Verify that the file has not been transferred back by using
http, when file does not exist.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn + ts

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(False, False)
        self.assert_(self.curl_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_srm_transfer_inbound_http(self):
        self.lfn.put_name('SRM TRANSFER INBOUND HTTP')
        des = '''Verify that the file has been transferred back by using http.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                    self.tsets['http']['no_voms'], self.dfn, self.prt)
        self.lfn.put_cmd(storm_ptg.get_command())
        self.ptg_result = storm_ptg.get_output()
        self.assert_(self.ptg_result['status'] == 'PASS')

        cp_curl = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL'])
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(False, False)
        self.assert_(self.curl_result['status'] == 'PASS')

        storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                   self.tsets['http']['no_voms'], self.dfn,
                   self.ptg_result['requestToken'])
        self.lfn.put_cmd(storm_rf.get_command())
        self.rf_result = storm_rf.get_output()
        self.assert_(self.rf_result['status'] == 'PASS')

        storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                   self.tsets['http']['no_voms'], self.dfn)
        self.lfn.put_cmd(storm_rm.get_command())
        self.rm_result = storm_rm.get_output()
        self.assert_(self.rm_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_srm_transfer_outbound_https(self):
        self.lfn.put_name('SRM TRANSFER OUTBOUND HTTPS')
        des = '''Verify that the file has been transferred by using https.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['https']['no_voms'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.lsbt_result = lcg_ls.get_output()
        self.assert_(self.lsbt_result['status'] == 'FAILURE')

        storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                    self.tsets['https']['no_voms'], self.dfn, self.prt)
        self.lfn.put_cmd(storm_ptp.get_command())
        self.ptp_result = storm_ptp.get_output()
        self.assert_(self.ptp_result['status'] == 'PASS')

        cp_curl = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL'])
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, True)
        self.assert_(self.curl_result['status'] == 'PASS')

        storm_pd = cp.StoRMPd(self.tsets['general']['endpoint'],
                   self.tsets['https']['no_voms'], self.dfn,
                   self.ptp_result['requestToken'])
        self.lfn.put_cmd(storm_pd.get_command())
        self.pd_result = storm_pd.get_output()
        self.assert_(self.pd_result['status'] == 'PASS')

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['https']['no_voms'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.lsat_result = lcg_ls.get_output()
        self.assert_(self.lsat_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_outbound_https(self):
        self.lfn.put_name('DIRECT TRANSFER OUTBOUND HTTPS')
        des = '''Verify that the file has been transferred by using https.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms'] + self.dfn + ts

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, True)
        self.assert_(self.curl_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_outbound_https_exist_file(self):
        self.lfn.put_name('DIRECT TRANSFER OUTBOUND HTTPS')
        des = '''Verify that the file has been transferred by using https,
when the file exists.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms'] + self.dfn

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, True)
        self.assert_(self.curl_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_inbound_https(self):
        self.lfn.put_name('DIRECT TRANSFER INBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms']  + self.dfn

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, False)
        self.assert_(self.curl_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_no_auth(self):
        self.lfn.put_name('DIRECT TRANSFER INBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https
without authorization.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_auth']  + self.dfn

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, False)
        self.assert_(self.curl_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_unexist_file(self):
        self.lfn.put_name('DIRECT TRANSFER INBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https,
when file does not exist.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms']  + self.dfn + ts

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, False)
        self.assert_(self.curl_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_srm_transfer_inbound_https(self):
        self.lfn.put_name('SRM TRANSFER INBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                    self.tsets['https']['no_voms'], self.dfn, self.prt)
        self.lfn.put_cmd(storm_ptg.get_command())
        self.ptg_result = storm_ptg.get_output()
        self.assert_(self.ptg_result['status'] == 'PASS')

        cp_curl = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL'])
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, False)
        self.assert_(self.curl_result['status'] == 'PASS')

        storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                   self.tsets['https']['no_voms'], self.dfn,
                   self.ptg_result['requestToken'])
        self.lfn.put_cmd(storm_rf.get_command())
        self.rf_result = storm_rf.get_output()
        self.assert_(self.rf_result['status'] == 'PASS')

        storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                   self.tsets['https']['no_voms'], self.dfn)
        self.lfn.put_cmd(storm_rm.get_command())
        self.rm_result = storm_rm.get_output()
        self.assert_(self.rm_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_srm_transfer_outbound_https_voms(self):
        self.lfn.put_name('SRM TRANSFER OUTBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https
with voms.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['https']['voms'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.lsbt_result = lcg_ls.get_output()
        self.assert_(self.lsbt_result['status'] == 'FAILURE')

        storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                    self.tsets['https']['voms'], self.dfn, self.prt)
        self.lfn.put_cmd(storm_ptp.get_command())
        self.ptp_result = storm_ptp.get_output()
        self.assert_(self.ptp_result['status'] == 'PASS')

        cp_curl = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL'])
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, True)
        self.assert_(self.curl_result['status'] == 'PASS')

        storm_pd = cp.StoRMPd(self.tsets['general']['endpoint'],
                   self.tsets['https']['voms'], self.dfn,
                   self.ptp_result['requestToken'])
        self.lfn.put_cmd(storm_pd.get_command())
        self.pd_result = storm_pd.get_output()
        self.assert_(self.pd_result['status'] == 'PASS')

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['https']['voms'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.lsat_result = lcg_ls.get_output()
        self.assert_(self.lsat_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_outbound_https_voms(self):
        self.lfn.put_name('DIRECT TRANSFER OUTBOUND HTTPS')
        des = '''Verify that the file has been transferred by using https
with voms.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn + ts

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, True)
        self.assert_(self.curl_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_outbound_https_voms_exist_file(self):
        self.lfn.put_name('DIRECT TRANSFER OUTBOUND HTTPS')
        des = '''Verify that the file has been transferred by using https
with voms when file exists.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, True)
        self.assert_(self.curl_result['status'] == 'PASS')
 
        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_voms(self):
        self.lfn.put_name('DIRECT TRANSFER INBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https
with voms.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, False)
        self.assert_(self.curl_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_voms_no_auth(self):
        self.lfn.put_name('DIRECT TRANSFER INBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https
with voms without authorization.'''
        self.lfn.put_description(des)
        self.lfn.put_description('with voms but no auth')
        self.lfn.put_uid('')
        self.lfn.put_output()

        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_auth'] + self.dfn
  
        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, False)
        self.assert_(self.curl_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_voms_unexist_file(self):
        self.lfn.put_name('DIRECT TRANSFER INBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https
with voms when file does not exist.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn + ts

        cp_curl = cp.curl(self.ifn, self.bifn, a)
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, False)
        self.assert_(self.curl_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_srm_transfer_inbound_https_voms(self):
        self.lfn.put_name('SRM TRANSFER INBOUND HTTPS')
        des = '''Verify that the file has been transferred back by using https
with voms.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                    self.tsets['https']['voms'], self.dfn, self.prt)
        self.lfn.put_cmd(storm_ptg.get_command())
        self.ptg_result = storm_ptg.get_output()
        self.assert_(self.ptg_result['status'] == 'PASS')

        cp_curl = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL'])
        self.lfn.put_cmd(cp_curl.get_command())
        self.curl_result = cp_curl.get_output(True, False)
        self.assert_(self.curl_result['status'] == 'PASS')

        storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                   self.tsets['https']['voms'], self.dfn,
                   self.ptg_result['requestToken'])
        self.lfn.put_cmd(storm_rf.get_command())
        self.rf_result = storm_rf.get_output()
        self.assert_(self.rf_result['status'] == 'PASS')

        storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                   self.tsets['https']['voms'], self.dfn)
        self.lfn.put_cmd(storm_rm.get_command())
        self.rm_result = storm_rm.get_output()
        self.assert_(self.rm_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
