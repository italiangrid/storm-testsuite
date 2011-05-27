__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import config
from tstorm.utils import createfile
from tstorm.utils import removefile
from tstorm.utils import ls
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import rmdir
from tstorm.utils import cksm

class 8DigitStringChecksumRt(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn,bifn):
      super(8DigitStringChecksumRt, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn
    
    def test_settings(self):
      for x in self.tsets:
        self.assert_(x in ('general','bug-general'))
        for y in self.tsets[x]:
            self.assert_(x != '')

    def test_cf(self):
      self.cf_result = createfile.Cf(self.ifn).get_output()
      self.assert_(self.cf_result['status'] == 'PASS')

    def test_ls_bt(self):
      for x in self.tsets:
        self.lsbt_result = ls.LcgLs(self.tsets[x]['endpoint'], self.tsets[x]['accesspoint'], self.dfn).get_output()
        self.assert_(self.lsbt_result['status'] == 'FAILURE')

    def test_cp_bt(self):
      for x in self.tsets:
        self.cpbt_result = cp.LcgCp(self.tsets[x]['endpoint'], self.tsets[x]['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
        self.assert_(self.cpbt_result['status'] == 'PASS')

    def test_ls_at(self):
      for x in self.tsets:
        self.lsat_result = ls.LcgLs(self.tsets[x]['endpoint'], self.tsets[x]['accesspoint'], self.dfn).get_output()
        self.assert_(self.lsat_result['status'] == 'PASS')
        self.lcksm_result = cksm.CksmLf(self.ifn).get_output()
        
        if x == 'general':
          self.assert_(self.lsat_result['Checksum'] == self.lcksm_result['Checksum'])
        elif x == 'bug-general':
          self.assert_(self.lsat_result['Checksum'] != self.lcksm_result['Checksum'])

    def test_rm(self):
      for x in self.tsets:
        self.rm_result = rm.SrmRm(self.tsets[x]['endpoint'], self.tsets[x]['accesspoint'], self.dfn).get_output()
        self.assert_(self.rm_result['status'] == 'PASS')

    def test_rmdir(self):
      for x in self.tsets:
        if '/' in self.dfn:
          a=os.path.dirname(self.dfn)
          self.rmdir_result = rmdir.SrmRmdir(self.tsets[x]['endpoint'], self.tsets[x]['accesspoint'], a).get_output()
          for x in self.rmdir_result['status']:
            self.assert_(x == 'PASS')

    def test_rm_lf(self):
      self.rmlf_result = removefile.RmLf(self.ifn, '').get_output()
      self.assert_(self.rmlf_result['status'] == 'PASS')
