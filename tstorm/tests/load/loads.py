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

class LoadsTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, lfn):
        super(LoadsTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.lfn = lfn

    def test_storm_get_transfer_protocols(self):
        storm_protocol = protocol.StoRMGtp(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(storm_protocol.get_command())
        protocol_result = storm_protocol.get_output()
        self.assert_(protocol_result['status'] == 'PASS')
        self.assertEqual(len(protocol_result['transferProtocol']), 6)

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_ls_unexist_file(self):
        storm_ls = ls.StoRMLs(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ls.get_command())
        ls_result = storm_ls.get_output()
        self.assert_(ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_ls_unexist_dir(self):
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            storm_ls = ls.StoRMLs(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(storm_ls.get_command())
            ls_result = storm_ls.get_output()
            self.assert_(ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_ls_dir(self):
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            storm_ls = ls.StoRMLs(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(storm_ls.get_command())
            ls_result = storm_ls.get_output()
            self.assert_(ls_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_ls_file(self):
        storm_ls = ls.StoRMLs(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ls.get_command())
        ls_result = storm_ls.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        cksm_lf = cksm.CksmLf(self.ifn)
        cksm_result = cksm_lf.get_output()
        new_check_value = ls_result['checkSumValue'] + ' (' + ls_result['checkSumType'] + ')'
        self.assert_(new_check_value == cksm_result['Checksum'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_ls_fake_file(self):
        storm_ls = ls.StoRMLs(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ls.get_command())
        ls_result = storm_ls.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_mkdir(self):
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            #print self.dfn, a
            storm_mkdir = mkdir.StoRMMkdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)

            dtc=a.split('/')
            dtc=dtc[1:]
            y='/' 
            for x in dtc:
                if x != '':
                    self.lfn.put_cmd(storm_mkdir.get_command(y + x))
                    y = y + x + '/' 

            mkdir_result = storm_mkdir.get_output()
            #print mkdir_result
            for x in mkdir_result['status']:
                self.assert_(x == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_mkdir_exist_dir(self):
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            storm_mkdir = mkdir.StoRMMkdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)

            dtc=a.split('/')
            dtc=dtc[1:]
            y='/'
            for x in dtc:
                if x != '':
                    self.lfn.put_cmd(storm_mkdir.get_command(y + x))
                    y = y + x + '/'

            mkdir_result = storm_mkdir.get_output()
            for x in mkdir_result['status']:
                self.assert_(x == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_rm_file(self):
        storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_rm.get_command())
        rm_result = storm_rm.get_output()
        self.assert_(rm_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_rm_unexist_file(self):
        storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_rm.get_command())
        rm_result = storm_rm.get_output()
        self.assert_(rm_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_rm_dir(self):
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            storm_rmdir = rmdir.StoRMRmdir(self.tsets['general']['endpoint'],
                               self.tsets['general']['accesspoint'], a)

            y=a
            while y != '/':
                self.lfn.put_cmd(storm_rmdir.get_command(y))
                y=os.path.dirname(y)

            rmdir_result = storm_rmdir.get_output()
            for x in rmdir_result['status']:
                self.assert_(x == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_rm_unexist_dir(self):
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            storm_rmdir = rmdir.StoRMRmdir(self.tsets['general']['endpoint'],
                        self.tsets['general']['accesspoint'], a)

            y=a
            while y != '/':
                self.lfn.put_cmd(storm_rmdir.get_command(y))
                y=os.path.dirname(y)

            rmdir_result = storm_rmdir.get_output()
            for x in rmdir_result['status']:
                self.assert_(x == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_prepare_to_get(self):
        storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                    self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ptg.get_command())
        ptg_result = storm_ptg.get_output()
        self.assert_(ptg_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_prepare_to_get_unexist_file(self):
        storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                    self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ptg.get_command())
        ptg_result = storm_ptg.get_output()
        self.assert_(ptg_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_release_file(self):
        storm_ptg = cp.StoRMPtg(self.tsets['general']['endpoint'],
                    self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ptg.get_command())
        ptg_result = storm_ptg.get_output()
        self.assert_(ptg_result['status'] == 'PASS')

        storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn,
                   ptg_result['requestToken'])
        self.lfn.put_cmd(storm_rf.get_command())
        rf_result = storm_rf.get_output()
        self.assert_(rf_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_prepare_to_put(self):
        storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                    self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ptp.get_command())
        ptp_result = storm_ptp.get_output()
        self.assert_(ptp_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_prepare_to_put_exist_file(self):
        storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                    self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ptp.get_command())
        ptp_result = storm_ptp.get_output()
        self.assert_(ptp_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_put_done(self):
        storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                    self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(storm_ptp.get_command())
        ptp_result = storm_ptp.get_output()
        self.assert_(ptp_result['status'] == 'PASS')

        storm_pd = cp.StoRMPd(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn,
                   ptp_result['requestToken'])
        self.lfn.put_cmd(storm_pd.get_command())
        pd_result = storm_pd.get_output()
        self.assert_(pd_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
