__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import readfile
from tstorm.utils import service

class RegressionConfigurationTest(unittest.TestCase):
    def __init__(self):
      super(RegressionConfigurationTest, self).__init__(testname)

    def test_backend_logrotate_file(self):
      print '''\nSYSTEM TEST - REGRESSION TESTS'''
      print '''RT 3.4.8 - RfC https://storm.cnaf.infn.it:8443/redmine/issues/134\n'''
      self.cat_result = readfile.Cat('/etc/logrotate.d/storm-backend-server').get_output()
      self.assert_(self.cat_result['status'] == 'PASS')
      self.assert_('/opt/storm/backend/var/log/storm-backend.stdout' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/var/log/storm-backend.stderr' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/var/log/lcmaps.log' not in self.cat_result['otpt'])
      self.assert_('/var/log/storm/storm-backend.stdout' in self.cat_result['otpt'])
      self.assert_('/var/log/storm/storm-backend.stderr' in self.cat_result['otpt'])
      self.assert_('/var/log/storm/lcmaps.log' in self.cat_result['otpt'])

    def test_backend_cron_file(self):
      print '''\nSYSTEM TEST - REGRESSION TESTS'''
      print '''3.4.9 - RfC https://storm.cnaf.infn.it:8443/redmine/issues/135\n'''
      self.cat_result = readfile.Cat('/etc/cron.d/storm-backend-server.cron').get_output()
      self.assert_(self.cat_result['status'] == 'PASS')
      self.assert_('/opt/storm/backend/etc/logrotate.d/logrotate.status' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/etc/logrotate.d/storm-backend.logrotate' not in self.cat_result['otpt'])
      self.assert_('/etc/logrotate.d/storm-backend-server' in self.cat_result['otpt'])
      self.assert_('/etc/logrotate.d/logrotate.statusr' in self.cat_result['otpt'])

    def test_backend_gridhttps(self):
      print '''\nSYSTEM TEST - REGRESSION TESTS'''
      print '''3.4.16 - RfC https://storm.cnaf.infn.it:8443/redmine/issues/140\n'''
      self.sr_result = service.Service('storm-backend-server').get_output()
      self.assert_(self.sr_result['status'] == 'PASS')
      self.assert_('running' in self.sr_result['otpt'])
      self.assert_('NOT' not in self.sr_result['otpt'])
      self.sr_result = service.Service('tomcat5').get_output()
      self.assert_(self.sr_result['status'] == 'PASS')
      self.assert_('running' in self.sr_result['otpt'])
