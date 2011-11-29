#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
import time
from tstorm.utils import config
from tstorm.utils import ping
from tstorm.utils import ls
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import space
from tstorm.utils import bringonline as bol

class TapeTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn):
      super(TapeTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn

    def test_verify_tsa1(self):
      ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn)
      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'ONLINE':
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'ONLINE_AND_NEARLINE':
        time.sleep(5)
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'NEARLINE':
        time.sleep(5)
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll     
      self.bol_result = bol.LcgBol(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output() 
      self.assert_(self.bol_result['status'] == 'PASS')

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'ONLINE_AND_NEARLINE':
        time.sleep(5)
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll
      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn, self.bol_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS') 

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'NEARLINE':
        time.sleep(5)
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll

      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'FAILURE')

    def test_verify_tsa2(self):
      ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn)
      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'ONLINE':
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'ONLINE_AND_NEARLINE':
        time.sleep(5)
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'NEARLINE':
        time.sleep(5)
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll
      self.bol_result = bol.LcgBol(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.bol_result['status'] == 'PASS')

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'ONLINE_AND_NEARLINE':
        time.sleep(5)
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll

      st_result = space.StoRMGst(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.tsets['tape']['spacetoken'])
      stb = st_result.get_output()
      self.assert_(stb['status'] == 'PASS')
      us_result = space.StoRMGsm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], st_result['arrayOfSpaceTokens'])
      usb = us_result.get_output()
      self.assert_(usb['status'] == 'PASS')

      self.lls_result = ls.Ls(self.ifn).get_output()
      self.assert_(self.lls_result['status'] == 'PASS')

      self.rf_result = cp.StoRMRf(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn, self.bol_result['requestToken']).get_output()
      self.assert_(self.rf_result['status'] == 'PASS')

      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'PASS')
      while ll['fileLocality'] != 'NEARLINE':
        time.sleep(5)
        ll = ls_result.get_output()
        self.assert_(ll['status'] == 'PASS')

      print ll

      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['tape']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      ll = ls_result.get_output()
      self.assert_(ll['status'] == 'FAILURE')

      sta = st_result.get_output()
      self.assert_(sta['status'] == 'PASS')
      usa = us_result.get_output()
      self.assert_(usa['status'] == 'PASS')
      print self.lls_result['size'], usb['unusedSize'], usa['unusedSize']
      self.assert_(int(self.lls_result['size']) == int(usb['unusedSize']) - int(usa['unusedSize']))
