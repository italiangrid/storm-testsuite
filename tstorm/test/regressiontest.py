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
from tstorm.utils import sizefile
from tstorm.utils import findstrings

class RegressionTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, prt):
      super(RegressionTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn
      self.prt = prt

    def test_eight_digit_string_checksum(self):
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
      ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn)
      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'FAILURE')

      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')
      self.st_result = space.StoRMGst(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.tsets['general']['spacetoken']).get_output()
      self.assert_(self.st_result['status'] == 'PASS')

      sm_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.st_result['arrayOfSpaceTokens'])
      sm1 = sm_result.get_output()
      self.assert_(sm1['status'] == 'PASS')

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

      self.lls_result = sizefile.Ls(self.ifn).get_output()
      self.assert_(self.lls_result['status'] == 'PASS')
      
      sm2 = sm_result.get_output()
      self.assert_(sm2['status'] == 'PASS')
      self.assert_(int(self.lls_result['size']) == int(sm2['unusedSize']) - int(sm1['unusedSize']))

    def test_update_used_space_upon_pd(self):
      self.st_result = space.StoRMGst(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.tsets['general']['spacetoken']).get_output()
      self.assert_(self.st_result['status'] == 'PASS')

      sm_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.st_result['arrayOfSpaceTokens'])
      sm1 = sm_result.get_output()
      self.assert_(sm1['status'] == 'PASS')

      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')
      self.lls_result = sizefile.Ls(self.ifn).get_output()
      self.assert_(self.lls_result['status'] == 'PASS')

      sm2 = sm_result.get_output()
      self.assert_(sm2['status'] == 'PASS')
      self.assert_(int(self.lls_result['size']) == int(sm1['unusedSize']) - int(sm2['unusedSize']))

      self.rm_result = rm.StoRMRm(self.tsets['general']['endpoint'], self.tsets['https']['voms'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.StoRMRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'PASS')

    def test_unsupported_protocols(self):
      self.ptp_result = cp.StoRMPtp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn, 'unsupported').get_output()
      self.assert_(self.ptp_result['status'] == 'FAILURE')
      slef.assert_('SRM_NOT_SUPPORTED' in self.ptp_result['statusCode'])

    def test_both_sup_and_unsup_protocols(self):
      self.ptp_result = cp.StoRMPtp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn, self.prt + ', unsupported').get_output()
      self.assert_(self.ptp_result['status'] == 'PASS')
      self.fs_result =findstrings.Grep().get_output()
      self.assert_(self.fs_result['status'] == 'FAILURE')
