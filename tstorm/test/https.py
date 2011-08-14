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
      print '''\nBT 3.3.9 normal workflow\n'''
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
      print '''\nBT 3.3.15 normal workflow\n'''
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn + ts

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(False, True)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_outbound_http_exist_file(self):
      print '''\nBT 3.3.15 existent file\n'''
      a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(False, True)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_http(self):
      print '''\nBT 3.3.18 normal workflow\n'''
      a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(False, False)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_http_unexist_file(self):
      print '''\nBT 3.3.2 unexistent file\n'''
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'http://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['http_port'] + '/storageArea/'+ self.tsets['http']['no_voms'] +  self.dfn + ts
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(False, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_srm_transfer_inbound_http(self):
      print '''\nBT 3.3.12 normal workflow\n'''
      self.ptg_result = cp.StoRMPtg(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptg_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL']).get_output(False, False)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn, self.ptg_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')
      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['http']['no_voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')

    def test_srm_transfer_outbound_https(self):
      print '''\nBT 3.3.10 normal workflow\n'''
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
      print '''\nBT 3.3.16 normal workflow\n'''
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms'] + self.dfn + ts

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_outbound_https_exist_file(self):
      print '''\nBT 3.3.16 existent file\n'''
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms'] + self.dfn

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_https(self):
      print '''\nBT 3.3.19 normal workflow\n'''
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms']  + self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_https_no_auth(self):
      print '''\nBT 3.3.19 no read permission\n'''
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_auth']  + self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_inbound_https_unexist_file(self):
      print '''\nBT 3.3.19 unexistent file\n'''
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_voms']  + self.dfn + ts
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_srm_transfer_inbound_https(self):
      print '''\nBT 3.3.13 normal workflow\n'''
      self.ptg_result = cp.StoRMPtg(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptg_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL']).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn, self.ptg_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')
      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['https']['no_voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')

    def test_srm_transfer_outbound_https_voms(self):
      print '''\nBT 3.3.11 normal workflow\n'''
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
      print '''\nBT 3.3.17 normal workflow\n'''
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn + ts

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_outbound_https_voms_exist_file(self):
      print '''\nBT 3.3.17 existent file\n'''
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, True)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_https_voms(self):
      print '''\nBT 3.3.20 normal workflow\n'''
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'PASS')

    def test_direct_transfer_inbound_https_voms_no_auth(self):
      print '''\nBT 3.3.20 no read permission\n'''
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['no_auth'] + self.dfn
      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_direct_transfer_inbound_https_voms_unexist_file(self):
      print '''\nBT 3.3.20 unexistent file\n'''
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      a = 'https://' + self.tsets['general']['gridhttp_server_hostname'] + ':' + self.tsets['general']['https_port'] + '/storageArea/'+ self.tsets['https']['voms'] + self.dfn + ts

      self.curl_result = cp.curl(self.ifn, self.bifn, a).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'FAILURE')

    def test_srm_transfer_inbound_https_voms(self):
      print '''\nBT 3.3.14 normal workflow\n'''
      self.ptg_result = cp.StoRMPtg(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn, self.prt).get_output()
      self.assert_(self.ptg_result['status'] == 'PASS')
      self.curl_result = cp.curl(self.ifn, self.bifn, self.ptg_result['transferURL']).get_output(True, False)
      self.assert_(self.curl_result['status'] == 'PASS')
      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn, self.ptg_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')
      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
