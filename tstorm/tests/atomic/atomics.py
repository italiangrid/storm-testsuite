__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
import inspect

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
        self.id = uid.get_id()
        self.lfn = lfn

    def test_dcache_ping(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:        
            srm_ping = ping.SrmPing(self.tsets['general']['endpoint'])
            self.lfn.put_cmd(srm_ping.get_command())
            ping_result = srm_ping.get_output()

            msg = 'dcache ping status' 
            self.assert_(ping_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong version info'
            self.assert_(ping_result['VersionInfo'] == self.tsets['ping']['versioninfo'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong backend type'
            self.assert_(ping_result['backend_type'] == self.tsets['ping']['backend_type'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong backend version'
            self.assert_(ping_result['backend_version'] == self.tsets['ping']['backend_version'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_storm_ping(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            storm_ping = ping.StoRMPing(self.tsets['general']['endpoint'])
            self.lfn.put_cmd(storm_ping.get_command())
            ping_result = storm_ping.get_output()

            msg = 'storm ping status'
            self.assert_(ping_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong version info'    
            self.assert_(ping_result['versionInfo'] == self.tsets['ping']['versioninfo'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            for x in ping_result['key']:
                if x == 'backend_type':
                    msg = 'Wrong backend type'
                    self.assert_(ping_result['value'][ping_result['key'].index(x)] == self.tsets['ping']['backend_type'],
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))
                elif x == 'backend_version':
                    msg = 'Wrong backend version'
                    self.assert_(ping_result['value'][ping_result['key'].index(x)] == self.tsets['ping']['backend_version'],
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_storm_ping_wo(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            storm_ping = ping.StoRMPing(self.tsets['general']['endpoint'])
            self.lfn.put_cmd(storm_ping.get_command(wrong_option=True))
            ping_result = storm_ping.get_output(wrong_option=True)

            msg = 'storm ping status'
            self.assert_(ping_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_storm_gtp(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            storm_protocol = protocol.StoRMGtp(self.tsets['general']['endpoint'])
            self.lfn.put_cmd(storm_protocol.get_command())
            protocol_result = storm_protocol.get_output()
            
            msg = 'storm gtp status'
            self.assert_(protocol_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'The number of supported protocols is not 6'
            self.assertEqual(len(protocol_result['transferProtocol']), 6,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_storm_gtp_wo(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            storm_protocol = protocol.StoRMGtp(self.tsets['general']['endpoint'])
            self.lfn.put_cmd(storm_protocol.get_command(wrong_option=True))
            protocol_result = storm_protocol.get_output(wrong_option=True)
            
            msg = 'storm gtp status'
            self.assert_(protocol_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_lcg_ls_unexist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_lcg_ls_unexist_dir(self):
        if '/' in self.dfn:
            stack_value = inspect.stack()[0]
            path = stack_value[1]
            method = stack_value[3]

            try:
                a=os.path.dirname(self.dfn)
                lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'], a)
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
  
                msg = 'lcg ls status'
                self.assert_(ls_result['status'] == 'FAILURE',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
            except AssertionError, err:
                print err
                self.lfn.put_result('FAILED')
            else:
                self.lfn.put_result('PASSED')

            self.lfn.flush_file()

    def test_dcache_mkdir(self):
        if '/' in self.dfn:
            stack_value = inspect.stack()[0]
            path = stack_value[1]
            method = stack_value[3]

            try:
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
  
                msg = 'dcache mkdir status'
                for x in mkdir_result['status']:
                    self.assert_(x == 'PASS',
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))
            except AssertionError, err:
                print err
                self.lfn.put_result('FAILED')
            else:
                self.lfn.put_result('PASSED')

            self.lfn.flush_file()

    def test_dcache_mkdir_exist_dir(self):
        if '/' in self.dfn:
            stack_value = inspect.stack()[0]
            path = stack_value[1]
            method = stack_value[3]

            try:
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
  
                msg = 'dcache mkdir status'
                for x in mkdir_result['status']:
                    self.assert_(x == 'FAILURE',
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))
            except AssertionError, err:
                print err
                self.lfn.put_result('FAILED')
            else:
                self.lfn.put_result('PASSED')

            self.lfn.flush_file()

    def test_lcg_ls_dir(self):
        if '/' in self.dfn:
            stack_value = inspect.stack()[0]
            path = stack_value[1]
            method = stack_value[3]

            try:
                a=os.path.dirname(self.dfn)
                lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'], a)
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()

                msg = 'lcg ls status'
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
            except AssertionError, err:
                print err
                self.lfn.put_result('FAILED')
            else:
                self.lfn.put_result('PASSED')

            self.lfn.flush_file()

    def test_lcg_cp_out(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command())
            cp_result = lcg_cp.get_output()

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_lcg_ls_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            cksm_lf = cksm.CksmLf(self.ifn)
            cksm_result = cksm_lf.get_output()

            msg = 'Wrong checksum'
            self.assert_(ls_result['Checksum'] == cksm_result['Checksum'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_lcg_cp_in(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command(False))
            cp_result = lcg_cp.get_output(False)

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_dcache_rm_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
            self.lfn.put_cmd(srm_rm.get_command())
            rm_result = srm_rm.get_output()

            msg = 'dcache rm status'
            self.assert_(rm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_dcache_rm_unexist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
            self.lfn.put_cmd(srm_rm.get_command())
            rm_result = srm_rm.get_output()
            
            msg = 'dcache rm status'
            self.assert_(rm_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_dcache_rm_dir(self):
        if '/' in self.dfn:
            stack_value = inspect.stack()[0]
            path = stack_value[1]
            method = stack_value[3]

            try:
                a=os.path.dirname(self.dfn)
                srm_rmdir = rmdir.SrmRmdir(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'], a)

                y=a
                while y != '/':
                    self.lfn.put_cmd(srm_rmdir.get_command(y))
                    y=os.path.dirname(y)

                rmdir_result = srm_rmdir.get_output()
                msg = 'dcache rm status'
                for x in rmdir_result['status']:
                    self.assert_(x == 'PASS',
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))
            except AssertionError, err:
                print err
                self.lfn.put_result('FAILED')
            else:
                self.lfn.put_result('PASSED')

            self.lfn.flush_file()

    def test_dcache_rm_unexist_dir(self):
        if '/' in self.dfn:
            stack_value = inspect.stack()[0]
            path = stack_value[1]
            method = stack_value[3]

            try:
                a=os.path.dirname(self.dfn)
                srm_rmdir = rmdir.SrmRmdir(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'], a)

                y=a
                while y != '/':
                    self.lfn.put_cmd(srm_rmdir.get_command(y))
                    y=os.path.dirname(y)

                rmdir_result = srm_rmdir.get_output()

                msg = 'dcache rm status'
                for x in rmdir_result['status']:
                    self.assert_(x == 'FAILURE',
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))
            except AssertionError, err:
                print err
                self.lfn.put_result('FAILED')
            else:
                self.lfn.put_result('PASSED')

            self.lfn.flush_file()
