__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ls
from tstorm.utils import cp
from tstorm.utils import rm
from tstorm.utils import rmdir
from tstorm.utils import cksm
from tstorm.utils import space
from tstorm.utils import findstrings
from tstorm.utils import abort
from tstorm.utils import createfile
from tstorm.utils import removefile

class RegressionTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, lfn, prt='gsiftp'):
        super(RegressionTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.prt = prt
        self.lfn = lfn

    def test_eight_digit_string_checksum(self):
        self.lfn.put_name('COMPARISON BUG IN LCG-CR COPYING TO STORM')
        des = '''The StoRM GridFTP component stores the checksum value computed during 
the file transfer as a long number, discarding in this way leading zeroes. The
default ADLER32 checksum match algorithm considers checksum values as strings so the 
leading zeroes matters.'''
        self.lfn.put_description(des)
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/108')
        self.lfn.put_output()

        dd = createfile.Dd(self.ifn)
        self.lfn.put_cmd(dd.get_command())
        self.dd_result = dd.get_output()
        self.assert_(self.dd_result['status'] == 'PASS')

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ll = lcg_ls.get_output()
        self.assert_(ll['status'] == 'FAILURE')

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        self.cp_result = lcg_cp.get_output()
        self.assert_(self.cp_result['status'] == 'PASS')

        self.lfn.put_cmd(lcg_ls.get_command())
        ll = lcgls.get_output()
        self.assert_(ll['status'] == 'PASS')

        self.lcksm_result = cksm.CksmLf(self.ifn).get_output()
        self.assert_(ll['Checksum'] == self.lcksm_result['Checksum'])

        storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                   self.tsets['https']['voms'], self.dfn)
        self.lfn.put_cmd(storm_rm.get_command())
        self.rm_result = storm_rm.get_output()
        self.assert_(self.rm_result['status'] == 'PASS')
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            storm_rmdir = rmdir.StoRMRmdir(self.tsets['general']['endpoint'],
                          self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(storm_rmdir.get_command())
            self.rmdir_result = storm_rmdir.get_output()
            for x in self.rmdir_result['status']:
                self.assert_(x == 'PASS')

        rm_lf = removefile.RmLf(self.ifn, self.bifn)
        self.lfn.put_cmd(rm_lf.get_command())
        self.rmlf_result = rm_lf.get_output()
        self.assert_(self.rmlf_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_update_free_space_upon_rm(self):
        self.lfn.put_name('INCORRECT INFORMATION PUBLISHED BY STORM')
        des = '''StoRM does not publish correctly values for used and free space on the
 BDII due to a bug in the update of the free space after the the srmRm operation'''
        self.lfn.put_description(des)
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/106')
        self.lfn.put_output()

        dd = createfile.Dd(self.ifn)
        self.lfn.put_cmd(dd.get_command())
        self.dd_result = dd.get_output()
        self.assert_(self.dd_result['status'] == 'PASS')

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        ll = lcg_ls.get_output()
        self.assert_(ll['status'] == 'FAILURE')

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn,
                 self.dfn, self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        self.cp_result = lcg_cp.get_output()
        self.assert_(self.cp_result['status'] == 'PASS')

        storm_gst = space.StoRMGst(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'],
                   self.tsets['general']['spacetoken'])
        self.lfn.put_cmd(storm_gst.get_command())
        self.st_result = storm_gst.get_output()
        self.assert_(self.st_result['status'] == 'PASS')

        storm_gsm1 = space.StoRMGsm(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'],
                     self.st_result['arrayOfSpaceTokens'])
        self.lfn.put_cmd(storm_gsm1.get_command())
        self.sm1_result = storm_gsm1.get_output()
        self.assert_(self.sm1_result['status'] == 'PASS')

        self.lfn.put_cmd(lcg_ls.get_command())
        ll = lcg_ls.get_output()
        self.assert_(ll['status'] == 'PASS')

        storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                   self.tsets['https']['voms'], self.dfn)
        self.lfn.put_cmd(storm_rm.get_command())
        self.rm_result = storm_rm.get_output()
        self.assert_(self.rm_result['status'] == 'PASS')
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            storm_rmdir = rmdir.StoRMRmdir(self.tsets['general']['endpoint'],
                          self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(storm_rmdir.get_command())
            self.rmdir_result = storm_rmdir.get_output()
            for x in self.rmdir_result['status']:
                self.assert_(x == 'PASS')

        self.lfn.put_cmd(lcg_ls.get_command())
        ll = lcg_ls.get_output()
        self.assert_(ll['status'] == 'FAILURE')

        ls_ls = ls.Ls(self.ifn)
        self.lfn.put_cmd(ls_ls.get_command())
        self.lls_result = ls_ls.get_output()
        self.assert_(self.lls_result['status'] == 'PASS')

        storm_gsm2 = space.StoRMGsm(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'],
                     self.st_result['arrayOfSpaceTokens'])
        self.lfn.put_cmd(storm_gsm2.get_command())
        self.sm2_result = storm_gsm2.get_output()
        self.assert_(self.sm2_result['status'] == 'PASS')
 
        a=int(self.sm2_result['unusedSize']) - int(self.sm1_result['unusedSize'])
        self.assert_(int(self.lls_result['size']) == a)

        rm_lf = removefile.RmLf(self.ifn, self.bifn)
        self.lfn.put_cmd(rm_lf.get_command())
        self.rmlf_result = rm_lf.get_output()
        self.assert_(self.rmlf_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_update_used_space_upon_pd(self):
        self.lfn.put_name('STORM BUG: SPACE TOKEN USED SPACE IS NOT UPDATE')
        des = '''StoRM does not provides updated used space value for Space Token
due to a bug in the update of the used space after the the srmPutDone 
operation.'''
        self.lfn.put_description(des)
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/109')
        self.lfn.put_output()

        dd = createfile.Dd(self.ifn)
        self.lfn.put_cmd(dd.get_command())
        self.dd_result = dd.get_output()
        self.assert_(self.dd_result['status'] == 'PASS')

        storm_gst = space.StoRMGst(self.tsets['general']['endpoint'],
                    self.tsets['general']['accesspoint'],
                    self.tsets['general']['spacetoken'])
        self.lfn.put_cmd(storm_gst.get_command())
        self.st_result = storm_gst.get_output()
        self.assert_(self.st_result['status'] == 'PASS')

        storm_gsm1 = space.StoRMGsm(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'],
                     self.st_result['arrayOfSpaceTokens'])
        self.lfn.put_cmd(storm_gsm1.get_command())
        self.sm1_result = storm_gsm1.get_output()
        self.assert_(self.sm1_result['status'] == 'PASS')

        lcg_ls = ls.LcgLs(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.dfn)
        self.lfn.put_cmd(lcg_ls.get_command())
        self.ls_result = lcg_ls.get_output()
        self.assert_(self.ls_result['status'] == 'FAILURE')

        lcg_cp = cp.LcgCp(self.tsets['general']['endpoint'],
                 self.tsets['general']['accesspoint'], self.ifn, self.dfn,
                 self.bifn)
        self.lfn.put_cmd(lcg_cp.get_command())
        self.cp_result = lcg_cp.get_output()
        self.assert_(self.cp_result['status'] == 'PASS')

        ls_ls = ls.Ls(self.ifn)
        self.lfn.put_cmd(ls_ls.get_command())
        self.lls_result = ls_ls.get_output()
        self.assert_(self.lls_result['status'] == 'PASS')

        storm_gsm2 = space.StoRMGsm(self.tsets['general']['endpoint'],
                     self.tsets['general']['accesspoint'],
                     self.st_result['arrayOfSpaceTokens'])
        self.lfn.put_cmd(storm_gsm2.get_command())
        self.sm2_result = storm_gsm2.get_output()
        self.assert_(self.sm2_result['status'] == 'PASS')

        a=(int(self.sm1_result['unusedSize']) - int(self.sm2_result['unusedSize']))
        self.assert_(int(self.lls_result['size']) == a)

        storm_rm = rm.StoRMRm(self.tsets['general']['endpoint'],
                   self.tsets['https']['voms'], self.dfn)
        self.lfn.put_cmd(storm_rm.get_command())
        self.rm_result = storm_rm.get_output()
        self.assert_(self.rm_result['status'] == 'PASS')
        if '/' in self.dfn:
            a=os.path.dirname(self.dfn)
            storm_rmdir = rmdir.StoRMRmdir(self.tsets['general']['endpoint'],
                          self.tsets['general']['accesspoint'], a)
            self.lfn.put_cmd(storm_rmdir.get_command())
            self.rmdir_result = storm_rmdir.get_output()
            for x in self.rmdir_result['status']:
                self.assert_(x == 'PASS')

        rm_lf = removefile.RmLf(self.ifn, self.bifn)
        self.lfn.put_cmd(rm_lf.get_command())
        self.rmlf_result = rm_lf.get_output()
        self.assert_(self.rmlf_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_unsupported_protocols(self):
        name = '''STORM BUG: SRM TRANSFER COMMANDS DOES NOT REPORT ERRONEOUS 
PROTOCOL REQUESTS'''
        self.lfn.put_name(name)
        des = '''StoRM does not returns SRM_NOT_SUPPORTED error code when file 
transfer operation (srmPrepareToPut, srmPrepareToGet, srmBringOnline) are 
called providing a list of not supported desired transfer protocols to a 
bug in the management of file transfer operation. StoRM does not verifies 
if the provided protocols are supported.'''
        self.lfn.put_description(des)
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/127')
        self.lfn.put_output()

        storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn,
                   'unsupported')
        self.lfn.put_cmd(storm_ptp.get_command())
        self.ptp_result = storm_ptp.get_output()
        self.assert_(self.ptp_result['status'] == 'FAILURE')
        self.assert_('SRM_NOT_SUPPORTED' in self.ptp_result['statusCode'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_both_sup_and_unsup_protocols(self):
        name = '''STORM FRONTEND PRODUCES HUGE LOG FILE WHEN MANAGING REQUESTS 
THAT CONTAIN SUPPORTED PROTOCOLS'''
        self.lfn.put_name(name)
        des = '''StoRM produced huge log file when file transfer operation
(srmPrepareToPut, srmPrepareToGet, srmBringOnline) are called with a list of
desired transfered protocols.'''
        self.lfn.put_description(des)
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/126')
        self.lfn.put_output()

        storm_ptp = cp.StoRMPtp(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn, 
                   self.prt + ',unsupported')
        self.lfn.put_cmd(storm_ptp.get_command())
        self.ptp_result = storm_ptp.get_output()
        self.assert_(self.ptp_result['status'] == 'PASS')

        fs_grep = findstrings.Grep().get_output()
        self.lfn.put_cmd(fs_grep.get_command())
        self.fs_result = fs_grep.get_output()
        self.assert_(self.fs_result['status'] == 'FAILURE')

        storm_ar = abort.StoRMAr(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'],
                   self.ptp_result['requestToken'])
        self.lfn.put_cmd(storm_ar.get_command())
        self.ar_result = storm_ar.get_output()
        self.assert_(self.ar_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_non_ascii_chars(self):
        name = '''STORM BUG: REQUEST WITH AUTHORIZATION ID PARAMETERS WITH 
NON ASCII CHARACTERS MAKES FE CRASH'''
        self.lfn.put_name(name)
        des = '''StoRM Frontend crashes when managing asynchronous requests 
providing string parameters containing non ASCII characters.'''
        self.lfn.put_description(des)
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/137')
        self.lfn.put_output()

        storm_ls = ls.StoRMLs(self.tsets['general']['endpoint'],
                   self.tsets['general']['accesspoint'], self.dfn + 'tèstèèà')
        self.lfn.put_cmd(storm_ls.get_command())
        self.ls_result = storm_ls.get_output()
        self.assert_(self.ls_result['status'] == 'FAILURE')

        storm_ping = ping.StoRMPing(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(storm_ping.get_command())
        self.ping_result = storm_ping.get_output()
        self.assert_(self.ping_result['status'] == 'PASS')
        self.assert_(self.ping_result['versionInfo'] == self.tsets['ping']['versioninfo'])
        for x in self.ping_result['key']:
            if x == 'backend_type':
                self.assert_(self.ping_result['value'][self.ping_result['key'].index(x)] == self.tsets['ping']['backend_type'])
            elif x == 'backend_version':
                self.assert_(self.ping_result['value'][self.ping_result['key'].index(x)] == self.tsets['ping']['backend_version'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_storm_backend_age(self):
        name = '''WRONG STORM BACKEND AGE RETURNED BY SRM PING'''
        self.lfn.put_name(name)
        des = '''Wrong the StoRM backend age returned by the command srm ping.'''
        self.lfn.put_description(des)
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/181')
        self.lfn.put_output()

        storm_ping = ping.StoRMPing(self.tsets['general']['endpoint'])
        self.lfn.put_cmd(storm_ping.get_command())
        self.ping_result = storm_ping.get_output()
        self.assert_(self.ping_result['status'] == 'PASS')
        self.assert_(self.ping_result['versionInfo'] == self.tsets['ping']['versioninfo'])
        for x in self.ping_result['key']:
            if x == 'backend_type':
                self.assert_(self.ping_result['value'][self.ping_result['key'].index(x)] == self.tsets['ping']['backend_type'])
            elif x == 'backend_version':
                self.assert_(self.ping_result['value'][self.ping_result['key'].index(x)] == self.tsets['ping']['backend_version'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
