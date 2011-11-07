__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import config
from tstorm.utils import createfile
from tstorm.utils import removefile

class UtilitiesTest(unittest.TestCase):
    def __init__(self, testname, tfn, lfn, ifn, dfn, bifn):
      super(UtilitiesTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn
      self.lfn = lfn
    
    def test_settings(self):
      '''Verify configuration ini file'''
      print '''\nCT Verify ini file\n'''
      for x in self.tsets:
        self.assert_(x in ('general','ping','https','http','tape','bdii','yaim','log'))
        for y in self.tsets[x]:
            self.assert_(x != '')

    def test_dd(self):
      '''Verify creation of a file with size 1M'''
      print '''\nTSTORMT Verify creation of a file with size 1M\n'''
      self.dd_result = createfile.Dd(self.lfn, self.ifn).get_output()
      self.assert_(self.dd_result['status'] == 'PASS')

    def test_cr_lf(self):
      '''Verify creation of a file with a char'''
      print '''\nTSTORMT Verify creation of a file with a char\n'''
      self.cf_result = createfile.Cf(self.lfn, self.ifn).get_output()
      self.assert_(self.cf_result['status'] == 'PASS')

    def test_rm_lf(self):
      '''Verify deletion of a local file'''
      print '''\nTSTORMT Verify deletion of a local file\n'''
      self.rmlf_result = removefile.RmLf(self.lfn, self.ifn, self.bifn).get_output()
      self.assert_(self.rmlf_result['status'] == 'PASS')
