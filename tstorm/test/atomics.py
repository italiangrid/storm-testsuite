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

class AtomicsTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, lfn):
        super(FunctionalitiesTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.lfn = lfn

    def test_dcache_ping(self):
        self.lfn.put_name('SRM PING')
        self.lfn.put_description('Verify ping operation')
        self.lfn.put_uid('')
        self.lfn.put_output()

        ping = ping.SrmPing(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(ping.get_command())
        self.ping_result = ping.get_output()
        self.assert_(self.ping_result['status'] == 'PASS')
        self.assert_(self.ping_result['VersionInfo'] == self.tsets['ping']['versioninfo'])
        self.assert_(self.ping_result['backend_type'] == self.tsets['ping']['backend_type'])
        self.assert_(self.ping_result['backend_version'] == self.tsets['ping']['backend_version'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_ping(self):
        self.lfn.put_name('SRM PING')
        self.lfn.put_description('Verify ping operation')
        self.lfn.put_uid('')
        self.lfn.put_output()

        ping = ping.StoRMPing(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(ping.get_command())
        self.ping_result = ping.get_output()
        self.assert_(self.ping_result['status'] == 'PASS')
        self.assert_(self.ping_result['versionInfo'] == self.tsets['ping']['versioninfo'])
        for x in self.ping_result['key']:
            if x == 'backend_type':
                self.assert_(self.ping_result['value'][self.ping_result['key'].index(x)] == self.tsets['ping']['backend_type'])
            elif x == 'backend_version':
                self.assert_(self.ping_result['value'][self.ping_result['key'].index(x)] == self.tsets['ping']['backend_version'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_ls_unexist_file(self):
        self.lfn.put_name('SRM LS')
        des = 'Verify ls operation on a file that does not exist'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.ls_result = lcg_ls.get_output()
        self.assert_(self.ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_ls_unexist_dir(self):
        self.lfn.put_name('SRM LS')
        des = 'Verify ls operation on a directory that does not exist'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(lcg_ls.get_command())
            self.ls_result = lcg_ls.get_output()
            self.assert_(self.ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_mkdir_dir(self):
        self.lfn.put_name('SRM MKDIR')
        des = 'Verify mkdir operation on a directory'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            srm_mkdir = mkdir.SrmMkdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(srm_mkdir.get_command())
            self.mkdir_result = srm_mkdir.get_output()
            for x in self.mkdir_result['status']:
                self.assert_(x == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_mkdir_exist_dir(self):
        self.lfn.put_name('SRM MKDIR')
        des = 'Verify mkdir operation on a directory that already exists'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            srm_mkdir = mkdir.SrmMkdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(srm_mkdir.get_command())
            self.mkdir_result = srm_mkdir.get_output()
            for x in self.mkdir_result['status']:
                self.assert_(x == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_ls_dir(self):
        self.lfn.put_name('SRM LS')
        des = 'Verify ls operation on a directory that exists'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(lcg_ls.get_command())
            self.ls_result = lcg_ls.get_output()
            self.assert_(self.ls_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_cp_bt(self):
        self.lfn.put_name('SRM CP')
        des = 'Verify cp operation of a given file on a given storage'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        self.cp_result = lcg_cp.get_output()
        self.assert_(self.cp_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_ls_file(self):
        self.lfn.put_name('SRM LS')
        des = 'Verify ls operation on a file that exists'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.ls_result = lcg_ls.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')

        cksm_lf = cksm.CksmLf(self.ifn)
        self.lfn.put_cmd(cksm_lf.get_command())
        self.cksm_result = cksm_lf.get_output()
        self.assert_(self.ls_result['Checksum'] == self.cksm_result['Checksum'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_cp_at(self):
        self.lfn.put_name('SRM CP')
        des = 'Verify cp operation of a given file locally'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        self.cp_result = lcg_cp.get_output(False)
        self.assert_(self.cp_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_file(self):
        self.lfn.put_name('SRM RM')
        des = 'Verify rm operation of a given file'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(srm_rm.get_command())
        self.rm_result = srm_rm.get_output()
        self.assert_(self.rm_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_unexist_file(self):
        self.lfn.put_name('SRM RM')
        des = 'Verify rm operation of a file that does not exist'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(srm_rm.get_command())
        self.rm_result = srm_rm.get_output()
        self.assert_(self.rm_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_dir(self):
        self.lfn.put_name('SRM RMDIR')
        des = 'Verify rmdir operation of a given directory'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            srm_rmdir_result = rmdir.SrmRmdir(self.tsets['general']['endpoint'],
                               self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(srm_rmdir.get_command())
            self.rmdir_result = srm_rmdir.get_output()
            for x in self.rmdir_result['status']:
                self.assert_(x == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_unexist_dir(self):
        self.lfn.put_name('SRM RMDIR')
        des = 'Verify rmdir operation of a directory that does not exist'
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            srm_rmdir = rmdir.SrmRmdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(srm_rmdir.get_command())
            self.rmdir_result = srm_rmdir.get_output()
            for x in self.rmdir_result['status']:
                self.assert_(x == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()