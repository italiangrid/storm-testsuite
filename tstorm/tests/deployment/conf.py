import os 
import grp
import pwd
import unittest
import inspect

from tstorm.utils import configuration
from tstorm.utils import readfile
from tstorm.utils import rpm

from tstorm.tests.deployment import services

__author__ = 'Elisabetta Ronchieri'

class ConfTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn):
        super(ConfTest, self).__init__(testname)
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
                    get_resource_id = line.split('STORM_PEPC_RESOURCEID')[1]
                    break

            conf_file = ('%s/%s'
                % (services.FrontendSet.conf_folder,
                services.FrontendSet.conf_file))
            rf_result = readfile.Rf(fn=conf_file).get_output()

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
            elif get_argus_resource_id != '':
                self.assert_(get_resource_id == 'storm')

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_gridhttps_certificates_folder_added(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            msg = ('%s does not exist'
                % services.GridhttpsSet.certificates_folder)
            self.assertTrue(os.path.isdir(services.GridhttpsSet.certificates_folder),
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_gridhttps_conf_folder_ownership(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            stat_info = os.stat(services.GridhttpsSet.conf_folder)
            uid = stat_info.st_uid
            gid = stat_info.st_gid
            user = pwd.getpwuid(uid)[0]
            group = grp.getgrgid(gid)[0]

            msg = ('user %s is not set to %s'
                % (user, services.GridhttpsSet.ownership))
            self.assert_(user == services.GridhttpsSet.ownership,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            msg = ('group %s is not set to %s'
                % (group, services.GridhttpsSet.ownership))
            self.assert_(group == services.GridhttpsSet.ownership,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
