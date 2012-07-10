__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests import utilities as ut

def ts_conf(conf, ifn, bifn, uid, lfn):
    s = unittest.TestSuite()

    lfn.put_name(uid['ts_conf'][6])
    lfn.put_description(uid['ts_conf'][7])
    lfn.put_uuid(uid['ts_conf'][0])
    lfn.flush_file()

    s.addTest(ut.UtilitiesTest('test_settings', conf, ifn, bifn, lfn))

    return s
