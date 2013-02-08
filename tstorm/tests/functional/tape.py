__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
import time
import inspect

from tstorm.utils import config
from tstorm.commands import ping
from tstorm.commands import ls
from tstorm.commands import cp
from tstorm.commands import rm
from tstorm.commands import space
from tstorm.commands import bringonline

class TapeTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, uid, lfn):
        super(TapeTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.id = uid.get_id()
        self.lfn = lfn

    def test_access_tape_lcg(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.ifn, self.dfn,
                self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command())
            cp_result = lcg_cp.get_output()

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result

            lcg_bol = bol.LcgBol(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_bol.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg bol status'
            self.assert_(bol_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result

            storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn,
                bol_result['requestToken'])
            self.lfn.put_cmd(storm_rf.get_command())
            rf_result = storm_rf.get_output()

            msg = 'storm rf status'
            self.assert_(rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #ls_result = lcg_ls.get_output()
            #msg = 'lcg ls status'
            #self.assert_(ls_result['status'] == 'PASS',
            #    '%s, %s - FAILED, %s, Test ID %s' %
            #    (path, method, msg, self.id))
            #while ls_result['fileLocality'] != 'NEARLINE':
            #    ls_result = lcg_ls.get_output()
            #    self.assert_(ls_result['status'] == 'PASS',
            #        '%s, %s - FAILED, %s, Test ID %s' %
            #        (path, method, msg, self.id))

            #print ls_result

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

    def test_access_tape_storm(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.ifn, self.dfn,
                self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command())
            cp_result = lcg_cp.get_output()

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result

            lcg_bol = bol.StoRMBol(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_bol.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg bol status'
            self.assert_(bol_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result

            storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn,
                bol_result['requestToken'])
            self.lfn.put_cmd(storm_rf.get_command())
            rf_result = storm_rf.get_output()

            msg = 'storm rf status'
            self.assert_(rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #ls_result = lcg_ls.get_output()
            #msg = 'lcg ls status'
            #self.assert_(ls_result['status'] == 'PASS',
            #    '%s, %s - FAILED, %s, Test ID %s' %
            #    (path, method, msg, self.id)))
            #while ls_result['fileLocality'] != 'NEARLINE':
            #    ls_result = lcg_ls.get_output()
            #    self.assert_(ls_result['status'] == 'PASS',
            #        '%s, %s - FAILED, %s, Test ID %s' %
            #        (path, method, msg, self.id)))

            #print ls_result

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

    def test_verify_tsa2(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.ifn, self.dfn,
                self.bifn)
            self.lfn.put_cmd(lcg_cp.get_command())
            cp_result = lcg_cp.get_output()

            msg = 'lcg cp status'
            self.assert_(cp_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result 

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result

            lcg_bol = bol.StoRMBol(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_bol.get_command())
            ls_result = lcg_ls.get_output()

            msg = 'lcg bol status'
            self.assert_(bol_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            print ls_result

            storm_gst = space.StoRMGst(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'],
                self.tsets['tape']['spacetoken'])
            self.lfn.put_cmd(storm_gst.get_command())
            st_result = storm_gst.get_output()

            msg = 'storm gst status'
            self.assert_(st_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_gsm = space.StoRMGsm(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'],
                st_result['arrayOfSpaceTokens'])
            self.lfn.put_cmd(storm_gsm.get_command())
            sm_result = storm_gsm.get_output()

            msg = 'storm gsm status'
            self.assert_(sm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn,
                bol_result['requestToken'])
            self.lfn.put_cmd(storm_rf.get_command())
            rf_result = storm_rf.get_output()

            msg = 'storm rf status'
            self.assert_(rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #ls_result = lcg_ls.get_output()
            #msg = 'lcg ls status'
            #self.assert_(ls_result['status'] == 'PASS',
            #    '%s, %s - FAILED, %s, Test ID %s' %
            #    (path, method, msg, self.id))
            #while ls_result['fileLocality'] != 'NEARLINE':
            #    ls_result = lcg_ls.get_output()
            #    self.assert_(ls_result['status'] == 'PASS',
            #        '%s, %s - FAILED, %s, Test ID %s' %
            #        (path, method, msg, self.id))

            #print ls_result

            srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.dfn)
            self.lfn.put_cmd(srm_rm.get_command())
            rm_result = srm_rm.get_output()

            msg = 'dcache rm status'
            self.assert_(rm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            print ls_result

            st_result = storm_gst.get_output()
            msg = 'storm gst status'
            self.assert_(st_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            sm_result = storm_gsm.get_output()
            msg = 'storm gsm status'
            self.assert_(sm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            print ls_result['size'], st_result['unusedSize'], sm_result['unusedSize']
            self.assert_(int(ls_result['size']) == int(sm_result['unusedSize']) - int(st_result['unusedSize']))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
