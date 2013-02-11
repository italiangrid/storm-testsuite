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

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

            lcg_bol = bringonline.LcgBol(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_bol.get_command())
            bol_result = lcg_bol.get_output()

            msg = 'lcg bol status'
            self.assert_(bol_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

            storm_rf = cp.StoRMRf(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn,
                bol_result['requestToken'])
            self.lfn.put_cmd(storm_rf.get_command())
            rf_result = storm_rf.get_output()

            msg = 'storm rf status'
            self.assert_(rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #self.lfn.put_cmd(lcg_ls.get_command())
            #ls_result = lcg_ls.get_output()
            #msg = 'lcg ls status'
            #self.assert_(ls_result['status'] == 'PASS',
            #    '%s, %s - FAILED, %s, Test ID %s' %
            #    (path, method, msg, self.id))
            #while ls_result['fileLocality'] != 'NEARLINE':
            #    self.lfn.put_cmd(lcg_ls.get_command())
            #    ls_result = lcg_ls.get_output()
            #    self.assert_(ls_result['status'] == 'PASS',
            #        '%s, %s - FAILED, %s, Test ID %s' %
            #        (path, method, msg, self.id))


            #srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
            #    self.tsets['general']['accesspoint'], self.dfn)
            #self.lfn.put_cmd(srm_rm.get_command())
            #rm_result = srm_rm.get_output()

            #msg = 'dcache rm status'
            #self.assert_(rm_result['status'] == 'PASS',
            #    '%s, %s - FAILED, %s, Test ID %s' %
            #    (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        except KeyError, err:
            self.lfn.put_result('TAPE NOT SUPPORTED')
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

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

            lcg1_bol = bringonline.StoRMBol(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg1_bol.get_command())
            bol1_result = lcg1_bol.get_output()

            msg = 'lcg bol1 status'
            self.assert_(bol1_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcg2_bol = bringonline.StoRMBol(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg2_bol.get_command())
            bol2_result = lcg2_bol.get_output()

            msg = 'lcg bol2 status'
            self.assert_(bol2_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

            #self.lfn.put_cmd(lcg_ls.get_command())
            #ls_result = lcg_ls.get_output()
            #msg = 'lcg ls status'
            #self.assert_(ls_result['status'] == 'PASS',
            #    '%s, %s - FAILED, %s, Test ID %s' %
            #    (path, method, msg, self.id)))
            #while ls_result['fileLocality'] != 'NEARLINE':
            #    self.lfn.put_cmd(lcg_ls.get_command())
            #    ls_result = lcg_ls.get_output()
            #    self.assert_(ls_result['status'] == 'PASS',
            #        '%s, %s - FAILED, %s, Test ID %s' %
            #        (path, method, msg, self.id)))

            #print ls_result

            storm_rf1 = cp.StoRMRf(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn,
                bol1_result['requestToken'])
            self.lfn.put_cmd(storm_rf1.get_command())
            rf1_result = storm_rf1.get_output()

            msg = 'storm rf1 status'
            self.assert_(rf1_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            storm_rf2 = cp.StoRMRf(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn,
                bol2_result['requestToken'])
            self.lfn.put_cmd(storm_rf2.get_command())
            rf2_result = storm_rf2.get_output()

            msg = 'storm rf2 status'
            self.assert_(rf2_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
            #    self.tsets['general']['accesspoint'], self.dfn)
            #self.lfn.put_cmd(srm_rm.get_command())
            #rm_result = srm_rm.get_output()

            #msg = 'dcache rm status'
            #self.assert_(rm_result['status'] == 'PASS',
            #    '%s, %s - FAILED, %s, Test ID %s' %
            #    (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        except KeyError, err:
            self.lfn.put_result('TAPE NOT SUPPORTED')
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

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

            lcg_bol = bringonline.StoRMBol(self.tsets['general']['endpoint'],
                self.tsets['tape']['accesspoint'], self.dfn)
            self.lfn.put_cmd(lcg_bol.get_command())
            bol_result = lcg_bol.get_output()

            msg = 'lcg bol status'
            self.assert_(bol_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            while ls_result['fileLocality'] != 'ONLINE_AND_NEARLINE':
                self.lfn.put_cmd(lcg_ls.get_command())
                ls_result = lcg_ls.get_output()
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            self.lfn.flush_file()

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

            #self.lfn.put_cmd(lcg_ls.get_command())
            #ls_result = lcg_ls.get_output()
            #msg = 'lcg ls status'
            #self.assert_(ls_result['status'] == 'PASS',
            #    '%s, %s - FAILED, %s, Test ID %s' %
            #    (path, method, msg, self.id))
            #while ls_result['fileLocality'] != 'NEARLINE':
            #    self.lfn.put_cmd(lcg_ls.get_command())
            #    ls_result = lcg_ls.get_output()
            #    self.assert_(ls_result['status'] == 'PASS',
            #        '%s, %s - FAILED, %s, Test ID %s' %
            #        (path, method, msg, self.id))


            srm_rm = rm.SrmRm(self.tsets['general']['endpoint'],
                self.tsets['general']['accesspoint'], self.dfn)
            self.lfn.put_cmd(srm_rm.get_command())
            rm_result = srm_rm.get_output()

            msg = 'dcache rm status'
            self.assert_(rm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(lcg_ls.get_command())
            ls_result = lcg_ls.get_output()
            msg = 'lcg ls status'
            self.assert_(ls_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

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

            self.assert_(int(ls_result['size']) == int(sm_result['unusedSize']) - int(st_result['unusedSize']))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        except KeyError, err:
            self.lfn.put_result('TAPE NOT SUPPORTED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
