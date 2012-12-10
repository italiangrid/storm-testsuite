__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
import inspect
from tstorm.utils import config
from tstorm.utils import createfile
from tstorm.utils import removefile
from tstorm.utils import utils

class UtilitiesTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, bifn, uid, lfn):
        super(UtilitiesTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.bifn = bifn
        self.id = uid.get_id()
        self.lfn = lfn
    
    def test_settings(self):
        self.lfn.put_cmd('')

        for x in self.tsets:
            try:
                msg = 'Section %s is wrong in the conf file' % x
                self.assert_(x in ('general','ping','https','http','tape',
                    'bdii','yaim','log','node'),
                    '%s - FAILED, %s, Test ID %s' %
                    (inspect.stack()[1][3], msg, self.id))
            except AssertionError, err:
                print err
                self.lfn.put_result('FAILED')
                break

            for y in self.tsets[x]:
                try:
                    msg = 'Option value %s is not set' % y
                    self.assert_(y != '',
                        '%s - FAILED, %s, Test ID %s' %
                        (inspect.stack()[1][3], msg, self.id))
                except AssertionError, err:
                    print err
                    self.lfn.put_result('FAILED')
                    break

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_dd(self):
        dd = createfile.Dd(self.ifn)
        self.lfn.put_cmd(dd.get_command())
        self.dd_result = dd.get_output()
        try:
            msg = 'Input file %s has not been created' % self.ifn
            self.assert_(self.dd_result['status'] == 'PASS',
                '%s - FAILED, %s, Test ID %s' %
                (inspect.stack()[1][3], msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else: 
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_cr_lf(self):
        self.cf_result = createfile.Cf(self.ifn).get_output()
        try:
            msg = 'Local file %s has not been created' % self.ifn
            self.assert_(self.cf_result['status'] == 'PASS',
                '%s - FAILED, %s, Test ID %s' %
                (inspect.stack()[1][3], msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_rm_lf(self):
        rm_lf = removefile.RmLf(self.ifn, self.bifn)
        self.lfn.put_cmd(rm_lf.get_command())
        self.rmlf_result = rm_lf.get_output()
        try:
            msg = 'Local files (%s,%s) have not been removed' % \
                (self.ifn, self.bifn)
            self.assert_(self.rmlf_result['status'] == 'PASS',
                '%s - FAILED, %s, Test ID %s' %
                (inspect.stack()[1][3], msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
