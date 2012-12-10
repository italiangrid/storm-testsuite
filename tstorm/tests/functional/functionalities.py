__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest

from tstorm.utils import config
from tstorm.commands import ping
from tstorm.commands import ls
from tstorm.commands import mkdir
from tstorm.commands import cp
from tstorm.commands import rm
from tstorm.commands import rmdir
from tstorm.utils import cksm

class FunctionalitiesTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, uid, lfn):
        super(FunctionalitiesTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.id = uid.get_id()
        self.lfn = lfn

    def test_cksm(self):
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

            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.ifn,
                self.dfn, self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command())
            cp_result = lcg_cp.get_output()

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.dfn)
            self.lfn.put_cmd(srm_rm.get_command())
            rm_result = srm_rm.get_output()

            msg = 'dcache rm status'
            self.assert_(rm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            if '/' in self.dfn:
                a=os.path.dirname(self.dfn)
                srm_rmdir = rmdir.SrmRmdir(self.tsets['general']['endpoint'],
                    self.tsets['general']['accesspoint'], a)

                y=a
                while y != '/':
                    self.lfn.put_cmd(srm_rmdir.get_command(y))
                    y=os.path.dirname(y)

                rmdir_result = srm_rmdir.get_output()

                msg = 'dcache rmdir status'
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

    def test_data_transfer_out_file(self):
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

            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command())
            cp_result = lcg_cp.get_output()

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.dfn)
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

    def test_data_transfer_out_exist_file(self):
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

            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command())
            cp_result = lcg_cp.get_output()

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_data_transfer_in_file(self):
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

    def test_data_transfer_in_unexist_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
        #t=datetime.datetime.now()
        #ts=str(time.mktime(t.timetuple()))
        #lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
        #         self.tsets['general']['accesspoint'], self.dfn)
        #self.lfn.put_cmd(lcg_ls.get_command())
        #ls_result = lcg_ls.get_output()
        #self.assert_(ls_result['status'] == 'PASS')

            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command(False))
            cp_result = lcg_cp.get_output(False)

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
