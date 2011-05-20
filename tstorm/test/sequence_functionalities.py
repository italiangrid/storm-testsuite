import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ping
from tstorm.utils import createfile
from tstorm.utils import removefile
from tstorm.utils import ls
from tstorm.utils import mkdir
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import rmdir
from tstorm.utils import cksm

class SequenceFunctionalities(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn):
      super(SequenceFunctionalities, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.ifn = ifn
      self.dfn = dfn
      self.bifn = bifn
    
    def test_settings(self):
      for x in self.tsets:
        self.assert_(x in ('general','ping'))
        for y in self.tsets[x]:
            self.assert_(x != '')

    def test_ping(self):
      self.ping_result = ping.SrmPing(self.tsets['general']['endpoint']).get_output()
      self.assert_(self.ping_result['status'] == 'PASS')
      self.assert_(self.ping_result['VersionInfo'] == self.tsets['ping']['versioninfo'])
      self.assert_(self.ping_result['backend_type'] == self.tsets['ping']['backend_type'])
      self.assert_(self.ping_result['backend_version'] == self.tsets['ping']['backend_version'])

    def test_dd(self):
      self.dd_result = createfile.Dd(self.ifn).get_output()
      self.assert_(self.dd_result['status'] == 'PASS')

    def test_ls_bt(self):
      self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.ls_result['status'] == 'FAILURE')
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        self.assert_(self.ls_result['status'] == 'FAILURE')

    def test_mkdir_bc(self):
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.mkdir_result = mkdir.SrmMkdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.mkdir_result['status']:
          self.assert_(x == 'PASS')

    def test_mkdir_ac(self):
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.mkdir_result = mkdir.SrmMkdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.mkdir_result['status']:
          self.assert_(x == 'FAILURE')

    def test_ls_ac(self):
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.ls_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        self.assert_(self.ls_result['status'] == 'PASS')

    def test_cp_bt(self):
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output()
      self.assert_(self.cp_result['status'] == 'PASS')

    def test_ls_at(self):
      self.lsat_result = ls.LcgLs(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.lsat_result['status'] == 'PASS')
      self.lcksm_result = cksm.CksmLf(self.ifn).get_output()
      self.assert_(self.lsat_result['Checksum'] == self.lcksm_result['Checksum'])

    def test_cp_at(self):
      self.cp_result = cp.LcgCp(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.ifn, self.dfn, self.bifn).get_output(False)
      self.assert_(self.cp_result['status'] == 'PASS')

    def test_rm(self):
      self.rm_result = rm.SrmRm(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], self.dfn).get_output()
      self.assert_(self.rm_result['status'] == 'PASS')

    def test_rmdir(self):
      if '/' in self.dfn:
        a=os.path.dirname(self.dfn)
        self.rmdir_result = rmdir.SrmRmdir(self.tsets['general']['endpoint'], self.tsets['general']['accesspoint'], a).get_output()
        for x in self.rmdir_result['status']:
          self.assert_(x == 'PASS')

    def test_rm_lf(self):
      self.rmlf_result = removefile.RmLf(self.ifn, self.bifn).get_output()
      print self.rmlf_result
      self.assert_(self.rmlf_result['status'] == 'PASS')
