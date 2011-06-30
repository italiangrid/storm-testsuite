__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ping
from tstorm.utils import ls
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import bringonline as bol

class TapeTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn):
      super(TapeTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn

    def test_verify_tsa1(self):
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result
     
      self.bol_result = bol.LcgBol(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output() 
      self.assert_(self.bol_result['status'] == 'PASS')
      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn, self.bol_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS') 

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')

    def test_verify_tsa2(self):
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.lsa_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.bol_result = bol.SrmBol(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.bol_result['status'] == 'PASS')
      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn, self.bol_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')

    def test_verify_tsa3(self):
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.lsa_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.bol_result = bol.SrmBol(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.bol_result['status'] == 'PASS')
      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn, self.bol_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')

      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      while self.ls_result['fileLocality'] != 'NEARLINE':
        self.ls_result = ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        print self.ls_result

      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      self.ls_result = ls.get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
