#!/usr/bin/python

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
    def __init__(self, testname, tfn, ifn, dfn, bifn, lfn):
        super(FunctionalitiesTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.lfn = lfn

    def test_cksm(self):
        self.lfn.put_name('CKSUM')
        des = '''Verify that the checksum is calculated for the transferred 
file using the gsiftp protocol.'''
        self.lfn.put_description(des)
        self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'], 
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'FAILURE')

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn,
                 self.dfn, self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        cp_result = lcg_cp.get_output()
        self.assert_(cp_result['status'] == 'PASS')

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(srm_rm.get_command())
        rm_result = srm_rm.get_output()
        self.assert_(rm_result['status'] == 'PASS')
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

    def test_data_transfer_out_file(self):
        self.lfn.put_name('DATA TRANSFER OUT')
        self.lfn.put_description('Verify that the file has been transferred')
        self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'FAILURE')

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        cp_result = lcg_cp.get_output()
        self.assert_(cp_result['status'] == 'PASS')

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_data_transfer_out_exist_file(self):
        self.lfn.put_name('DATA TRANSFER OUT')
        des = '''Verify that the file has not been transferred because it 
already exists.'''
        self.lfn.put_description(des)
        self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        cp_result = lcg_cp.get_output()
        self.assert_(cp_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_data_transfer_in_file(self):
        self.lfn.put_name('DATA TRANSFER IN')
        des = '''Verify that the file has been transferred back.'''
        self.lfn.put_description(des)
        self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        cp_result = lcg_cp.get_output(False)
        self.assert_(cp_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_data_transfer_in_unexist_file(self):
        self.lfn.put_name('DATA TRANSFER IN')
        des = '''Verify that the file has not been transferred back because it
does not exit.'''
        self.lfn.put_description(des)
        self.lfn.put_uid('')
        self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        t=datetime.datetime.now()
        ts=str(time.mktime(t.timetuple()))
        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ls_result = lcg_ls.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn+ts,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        cp_result = lcg_cp.get_output(False)
        self.assert_(cp_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
