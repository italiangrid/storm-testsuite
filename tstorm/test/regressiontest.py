__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ls
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import rmdir
from tstorm.utils import cksm

class RegressionTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn,bifn):
      super(RegressionTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn
    
    def test_ls_bt(self):
      self.lsbt_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.lsbt_result['status'] == 'FAILURE')

    def test_cp_bt(self):
      self.cpbt_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cpbt_result['status'] == 'PASS')

    def test_ls_at(self):
      self.lsat_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.lsat_result['status'] == 'PASS')
      self.lcksm_result = cksm.CksmLf(self.ifn).get_output()
      self.assert_(self.lsat_result['Checksum'] == self.lcksm_result['Checksum'])

    def test_rm(self):
      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')

    def test_rmdir(self):
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.SrmRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'PASS')
