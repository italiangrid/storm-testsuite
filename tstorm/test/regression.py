__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ls
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import rmdir
from tstorm.utils import cksm
from tstorm.utils import space
#from tstorm.utils import sizefile
from tstorm.utils import findstrings
from tstorm.utils import abort

class RegressionTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, prt='gsiftp'):
      super(RegressionTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn
      self.prt = prt

    def test_eight_digit_string_checksum(self):
      print '''\nDescription: The StoRM GridFTP component stores the checksum value computed during the file transfer as a long number, discarding in this way leading zeroes. The default ADLER32 checksum match algorithm considers checksum values as strings so the leading zeroes matters.\n'''
      print '''\nRfC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/108\n'''
      ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn)
      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'FAILURE')

      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')

      self.lcksm_result = cksm.CksmLf(self.ifn).get_output()
      self.assert_(ll['Checksum'] == self.lcksm_result['Checksum'])

      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.StoRMRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'PASS')

    def test_update_free_space_upon_rm(self):
      print '''\nDescription: StoRM does not publish correctly values for used and free space on the BDII due to a bug in the update of the free space after the the srmRm operation\n'''
      print '''\nRfC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/106\n'''
      ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn)
      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'FAILURE')

      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')
      self.st_result = space.StoRMGst(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.tsets['general']['spacetoken']).get_output()
      self.assert_(self.st_result['status'] == 'PASS')

      self.sm1_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.st_result['arrayOfSpaceTokens']).get_output()
      self.assert_(self.sm1_result['status'] == 'PASS')

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')

      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.StoRMRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'PASS')

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'FAILURE')

      self.lls_result = ls.Ls(self.ifn).get_output()
      self.assert_(self.lls_result['status'] == 'PASS')

      self.sm2_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.st_result['arrayOfSpaceTokens']).get_output()
      self.assert_(self.sm2_result['status'] == 'PASS')
 
      a=int(self.sm2_result['unusedSize']) - int(self.sm1_result['unusedSize'])
      self.assert_(int(self.lls_result['size']) == a)

    def test_update_used_space_upon_pd(self):
      print '''\nDescription: StoRM does not provides updated used space value for Space Token due to a bug in the update of the used space after the the srmPutDone operation.\n'''
      print '''\nRfC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/109\n'''
      self.st_result = space.StoRMGst(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.tsets['general']['spacetoken']).get_output()
      self.assert_(self.st_result['status'] == 'PASS')

      self.sm1_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.st_result['arrayOfSpaceTokens']).get_output()
      self.assert_(self.sm1_result['status'] == 'PASS')

      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')
      self.lls_result = ls.Ls(self.ifn).get_output()
      self.assert_(self.lls_result['status'] == 'PASS')

      self.sm2_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.st_result['arrayOfSpaceTokens']).get_output()
      self.assert_(self.sm2_result['status'] == 'PASS')

      a=(int(self.sm1_result['unusedSize']) - int(self.sm2_result['unusedSize']))
      self.assert_(int(self.lls_result['size']) == a)

      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.StoRMRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'PASS')

    def test_unsupported_protocols(self):
      print '''\nDescription: StoRM does not returns SRM_NOT_SUPPORTED error code when file transfer operation (srmPrepareToPut, srmPrepareToGet, srmBringOnline) are called providing a list of not supported desired transfer protocols to a bug in the management of file transfer operation. StoRM does not verifies if the provided protocols are supported\n'''
      print '''\nRfC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/127\n'''
      self.ptp_result = cp.StoRMPtp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn, 'unsupported').get_output()
      self.assert_(self.ptp_result['status'] == 'FAILURE')
      self.assert_('SRM_NOT_SUPPORTED' in self.ptp_result['statusCode'])

    def test_both_sup_and_unsup_protocols(self):
      print '''\nDescription: StoRM Frontend produces huge log file when managing request requesting non supported protocols\n'''
      print '''\nRfC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/126\n'''
      self.ptp_result = cp.StoRMPtp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn, self.prt + ',unsupported').get_output()
      self.assert_(self.ptp_result['status'] == 'PASS')
      self.fs_result =findstrings.Grep().get_output()
      self.assert_(self.fs_result['status'] == 'FAILURE')
      self.ar_result = abort.StoRMAr(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ptp_result['requestToken']).get_output()
      self.assert_(self.ar_result['status'] == 'PASS')

    def test_non_ascii_chars(self):
      print '''\nDescription: StoRM Frontend crashes when managing asynchronous requests providing string parameters containing non ASCII characters.\n'''
      print '''\nRfC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/137\n'''
      self.ls_result = ls.StoRMLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn + 'tèstèèà').get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')



