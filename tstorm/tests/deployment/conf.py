import os 
import unittest
import inspect

from tstorm.utils import configuration
from tstorm.utils import readfile

__author__ = 'Elisabetta Ronchieri'

class ConfTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn):
        super(Conf, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.id = uid.get_id()
        self.lfn = lfn

    def test_yaim_storm_pepc_resourceid_variable(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            r_yaim_result = readfile.Rf(fn=self.tsets['yaim']['def_path']).get_output()

            msg = 'rf status'
            self.assert_(r_yaim_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            get_resource_id = ''
            for line in r_yaim_result['otpt'].split('\n'):
                if 'STORM_PEPC_RESOURCEID' in line:
                    get_resource_id = line.split('STORM_STORM_PEPC_RESOURCEID')[1]
                    break

            rf_result = readfile.Rf(fn='/etc/storm/frontend-server/storm-frontend-server.spec').get_output()

            msg = 'rf status'
            self.assert_(rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            get_argus_resource_id = ''
            for x in rf_result['otpt'].split('\n'):
                if 'argus.resource-id' in x:
                    get_argus_resource_id = x.split('argus.resource-id=')[1]
                    break

            if get_resource_id != '' and get_argus_resource_id != '':
                self.assert_(get_resource_id == get_argus_resource_id)

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
