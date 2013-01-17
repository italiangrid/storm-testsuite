__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
import inspect
from tstorm.utils import config
from tstorm.commands import ls
from tstorm.commands import cp
from tstorm.commands import rm
from tstorm.utils import utils

class HttpsTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, prt, uid, lfn, voms=False):
        super(HttpsTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.prt = prt
        self.bifn = bifn
        self.id = uid.get_id()
        self.lfn = lfn
        self.voms = voms

    def test_srm_transfer_outbound_http(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['http']['no_voms'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            self.ls_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(self.ls_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                 self.tsets['http']['no_voms'], self.dfn, protocol=self.prt)
            self.lfn.put_cmd(storm_ptp.get_command())
            self.ptp_result = storm_ptp.get_output()

            msg = 'storm ptp status'
            self.assert_(self.ptp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            cp_curl = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL'])
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=False, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=False, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_pd = cp.StoRMPd(self.tsets['general']['endpoint'],
                 self.tsets['http']['no_voms'], self.dfn,
                 self.ptp_result['requestToken'])
            self.lfn.put_cmd(storm_pd.get_command())
            self.pd_result = storm_pd.get_output()

            msg = 'storm pd status'
            self.assert_(self.pd_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['http']['no_voms'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            self.ls_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(self.ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_outbound_http(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            t=datetime.datetime.now()
            ts=str(time.mktime(t.timetuple()))
            turl = 'http://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['http_port'] + '/storageArea/'
            turl += self.tsets['http']['no_voms'] +  self.dfn + ts

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=False, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=False, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_outbound_http_exist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            turl = 'http://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['http_port'] + '/storageArea/'
            turl += self.tsets['http']['no_voms'] +  self.dfn

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=False, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=False, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_inbound_http(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            turl = 'http://' 
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':' 
            turl += self.tsets['general']['http_port'] + '/storageArea/'
            turl += self.tsets['http']['no_voms'] +  self.dfn
  
            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=False, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=False, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_inbound_http_unexist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            t=datetime.datetime.now()
            ts=str(time.mktime(t.timetuple()))
            turl = 'http://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['http_port'] + '/storageArea/'
            turl += self.tsets['http']['no_voms'] +  self.dfn + ts

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=False, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=False, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_srm_transfer_inbound_http(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                 self.tsets['http']['no_voms'], self.dfn, self.prt)
            self.lfn.put_cmd(storm_ptg.get_command())
            self.ptg_result = storm_ptg.get_output()

            msg = 'storm ptg status'
            self.assert_(self.ptg_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            cp_curl = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL'])
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=False, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=False, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                 self.tsets['http']['no_voms'], self.dfn,
                 self.ptg_result['requestToken'])
            self.lfn.put_cmd(storm_rf.get_command())
            self.rf_result = storm_rf.get_output()

            msg = 'storm rf status'
            self.assert_(self.rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                 self.tsets['http']['no_voms'], self.dfn)
            self.lfn.put_cmd(storm_rm.get_command())
            self.rm_result = storm_rm.get_output()

            msg = 'storm rm status'
            self.assert_(self.rm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_srm_transfer_outbound_https(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['https']['no_voms'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            self.lsbt_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(self.lsbt_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                 self.tsets['https']['no_voms'], self.dfn, protocol=self.prt)
            self.lfn.put_cmd(storm_ptp.get_command())
            self.ptp_result = storm_ptp.get_output()

            msg = 'storm ptp status'
            self.assert_(self.ptp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            cp_curl = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL'])
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_pd = cp.StoRMPd(self.tsets['general']['endpoint'],
                 self.tsets['https']['no_voms'], self.dfn,
                 self.ptp_result['requestToken'])
            self.lfn.put_cmd(storm_pd.get_command())
            self.pd_result = storm_pd.get_output()

            msg = 'storm pd status'
            self.assert_(self.pd_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['https']['no_voms'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            self.lsat_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(self.lsat_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_outbound_https(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            t=datetime.datetime.now()
            ts=str(time.mktime(t.timetuple()))
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['no_voms'] + self.dfn + ts

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_outbound_https_exist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['no_voms'] + self.dfn

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_inbound_https(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['no_voms']  + self.dfn

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_no_auth(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['no_auth']  + self.dfn

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_unexist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            t=datetime.datetime.now()
            ts=str(time.mktime(t.timetuple()))
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['no_voms']  + self.dfn + ts

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_srm_transfer_inbound_https(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                 self.tsets['https']['no_voms'], self.dfn, self.prt)
            self.lfn.put_cmd(storm_ptg.get_command())
            self.ptg_result = storm_ptg.get_output()

            msg = 'storm ptg status'
            self.assert_(self.ptg_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            cp_curl = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL'])
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                 self.tsets['https']['no_voms'], self.dfn,
                 self.ptg_result['requestToken'])
            self.lfn.put_cmd(storm_rf.get_command())
            self.rf_result = storm_rf.get_output()

            msg = 'storm rf status'
            self.assert_(self.rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                 self.tsets['https']['no_voms'], self.dfn)
            self.lfn.put_cmd(storm_rm.get_command())
            self.rm_result = storm_rm.get_output()

            msg = 'storm rm status'
            self.assert_(self.rm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_srm_transfer_outbound_https_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['https']['voms'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            self.lsbt_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(self.lsbt_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                 self.tsets['https']['voms'], self.dfn, protocol=self.prt)
            self.lfn.put_cmd(storm_ptp.get_command())
            self.ptp_result = storm_ptp.get_output()

            msg = 'storm ptp status'
            self.assert_(self.ptp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            cp_curl = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL'])
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_pd = cp.StoRMPd(self.tsets['general']['endpoint'],
                 self.tsets['https']['voms'], self.dfn,
                 self.ptp_result['requestToken'])
            self.lfn.put_cmd(storm_pd.get_command())
            self.pd_result = storm_pd.get_output()

            msg = 'storm pd status'
            self.assert_(self.pd_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['https']['voms'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            self.lsat_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(self.lsat_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_outbound_https_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            t=datetime.datetime.now()
            ts=str(time.mktime(t.timetuple()))
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['voms'] + self.dfn + ts

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_outbound_https_voms_exist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['voms'] + self.dfn

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=True))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=True)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')
 
        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':' 
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['voms'] + self.dfn

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_voms_no_auth(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['no_auth'] + self.dfn
  
            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_direct_transfer_inbound_https_voms_unexist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            t=datetime.datetime.now()
            ts=str(time.mktime(t.timetuple()))
            turl = 'https://'
            turl += self.tsets['general']['gridhttp_server_hostname'] + ':'
            turl += self.tsets['general']['https_port'] + '/storageArea/'
            turl += self.tsets['https']['voms'] + self.dfn + ts

            cp_curl = cp.curl(self.ifn, self.bifn, turl)
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_srm_transfer_inbound_https_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                 self.tsets['https']['voms'], self.dfn, self.prt)
            self.lfn.put_cmd(storm_ptg.get_command())
            self.ptg_result = storm_ptg.get_output()

            msg = 'storm ptg status'
            self.assert_(self.ptg_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            cp_curl = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL'])
            self.lfn.put_cmd(cp_curl.get_command(use_ssl=True, in_write=False))
            self.curl_result = cp_curl.get_output(use_ssl=True, in_write=False)

            msg = 'curl status'
            self.assert_(self.curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                 self.tsets['https']['voms'], self.dfn,
                 self.ptg_result['requestToken'])
            self.lfn.put_cmd(storm_rf.get_command())
            self.rf_result = storm_rf.get_output()

            msg = 'storm rf status'
            self.assert_(self.rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                 self.tsets['https']['voms'], self.dfn)
            self.lfn.put_cmd(storm_rm.get_command())
            self.rm_result = storm_rm.get_output()

            msg = 'storm rm status'
            self.assert_(self.rm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
