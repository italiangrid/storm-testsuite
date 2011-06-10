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

class RegressionTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn,bifn):
      super(RegressionTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn

    def test_ls_file(self):
      self.lsat_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.lsat_result['status'] == 'PASS')
      self.lcksm_result = cksm.CksmLf(self.ifn).get_output()
      self.assert_(self.lsat_result['Checksum'] == self.lcksm_result['Checksum'])

    def test_update_used_soace_upon(self):
      self.st_result = space.StoRMGst(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.tsets['general']['spacetoken']).get_output()
      self.assert_(self.st_result['status'] == 'PASS')
      self.sm1_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.st_result['arrayOfSpaceTokens']).get_output()
      self.assert_(self.sm1_result['status'] == 'PASS')
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      print self.cp_result
      self.assert_(self.cp_result['status'] == 'PASS')
      self.lls_result = sizefile.Ls(self.ifn).get_output()
      self.assert_(self.lls_result['status'] == 'PASS')
      self.sm2_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.st_result['arrayOfSpaceTokens']).get_output()
      print self.lls_result['status'], self.sm1_result['unused'], self.sm2_result['unused'] 
      self.assert_(inf(self.lls_result['size']) == int(self.sm1_result['unused']) - int(self.sm2_result['unused']))
