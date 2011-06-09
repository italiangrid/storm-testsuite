__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import config
from tstorm.utils import createfile
from tstorm.utils import removefile

class UtilitiesTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn):
      super(UtilitiesTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn
    
    def test_settings(self):
      for x in self.tsets:
        self.assert_(x in ('general','ping'))
        for y in self.tsets[x]:
            self.assert_(x != '')

    def test_dd(self):
      self.dd_result = createfile.Dd(self.ifn).get_output()
      self.assert_(self.dd_result['status'] == 'PASS')

    def test_cr_lf(self):
      self.cf_result = createfile.Cf(self.ifn).get_output()
      self.assert_(self.cf_result['status'] == 'PASS')

    def test_rm_lf(self):
      self.rmlf_result = removefile.RmLf(self.ifn, self.bifn).get_output()
      self.assert_(self.rmlf_result['status'] == 'PASS')
