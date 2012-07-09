__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest

from tstorm.utils import config
from tstorm.commands import ping
from tstorm.commands import protocol
from tstorm.commands import ls
from tstorm.commands import mkdir
from tstorm.commands import cp
from tstorm.commands import rm
from tstorm.commands import rmdir
from tstorm.utils import cksm
from tstorm.utils import utils

class AtomicsTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, uid, lfn):
        super(AtomicsTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.uid = uid
        self.lfn = lfn

    def test_dcache_ping(self):
        self.lfn.put_name(self.uid['test_dcache_ping'][6])
        self.lfn.put_description(self.uid['test_dcache_ping'][7])
        if self.uid.has_key('test_dcache_ping'):
            self.lfn.put_uuid(self.uid['test_dcache_ping'][0])
        else:
            print 'ADD UID for test_dcache_ping'
            self.lfn.put_uuid(utils.get_uuid())        
        self.lfn.put_uid('')
        self.lfn.put_output()

        srm_ping = ping.SrmPing(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(srm_ping.get_command())
        ping_result = srm_ping.get_output()
        self.assert_(ping_result['status'] == 'PASS')
        self.assert_(ping_result['VersionInfo'] == self.tsets['ping']['versioninfo'])
        self.assert_(ping_result['backend_type'] == self.tsets['ping']['backend_type'])
        self.assert_(ping_result['backend_version'] == self.tsets['ping']['backend_version'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_ping(self):
        self.lfn.put_name(self.uid['test_storm_ping'][6])
        self.lfn.put_description(self.uid['test_storm_ping'][7])
        if self.uid.has_key('test_storm_ping'):
            self.lfn.put_uuid(self.uid['test_storm_ping'][0])
        else:
            print 'ADD UID for test_storm_ping'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        storm_ping = ping.StoRMPing(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(storm_ping.get_command())
        ping_result = storm_ping.get_output()
        self.assert_(ping_result['status'] == 'PASS')
        self.assert_(ping_result['versionInfo'] == self.tsets['ping']['versioninfo'])
        for x in ping_result['key']:
            if x == 'backend_type':
                self.assert_(ping_result['value'][ping_result['key'].index(x)] == self.tsets['ping']['backend_type'])
            elif x == 'backend_version':
                self.assert_(ping_result['value'][ping_result['key'].index(x)] == self.tsets['ping']['backend_version'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_ping_wo(self):
        self.lfn.put_name(self.uid['test_storm_ping_wo'][6])
        self.lfn.put_description(self.uid['test_storm_ping_wo'][7])
        if self.uid.has_key('test_storm_ping_wo'):
            self.lfn.put_uuid(self.uid['test_storm_ping_wo'][0])
        else:
            print 'ADD UID for test_storm_ping_wo'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        storm_ping = ping.StoRMPing(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(storm_ping.get_command(wrong_option=True))
        ping_result = storm_ping.get_output(wrong_option=True)
        self.assert_(ping_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_gtp(self):
        self.lfn.put_name(self.uid['test_storm_gtp'][6])
        self.lfn.put_description(self.uid['test_storm_gtp'][7])
        if self.uid.has_key('test_storm_gtp'):
            self.lfn.put_uuid(self.uid['test_storm_gtp'][0])
        else:
            print 'ADD UID for test_storm_gtp'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        storm_protocol = protocol.StoRMGtp(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(storm_protocol.get_command())
        protocol_result = storm_protocol.get_output()
        self.assert_(protocol_result['status'] == 'PASS')
        self.assertEqual(len(protocol_result['transferProtocol']), 6)

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_gtp_wo(self):
        self.lfn.put_name(self.uid['test_storm_gtp_wo'][6])
        self.lfn.put_description(self.uid['test_storm_gtp_wo'][7])
        if self.uid.has_key('test_storm_gtp_wo'):
            self.lfn.put_uuid(self.uid['test_storm_gtp_wo'][0])
        else:
            print 'ADD UID for test_storm_gtp_wo'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        storm_protocol = protocol.StoRMGtp(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(storm_protocol.get_command(wrong_option=True))
        protocol_result = storm_protocol.get_output(wrong_option=True)
        self.assert_(protocol_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_ls_unexist_file(self):
        self.lfn.put_name(self.uid['test_ls_unexist_file'][6])
        self.lfn.put_description(self.uid['test_ls_unexist_file'][7])
        if self.uid.has_key('test_ls_unexist_file'):
            self.lfn.put_uuid(self.uid['test_ls_unexist_file'][0])
        else:
            print 'ADD UID for test_ls_unexist_file'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_ls_unexist_dir(self):
        self.lfn.put_name(self.uid['test_ls_unexist_dir'][6])
        self.lfn.put_description(self.uid['test_ls_unexist_dir'][7])
        if self.uid.has_key('test_ls_unexist_dir'):
            self.lfn.put_uuid(self.uid['test_ls_unexist_dir'][0])
        else:
            print 'ADD UID for test_ls_unexist_dir'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            self.assert_(ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_mkdir_dir(self):
        self.lfn.put_name(self.uid['test_mkdir_dir'][6])
        self.lfn.put_description(self.uid['test_mkdir_dir'][7])
        if self.uid.has_key('test_mkdir_dir'):
            self.lfn.put_uuid(self.uid['test_mkdir_dir'][0])
        else:
            print 'ADD UID for test_mkdir_dir'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            srm_mkdir = mkdir.SrmMkdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)

            dtc=a.split('/')
            dtc=dtc[1:]
            y='/' 
            for x in dtc:
                if x != '':
                    self.lfn.put_cmd(srm_mkdir.get_command(y + x))
                    y = y + x + '/' 

            mkdir_result = srm_mkdir.get_output()
            for x in mkdir_result['status']:
                self.assert_(x == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_mkdir_exist_dir(self):
        self.lfn.put_name(self.uid['test_mkdir_exist_dir'][6])
        self.lfn.put_description(self.uid['test_mkdir_exist_dir'][7])
        if self.uid.has_key('test_mkdir_exist_dir'):
            self.lfn.put_uuid(self.uid['test_mkdir_exist_dir'][0])
        else:
            print 'ADD UID for test_mkdir_exist_dir'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            srm_mkdir = mkdir.SrmMkdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)

            dtc=a.split('/')
            dtc=dtc[1:]
            y='/'
            for x in dtc:
                if x != '':
                    self.lfn.put_cmd(srm_mkdir.get_command(y + x))
                    y = y + x + '/'

            mkdir_result = srm_mkdir.get_output()
            for x in mkdir_result['status']:
                self.assert_(x == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_ls_dir(self):
        self.lfn.put_name(self.uid['test_ls_dir'][6])
        self.lfn.put_description(self.uid['test_ls_dir'][7])
        if self.uid.has_key('test_ls_dir'):
            self.lfn.put_uuid(self.uid['test_ls_dir'][0])
        else:
            print 'ADD UID for test_ls_dir'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            self.assert_(ls_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_cp_bt(self):
        self.lfn.put_name(self.uid['test_cp_bt'][6])
        self.lfn.put_description(self.uid['test_cp_bt'][7])
        if self.uid.has_key('test_cp_bt'):
            self.lfn.put_uuid(self.uid['test_cp_bt'][0])
        else:
            print 'ADD UID for test_cp_bt'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        cp_result = lcg_cp.get_output()
        self.assert_(cp_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_ls_file(self):
        self.lfn.put_name(self.uid['test_ls_file'][6])
        self.lfn.put_description(self.uid['test_ls_file'][7])
        if self.uid.has_key('test_ls_file'):
            self.lfn.put_uuid(self.uid['test_ls_file'][0])
        else:
            print 'ADD UID for test_ls_file'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        cksm_lf = cksm.CksmLf(self.ifn)
        cksm_result = cksm_lf.get_output()
        self.assert_(ls_result['Checksum'] == cksm_result['Checksum'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_cp_at(self):
        self.lfn.put_name(self.uid['test_cp_at'][6])
        self.lfn.put_description(self.uid['test_cp_at'][7])
        if self.uid.has_key('test_cp_at'):
            self.lfn.put_uuid(self.uid['test_cp_at'][0])
        else:
            print 'ADD UID for test_cp_at'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        cp_result = lcg_cp.get_output(False)
        self.assert_(cp_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_file(self):
        self.lfn.put_name(self.uid['test_rm_file'][6])
        self.lfn.put_description(self.uid['test_rm_file'][7])
        if self.uid.has_key('test_rm_file'):
            self.lfn.put_uuid(self.uid['test_rm_file'][0])
        else:
            print 'ADD UID for test_rm_file'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(srm_rm.get_command())
        rm_result = srm_rm.get_output()
        self.assert_(rm_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_unexist_file(self):
        self.lfn.put_name(self.uid['test_rm_unexist_file'][6])
        self.lfn.put_description(self.uid['test_rm_unexist_file'][7])
        if self.uid.has_key('test_rm_unexist_file'):
            self.lfn.put_uuid(self.uid['test_rm_unexist_file'][0])
        else:
            print 'ADD UID for test_rm_unexist_file'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(srm_rm.get_command())
        rm_result = srm_rm.get_output()
        self.assert_(rm_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_dir(self):
        self.lfn.put_name(self.uid['test_rm_dir'][6])
        self.lfn.put_description(self.uid['test_rm_dir'][7])
        if self.uid.has_key('test_rm_dir'):
            self.lfn.put_uuid(self.uid['test_rm_dir'][0])
        else:
            print 'ADD UID for test_rm_dir'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            srm_rmdir = rmdir.SrmRmdir(self.tsets['general']['endpoint'],
                               self.tsets['general']['accesspoint'], a)

            y=a
            while y != '/':
                self.lfn.put_cmd(srm_rmdir.get_command(y))
                y=os.path.dirname(y)

            rmdir_result = srm_rmdir.get_output()
            for x in rmdir_result['status']:
                self.assert_(x == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_unexist_dir(self):
        self.lfn.put_name(self.uid['test_rm_unexist_dir'][6])
        self.lfn.put_description(self.uid['test_rm_unexist_dir'][7])
        if self.uid.has_key('test_rm_unexist_dir'):
            self.lfn.put_uuid(self.uid['test_rm_unexist_dir'][0])
        else:
            print 'ADD UID for test_rm_unexist_dir'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            srm_rmdir = rmdir.SrmRmdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)

            y=a
            while y != '/':
                self.lfn.put_cmd(srm_rmdir.get_command(y))
                y=os.path.dirname(y)

            rmdir_result = srm_rmdir.get_output()
            for x in rmdir_result['status']:
                self.assert_(x == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
