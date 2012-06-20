__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import config
from tstorm.utils import createfile
from tstorm.utils import removefile
from tstorm.utils import utils

class UtilitiesTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, uid, lfn):
        super(UtilitiesTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.uid = uid
        self.lfn = lfn
    
    def test_settings(self):
        self.lfn.put_name(self.uid['test_settings'][5])
        self.lfn.put_description(self.uid['test_settings'][6])
        if self.uid.has_key('test_settings'):
            self.lfn.put_uuid(self.uid['test_settings'][0])
        else:
            print 'ADD UID for test_settings'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        self.lfn.put_cmd('')

        for x in self.tsets:
            self.assert_(x in ('general','ping','https','http','tape','bdii','yaim','log','node'))
            for y in self.tsets[x]:
                self.assert_(x != '')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_dd(self):
        self.lfn.put_name(self.uid['test_dd'][5])
        self.lfn.put_description(self.uid['test_dd'][6])
        if self.uid.has_key('test_dd'):
            self.lfn.put_uuid(self.uid['test_dd'][0])
        else:
            print 'ADD UID for test_dd'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        dd = createfile.Dd(self.ifn)
        self.lfn.put_cmd(dd.get_command())
        self.dd_result = dd.get_output()
        self.assert_(self.dd_result['status'] == 'PASS')
      
        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_cr_lf(self):
        self.lfn.put_name(self.uid['test_cr_lf'][5])
        self.lfn.put_description(self.uid['test_cr_lf'][6])
        if self.uid.has_key('test_cr_lf'):
            self.lfn.put_uuid(self.uid['test_cr_lf'][0])
        else:
            print 'ADD UID for test_cr_lf'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        self.cf_result = createfile.Cf(self.ifn).get_output()
        self.assert_(self.cf_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_rm_lf(self):
        self.lfn.put_name(self.uid['test_rm_lf'][5])
        self.lfn.put_description(self.uid['test_rm_lf'][6])
        if self.uid.has_key('test_rm_lf'):
            self.lfn.put_uuid(self.uid['test_rm_lf'][0])
        else:
            print 'ADD UID for test_rm_lf'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_output()

        rm_lf = removefile.RmLf(self.ifn, self.bifn)
        self.lfn.put_cmd(rm_lf.get_command())
        self.rmlf_result = rm_lf.get_output()
        self.assert_(self.rmlf_result['status'] == 'PASS')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
