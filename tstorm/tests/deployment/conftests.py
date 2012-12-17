__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.deployment import configuration

def ts_yaim_storm_pepc_resourceid_variable(conf, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(configuration.ConfigurationTest('test_yaim_storm_pepc_resourceid_variable', conf, uid, lfn))
    return s
