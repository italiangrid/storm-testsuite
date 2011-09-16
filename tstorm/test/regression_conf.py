__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import readfile
from tstorm.utils import service
from tstorm.utils import rpm
from tstorm.utils import ls

class RegressionConfigurationTest(unittest.TestCase):
    def __init__(self, testname):
      super(RegressionConfigurationTest, self).__init__(testname)

    def test_backend_logrotate_file(self):
      '''\nSYSTEM TEST - REGRESSION TESTS'''
      '''\nRT 3.4.8 - RfC https://storm.cnaf.infn.it:8443/redmine/issues/134'''
      self.cat_result = readfile.Cat('/etc/logrotate.d/storm-backend-server').get_output()
      self.assert_(self.cat_result['status'] == 'PASS')
      self.assert_('/opt/storm/backend/var/log/storm-backend.stdout' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/var/log/storm-backend.stderr' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/var/log/lcmaps.log' not in self.cat_result['otpt'])
      self.assert_('/var/log/storm/storm-backend.stdout' in self.cat_result['otpt'])
      self.assert_('/var/log/storm/storm-backend.stderr' in self.cat_result['otpt'])
      self.assert_('/var/log/storm/lcmaps.log' in self.cat_result['otpt'])

    def test_backend_cron_file(self):
      '''\nSYSTEM TEST - REGRESSION TESTS'''
      '''\nRT 3.4.9 - RfC https://storm.cnaf.infn.it:8443/redmine/issues/135'''
      self.cat_result = readfile.Cat('/etc/cron.d/storm-backend-server.cron').get_output()
      self.assert_(self.cat_result['status'] == 'PASS')
      self.assert_('/opt/storm/backend/etc/logrotate.d/logrotate.status' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/etc/logrotate.d/storm-backend.logrotate' not in self.cat_result['otpt'])
      self.assert_('/etc/logrotate.d/storm-backend-server' in self.cat_result['otpt'])
      self.assert_('/etc/logrotate.d/logrotate.status' in self.cat_result['otpt'])

    def test_yaim_version_file(self):
      '''\nSYSTEM TEST - REGRESSION TESTS'''
      '''\nRT 3.4.18 - RfC https://storm.cnaf.infn.it:8443/redmine/issues/149'''
      self.cat_result = readfile.Cat('/opt/glite/yaim/etc/versions/yaim-storm').get_output()
      self.assert_(self.cat_result['status'] == 'PASS')
      pn=self.cat_result['otpt'].split(' ')
      self.rpm_result = rpm.Rpm(pn[0]).get_output()
      self.assert_(self.rpm_result['status'] == 'PASS')
      v=self.rpm_result['otpt'].split(pn[0] + '-')[1].split('.noarch')[0]
      self.assert_(pn[1] == v[1])

    def test_backend_gridhttps(self):
      '''\nSYSTEM TEST - REGRESSION TESTS'''
      print '''\nRT 3.4.16 - RfC https://storm.cnaf.infn.it:8443/redmine/issues/140'''
      self.sr_result = service.Service('storm-backend-server').get_output()
      self.assert_(self.sr_result['status'] == 'PASS')
      self.assert_('running' in self.sr_result['otpt'])
      self.assert_('NOT' not in self.sr_result['otpt'])
      self.sr_result = service.Service('tomcat5').get_output()
      self.assert_(self.sr_result['status'] == 'PASS')
      self.assert_('running' in self.sr_result['otpt'])

    def test_gridhttps_plugin_link(self):
      '''\nSYSTEM TEST - REGRESSION TESTS'''
      print '''\nRT 3.4.19 - RfC https://storm.cnaf.infn.it:8443/redmine/issues/154'''
      self.ls_result = ls.Ls('/usr/share/java/storm-backend-server/storm-gridhttps-plugin.jar').get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.ls_result = ls.Ls('/usr/share/java/storm-backend-server/httpclient.jar').get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
      self.ls_result = ls.Ls('/usr/share/java/storm-backend-server/httpcore.jar').get_output()
      self.assert_(self.ls_result['status'] == 'PASS')
