__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ping
from tstorm.utils import ls
from tstorm.utils import mkdir
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import rmdir
from tstorm.utils import cksm

class FunctionalitiesTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn):
      super(FunctionalitiesTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn

    def test_dcache_ping(self):
      print '''\nBT 3.3.1\n'''
      self.ping_result = ping.SrmPing(self.tsets['general']['endpoint']).get_output()
      self.assert_(self.ping_result['status'] == 'PASS')
      self.assert_(self.ping_result['VersionInfo'] == self.tsets['ping']['versioninfo'])
      self.assert_(self.ping_result['backend_type'] == self.tsets['ping']['backend_type'])
      self.assert_(self.ping_result['backend_version'] == self.tsets['ping']['backend_version'])

    def test_storm_ping(self):
      print '''\nBT 3.3.1\n'''
      self.ping_result = ping.StoRMPing(self.tsets['general']['endpoint']).get_output()
      self.assert_(self.ping_result['status'] == 'PASS')
      self.assert_(self.ping_result['versionInfo'] == self.tsets['ping']['versioninfo'])
      for x in self.ping_result['key']:
        if x == 'backend_type':
          self.assert_(self.ping_result['value'][self.ping_result['key'].index(x)] == self.tsets['ping']['backend_type'])
        elif x == 'backend_version':
          self.assert_(self.ping_result['value'][self.ping_result['key'].index(x)] == self.tsets['ping']['backend_version'])

    def test_ls_unexist_file(self):
      print '''\nBT 3.3.2 unexistent file\n'''
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')

    def test_ls_unexist_dir(self):
      print '''\nBT 3.3.2 unexistent dir\n'''
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        self.assert_(self.ls_result['status'] == 'FAILURE')

    def test_mkdir_dir(self):
      print '''\nBT 3.3.4 normal workflow\n'''
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.mkdir_result = mkdir.SrmMkdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.mkdir_result['status']:
          self.assert_(x == 'PASS')

    def test_mkdir_exist_dir(self):
      print '''\nBT 3.3.4 existent file\n'''
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.mkdir_result = mkdir.SrmMkdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.mkdir_result['status']:
          self.assert_(x == 'FAILURE')

    def test_ls_dir(self):
      print '''\nBT 3.3.2 normal workflow\n'''
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        self.assert_(self.ls_result['status'] == 'PASS')

    def test_cp_bt(self):
      print '''\nBT 3.3.6 normal workflow\n'''
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')

    def test_ls_file(self):
      print '''\nBT 3.3.2 normal workflow\n'''
      self.lsat_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.lsat_result['status'] == 'PASS')
      self.lcksm_result = cksm.CksmLf(self.ifn).get_output()
      self.assert_(self.lsat_result['Checksum'] == self.lcksm_result['Checksum'])

    def test_cp_at(self):
      print '''\nBT 3.3.7 normal workflow\n'''
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output(False)
      self.assert_(self.cp_result['status'] == 'PASS')

    def test_rm_file(self):
      print '''\nBT 3.3.8 normal workflow\n'''
      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')

    def test_rm_unexist_file(self):
      print '''\nBT 3.3.8 unexistent file\n'''
      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'FAILURE')

    def test_rm_dir(self):
      print '''\nBT 3.3.5 normal workflow \n'''
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.SrmRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'PASS')

    def test_rm_unexist_dir(self):
      print '''\nBT 3.3.5 unexistent dir\n'''
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.SrmRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'FAILURE')

    def test_cksm(self):
      print '''\nBT 3.3.3 normal workflow\n'''
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.SrmRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'PASS')

    def test_data_transfer_out_file(self):
      print '''\nBT 3.3.6 normal workflow\n'''
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')

    def test_data_transfer_out_exist_file(self):
      print '''\nBT 3.3.6 existent file\n'''
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'FAILURE')

    def test_data_transfer_in_file(self):
      print '''\nBT 3.3.7 normal workflow\n'''  
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output(False)
      self.assert_(self.cp_result['status'] == 'PASS')

    def test_data_transfer_in_unexist_file(self):
      print '''\nBT 3.3.7 unexistent file\n'''
      t=datetime.datetime.now()
      ts=str(time.mktime(t.timetuple()))
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn+ts, self.bifn).get_output(False)
      self.assert_(self.cp_result['status'] == 'FAILURE')



