__author__ = 'Elisabetta Ronchieri'

import os 
import unittest
from tstorm.utils import config
from tstorm.utils import readfile
from tstorm.utils import service
from tstorm.utils import rpm
from tstorm.utils import ls

class RegressionConfigurationTest(unittest.TestCase):
    def __init__(self, testname, tfn, lfn):
      super(RegressionConfigurationTest, self).__init__(testname)
      self.tsets = config.TestSettings(tfn).get_test_sets()
      self.lfn = lfn

    def test_backend_server_status(self):
      self.lfn.put_name('WRONG STORM BACKEND SERVICE NAME RETURNED DURING STATUS')
      self.lfn.put_description('The name of StoRM Backend Service returned during the execution of status is wrong')
      self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/114')
      self.lfn.put_output()

      sr = service.Service('storm-backend-server')
      self.lfn.put_cmd(sr.get_command())

      self.sr_result(sr.get_output())
      self.assert_(self.sr_result['status'] == 'PASS')

      self.lfn.put_result('PASSED')
      self.lfn.flush_file()

    def test_backend_logrotate_file(self):
      self.lfn.put_name('STORN BACKEND LOGROTATE FILE POINTS TO NON EXISTING FILE')
      self.lfn.put_description('StoRM Backend logrotate file points to non existing file.')
      self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/134')
      self.lfn.put_output()

      rcat = readfile.Cat('/etc/logrotate.d/storm-backend-server')
      self.lfn.put_cmd(rcat.get_command())

      self.cat_result(rcat.get_output())
      self.assert_(self.cat_result['status'] == 'PASS')
      self.assert_('/opt/storm/backend/var/log/storm-backend.stdout' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/var/log/storm-backend.stderr' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/var/log/lcmaps.log' not in self.cat_result['otpt'])
      self.assert_('/var/log/storm/storm-backend.stdout' in self.cat_result['otpt'])
      self.assert_('/var/log/storm/storm-backend.stderr' in self.cat_result['otpt'])
      self.assert_('/var/log/storm/lcmaps.log' in self.cat_result['otpt'])

      self.lfn.put_result('PASSED')
      self.lfn.flush_file()

    def test_backend_cron_file(self):
      self.lfn.put_name('STORM BACKEND DOES NOT ROTATE LOG FILES')
      self.lfn.put_description('StoRM Backend does not rotate log files')
      self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/135')
      self.lfn.put_output()

      rcat = readfile.Cat('/etc/cron.d/storm-backend-server.cron')
      self.lfn.put_cmd(rcat.get_command())

      self.cat_result(rcat.get_output())
      self.assert_(self.cat_result['status'] == 'PASS')
      self.assert_('/opt/storm/backend/etc/logrotate.d/logrotate.status' not in self.cat_result['otpt'])
      self.assert_('/opt/storm/backend/etc/logrotate.d/storm-backend.logrotate' not in self.cat_result['otpt'])
      self.assert_('/etc/logrotate.d/storm-backend-server' in self.cat_result['otpt'])
      self.assert_('/etc/logrotate.d/logrotate.status' in self.cat_result['otpt'])

      self.lfn.put_result('PASSED')
      self.lfn.flush_file()

    def test_backend_gridhttps(self):
      self.lfn.put_name('DEFAULT GRIDHTTPS SERVER PORT NUMBER CONFLICTS WITH BACKEND DEFAULT XMLRPC PORT NUMBER')
      self.lfn.put_description('Default GridHTTPs server port number conflicts with Backend default xmlrpc port number')
      self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/140')
      self.lfn.put_output()

      sr = service.Service('storm-backend-server')
      self.lfn.put_cmd(sr.get_command())

      self.sr_result(sr.get_output())
      self.assert_(self.sr_result['status'] == 'PASS')
      self.assert_('running' in self.sr_result['otpt'])
      self.assert_('NOT' not in self.sr_result['otpt'])

      sr = service.Service('tomcat5')
      self.lfn.put_cmd(sr.get_command())

      self.sr_result(sr.get_output())
      self.assert_(self.sr_result['status'] == 'PASS')
      self.assert_('running' in self.sr_result['otpt'])

      self.lfn.put_result('PASSED')
      self.lfn.flush_file()

    def test_yaim_version_file(self):
      self.lfn.put_name('WRONG VERSION IN THE YAIM-VERSION FILE')
      self.lfn.put_description('Wrong version in the yaim-storm file')
      self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/149')
      self.lfn.put_output()

      rcat = readfile.Cat('/opt/glite/yaim/etc/versions/yaim-storm')
      self.lfn.put_cmd(rcat.get_command())

      self.cat_result(rcat.get_output())
      self.assert_(self.cat_result['status'] == 'PASS')
      pn=self.cat_result['otpt'].split(' ')

      crpm = rpm.Rpm(pn[0])
      self.lfn.put_cmd(crpm.get_command())

      self.rpm_result(crpm.get_output())
      self.assert_(self.rpm_result['status'] == 'PASS')
      v=self.rpm_result['otpt'].split(pn[0] + '-')[1].split('.noarch')
      self.assert_(pn[1] == v[0])

      self.lfn.put_result('PASSED')
      self.lfn.flush_file()

    def test_size_in_namespace_file(self):
      self.lfn.put_name('WRONG SETTINGS OF SIZE IN NAMESPACE.XML')
      self.lfn.put_description('Wrong settings of size in namespace.xml')
      self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/151')
      self.lfn.put_output()

      rcat = readfile.Cat(self.tsets['yaim']['def_path'])
      self.lfn.put_cmd(rcat.get_command())

      self.cat_result(rcat.get_output())
      self.assert_(self.cat_result['status'] == 'PASS')
      var=self.cat_result['otpt'].split('\n')

      rcatn = readfile.Cat('/etc/storm/backend-server/namespace.xml')
      self.lfn.put_cmd(rcatn.get_command())

      self.catn_result(rcatn.get_output())
      self.assert_(self.catn_result['status'] == 'PASS')
      varn=self.catn_result['otpt']
      for x in var:
        if "ONLINE_SIZE" in x or "NEARLINE_SIZE" in x:
          ls=x.split('SIZE')[1].split('=')
          bs=int(ls[1])*1024*1024*1024
          if 'ONLINE_SIZE' in x:
            ols='<TotalOnlineSize unit=\"Byte\" limited-size=\"true\">' + str(bs) + '</TotalOnlineSize>'
            self.assert_(ols in varn)
          elif 'NEARLINE_SIZE' in x:
            nls='<TotalNearlineSize unit=\"Byte\">' + str(bs) + '</TotalNearlineSize>'
            dnls='<TotalNearlineSize unit=\"Byte\">0</TotalNearlineSize>'
            for y in var:
               if ls[0] + 'STORAGECLASS' in y:
                 sc=x.split('STORAGECLASS')[1].split('=')[1][1:len(x.split('STORAGECLASS')[1].split('=')[1])-1]
                 if sc == 'T1D0':
                   self.assert_(nls in varn)
                   break

      self.lfn.put_result('PASSED')
      self.lfn.flush_file()

    def test_gridhttps_plugin_links(self):
      self.lfn.put_name('REMOVED GRIDHTTPS PLUGIN LINKS DURING UPGRADE FROM 1.7.0 to 1.7.1')
      self.lfn.put_description('Removed gridhttpds plugin links during upgrade from 1.7.0 to 1.7.1')
      self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/154')
      self.lfn.put_output()

      rls = ls.Ls('/usr/share/java/storm-backend-server/storm-gridhttps-plugin.jar')
      self.lfn.put_cmd(rls.get_command())

      self.ls_result(rls.get_output())
      self.assert_(self.ls_result['status'] == 'PASS')

      rls = ls.Ls('/usr/share/java/storm-backend-server/httpclient.jar')
      self.lfn.put_cmd(rls.get_command())

      self.ls_result(rls.get_output())
      self.assert_(self.ls_result['status'] == 'PASS')

      rls = ls.Ls('/usr/share/java/storm-backend-server/httpcore.jar')
      self.lfn.put_cmd(rls.get_command())

      self.ls_result(rls.get_output())
      self.assert_(self.ls_result['status'] == 'PASS')
      self.lfn.put_result('PASSED')
      self.lfn.flush_file()

    def test_mysql_connector_java_links(self):
      self.lfn.put_name('MYSQL-CONNECTOR-JAVA DOWNLOADING FAILURE')
      self.lfn.put_description('mysql-connector-java is not downloaded due to an issue in its owner repository')
      self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/179')
      self.lfn.put_output()

      rls = ls.Ls('/usr/share/java/storm-backend-server/mysql-connector-java-5.1.13-bin.jar')
      self.lfn.put_cmd(rls.get_command())

      self.ls_result(rls.get_output())
      self.assert_(self.ls_result['status'] == 'FAILURE')

      rls = ls.Ls('/usr/share/java/storm-backend-server/mysql-connector-java-5.1.12.jar')
      self.lfn.put_cmd(rls.get_command())

      self.ls_result(rls.get_output())
      self.assert_(self.ls_result['status'] == 'PASS')

      self.lfn.put_result('PASSED')
      self.lfn.flush_file()
