__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional.regression import regression as re

def ts_get_space_metadata_failure(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_get_space_metadata_failure'][6])
    lfn.put_description(uid['ts_get_space_metadata_failure'][7])
    lfn.put_uuid(uid['ts_get_space_metadata_failure'][0])
    lfn.put_ruid(self.uid['ts_get_space_metadata_failure'][3])

    s.addTest(re.RegressionTest('test_get_space_metadata_failure',conf, ifn, dfn, bifn, lfn))

    return s
