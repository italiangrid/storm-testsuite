__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional.regression import regression as re

def get_space_metadata_failure_ts(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(re.RegressionTest('test_get_space_metadata_failure',conf, ifn, dfn, bifn, uid, lfn))

    return s
