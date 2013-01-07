__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment import conf

def ts_yaim_storm_pepc_resourceid_variable(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(conf.ConfTest('test_yaim_storm_pepc_resourceid_variable', conf, uid, lfn))
    return s
