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
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            self.lfn.put_cmd('')

            for x in self.tsets:
                msg = 'Section %s is wrong in the conf file' % x
                self.assert_(x in ('general','ping','https','http','tape',
                    'bdii','yaim','log','node'),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            for y in self.tsets[x]:
                msg = 'Option value %s is not set' % y
                self.assert_(y != '',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_dd(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            dd = createfile.Dd(self.ifn)
            self.lfn.put_cmd(dd.get_command())
            self.dd_result = dd.get_output()

            msg = 'Input file %s has not been created' % self.ifn
            self.assert_(self.dd_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else: 
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_cr_lf(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            self.cf_result = createfile.Cf(self.ifn).get_output()

            msg = 'Local file %s has not been created' % self.ifn
            self.assert_(self.cf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_rm_lf(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            rm_lf = removefile.RmLf(self.ifn, self.bifn)
            self.lfn.put_cmd(rm_lf.get_command())
            self.rmlf_result = rm_lf.get_output()\

            msg = 'Local files (%s,%s) have not been removed' % \
                (self.ifn, self.bifn)
            self.assert_(self.rmlf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
