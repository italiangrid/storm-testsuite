__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ls
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import rmdir
from tstorm.utils import cksm

class HttpsTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, prt, voms=False):
      super(HttpsTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.prt = prt
      self.bifn = bifn
      self.voms = voms

    def test_srm_transfer_outbound_http(self):
      self.lsbt_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn).get_output()
      self.assert_(self.lsbt_result['status'] == 'FAILURE')
      self.ptp_result = cp.StoRMPtp(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptp_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL']).get_output(False, True)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.pd_result = cp.StoRMPd(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn, self.ptp_result['requestToken']).get_output()
      self.assert_(self.pd_result['status'] == 'PASS')
      self.lsat_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn).get_output()
      self.assert_(self.lsat_result['status'] == 'PASS')

    def test_direct_transfer_outbound_http(self):
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn + ts

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(False, True)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_outbound_http_exist_file(self):
      a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(False, True)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_http(self):
      a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(False, False)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_http_unexist_file(self):
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn + ts
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(False, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_srm_transfer_inbound_http(self):
      self.ptg_result = cp.StoRMPtg(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptg_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL']).get_output(False, False)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn, self.ptg_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')
      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')

    def test_srm_transfer_outbound_https(self):
      self.lsbt_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn).get_output()
      self.assert_(self.lsbt_result['status'] == 'FAILURE')
      self.ptp_result = cp.StoRMPtp(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptp_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL']).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.pd_result = cp.StoRMPd(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn, self.ptp_result['requestToken']).get_output()
      self.assert_(self.pd_result['status'] == 'PASS')
      self.lsat_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn).get_output()
      self.assert_(self.lsat_result['status'] == 'PASS')

    def test_direct_transfer_outbound_https(self):
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms'] + self.dfn + ts

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_outbound_https_exist_file(self):
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms'] + self.dfn

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_https(self):
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms']  + self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_https_no_auth(self):
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_auth']  + self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_inbound_https_unexist_file(self):
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms']  + self.dfn + ts
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_srm_transfer_inbound_https(self):
      self.ptg_result = cp.StoRMPtg(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptg_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL']).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn, self.ptg_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')
      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')

    def test_srm_transfer_outbound_https_voms(self):
      self.lsbt_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn).get_output()
      self.assert_(self.lsbt_result['status'] == 'FAILURE')
      self.ptp_result = cp.StoRMPtp(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptp_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptp_result['TURL']).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.pd_result = cp.StoRMPd(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn, self.ptp_result['requestToken']).get_output()
      self.assert_(self.pd_result['status'] == 'PASS')
      self.lsat_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn).get_output()
      self.assert_(self.lsat_result['status'] == 'PASS')

    def test_direct_transfer_outbound_https_voms(self):
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn + ts

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_outbound_https_voms_exist_file(self):
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_https_voms(self):
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_https_voms_no_auth(self):
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_auth'] + self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_inbound_https_voms_unexist_file(self):
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn + ts

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_srm_transfer_inbound_https_voms(self):
      self.ptg_result = cp.StoRMPtg(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptg_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL']).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn, self.ptg_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')
      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
