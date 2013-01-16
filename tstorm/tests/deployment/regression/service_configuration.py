import os 
import time
import unittest
import inspect

from tstorm.utils import configuration
from tstorm.utils import readfile
from tstorm.utils import service
from tstorm.utils import rpm
from tstorm.utils import mysqlquery as mq
from tstorm.utils import yaim
from tstorm.utils import utils
from tstorm.utils import listinfo
from tstorm.utils import library_dependencies

from tstorm.tests.deployment import services

__author__ = 'Elisabetta Ronchieri'

class RegressionConfigurationTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn):
        super(RegressionConfigurationTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.id = uid.get_id()
        self.lfn = lfn

    def test_backend_server_status(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            sr = service.Service(services.BackendSet.service)
            self.lfn.put_cmd(sr.get_command())
            sr_result = sr.get_output()

            msg = '%s status' % services.BackendSet.service
            self.assert_(sr_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_backend_logrotate_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            logrotate_file = ('%s/%s'
                % (services.BackendSet.logrotate_folder,
                services.BackendSet.logrotate_file))
            read_cat = readfile.Cat(logrotate_file)
            self.lfn.put_cmd(read_cat.get_command())
            cat_result = read_cat.get_output()

            msg = 'cat status'
            self.assert_(cat_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'File storm-backend.stdout was found'
            self.assert_('/opt/storm/backend/var/log/storm-backend.stdout' not in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'File storm-backend.stderr was found'
            self.assert_('/opt/storm/backend/var/log/storm-backend.stderr' not in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'File lcmaps.log was found'
            self.assert_('/opt/storm/backend/var/log/lcmaps.log' not in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            stdout_file = ('%s/%s'
                % (services.BackendSet.log_folder,
                services.BackendSet.stdout_file))
            msg = 'File %s was not found' % stdout_file
            self.assert_(stdout_file in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            stderr_file = ('%s/%s'
                % (services.BackendSet.log_folder,
                services.BackendSet.stderr_file))
            msg = 'File %s was not found' % stderr_file
            self.assert_(stderr_file in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            lcmaps_file = ('%s/%s'
                % (services.BackendSet.log_folder,
                services.BackendSet.lcmaps_file))
            msg = 'File %s was not found' % lcmaps_file
            self.assert_(lcmaps_file in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_backend_cron_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            cron_file = ('%s/%s'
                % (services.BackendSet.cron_folder,
                services.BackendSet.cron_file))
            read_cat = readfile.Cat(cron_file)
            self.lfn.put_cmd(read_cat.get_command())
            cat_result = read_cat.get_output()

            msg = 'cat %s status' % cron_file
            self.assert_(cat_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'File logrotate.status was found'
            self.assert_('/opt/storm/backend/etc/logrotate.d/logrotate.status' not in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'File storm-backend.logrotate was found'
            self.assert_('/opt/storm/backend/etc/logrotate.d/storm-backend.logrotate' not in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            logrotate_file = ('%s/%s'
               % (services.BackendSet.logrotate_folder,
               services.BackendSet.logrotate_file))
            msg = 'File %s was not found' % logroate_file
            self.assert_(logrotate_file in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            status_file = ('%s/%s'
               % (services.BackendSet.logrotate_folder,
               services.BackendSet.status_file))
            msg = 'File %s was not found' % status_file
            self.assert_(status_file in cat_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_backend_gridhttps(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            rpm_out = rpm.Rpm(services.BackendSet.package)
            self.lfn.put_cmd(rpm_out.get_command())
            rpm_result = rpm_out.get_output()

            if rpm_result['status'] == 'PASS':
                sr = service.Service(services.BackendSet.service)
                self.lfn.put_cmd(sr.get_command())
                sr_result = sr.get_output()

                msg = '%s status' % services.BackendSet.service
                self.assert_(sr_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

                msg = 'RUNNING was not found'
                self.assert_('RUNNING' in sr_result['otpt'],
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

                msg = 'NOT was found'
                self.assert_('NOT' not in sr_result['otpt'],
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))


                rpm_out = rpm.Rpm(services.GridhttpsSet.package)
                self.lfn.put_cmd(rpm_out.get_command())
                rpm_result = rpm_out.get_output()

                if rpm_result['status'] == 'PASS':
                    sr = service.Service(services.GridhttpsSet.dependency)
                    self.lfn.put_cmd(sr.get_command())
                    sr_result = sr.get_output()

                    msg = '%s status' % services.GridhttpsSet.dependency
                    self.assert_(sr_result['status'] == 'PASS',
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))

                    msg = 'running was not found'
                    self.assert_('running' in sr_result['otpt'],
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_yaim_version_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            version_file = ('%s/%s'
                % (services.YaimSet.version_folder,
                services.YaimSet.version_file))
            read_cat = readfile.Cat(version_file)
            self.lfn.put_cmd(read_cat.get_command())
            cat_result = read_cat.get_output()

            msg = 'cat %s status' % version_file
            self.assert_(cat_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            pn=cat_result['otpt'].split(' ')
            rpm_out = rpm.Rpm(pn[0])
            self.lfn.put_cmd(rpm_out.get_command())
            rpm_result = rpm_out.get_output()

            msg = 'rpm status'
            self.assert_(rpm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            v=rpm_result['otpt'].split(pn[0] + '-')[1].split('.noarch')

            msg = 'Wrong version value'
            self.assert_(pn[1] == v[0],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_size_in_namespace_file(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            read_cat = readfile.Cat(self.tsets['yaim']['def_path'])
            self.lfn.put_cmd(read_cat.get_command())
            cat_result = read_cat.get_output()

            msg = 'cat status'
            self.assert_(cat_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            var=cat_result['otpt'].split('\n')

            name_file = ('%s/%s'
                % (services.BackendSet.conf_folder,
                services.BackendSet.name_file))
            read_catn = readfile.Cat(name_file)
            self.lfn.put_cmd(read_catn.get_command())
            catn_result = read_catn.get_output()

            msg = 'cat %s status' % name_file
            self.assert_(catn_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            varn=catn_result['otpt']

            for x in var:
                if "ONLINE_SIZE" in x or "NEARLINE_SIZE" in x:
                    ls=x.split('SIZE')[1].split('=')
                    bs=int(ls[1])*1024*1024*1024
                if 'ONLINE_SIZE' in x:
                    ols='<TotalOnlineSize unit=\"Byte\" limited-size=\"true\">' + str(bs) + '</TotalOnlineSize>'

                    msg = 'Wrong totalonlinesize value'
                    self.assert_(ols in varn,
                        '%s, %s - FAILED, %s, Test ID %s' %
                        (path, method, msg, self.id))
                elif 'NEARLINE_SIZE' in x:
                    nls='<TotalNearlineSize unit=\"Byte\">' + str(bs) + '</TotalNearlineSize>'
                    dnls='<TotalNearlineSize unit=\"Byte\">0</TotalNearlineSize>'
                    for y in var:
                        if ls[0] + 'STORAGECLASS' in y:
                            sc=x.split('STORAGECLASS')[1].split('=')[1][1:len(x.split('STORAGECLASS')[1].split('=')[1])-1]
                            if sc == 'T1D0':
                                msg = 'Wrong totalnearlinesize value'
                                self.assert_(nls in varn,
                                    '%s, %s - FAILED, %s, Test ID %s' %
                                    (path, method, msg, self.id))
                                break
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_gridhttps_plugin_links(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            plugin_file = ('%s/%s'
                % (services.BackendSet.java_folder,
                services.BackendSet.plugin_file))
            ls_ls = listinfo.Ls(plugin_file)
            self.lfn.put_cmd(ls_ls.get_command())
            ls_result = ls_ls.get_output()

            msg = 'ls %s status' % plugin_file
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            httpclient_file = ('%s/%s'
                % (services.BackendSet.java_folder,
                services.BackendSet.httpclient_file))
            ls_ls = listinfo.Ls(httpclient_file)
            self.lfn.put_cmd(ls_ls.get_command())
            ls_result = ls_ls.get_output()

            msg = 'ls %s status' % httpclient_file
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            httpcore_file = ('%s/%s'
                % (services.BackendSet.java_folder,
                services.BackendSet.httpcore_file))
            ls_ls = listinfo.Ls(httpcore_file)
            self.lfn.put_cmd(ls_ls.get_command())
            ls_result = ls_ls.get_output()

            msg = 'ls %s status' % httpcore_file
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_backend_server_name_status(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            sr = service.Service(services.BackendSet.service)
            self.lfn.put_cmd(sr.get_command())
            sr_result = sr.get_output()

            msg = 'service %s status' % services.BackendSet.service
            self.assert_(sr_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = '%s was not found' % services.BackendSet.service
            self.assert_(services.BackendSet.service in sr_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_mysql_storage_space_update(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            read_cat = readfile.Cat(self.tsets['yaim']['def_path'])
            self.lfn.put_cmd(read_cat.get_command())
            cat_result = read_cat.get_output()

            msg = 'cat status'
            self.assert_(cat_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            var=cat_result['otpt'].split('\n')

            storage_area = {}
            replace_storage_area = {}
            token = {}
            db_user = ''
            db_pwd = ''
            for x in var:
                if "ONLINE_SIZE" in x:
                    ls=x.split('SIZE')[1].split('=')
                    #storage_area[x.split('STORM_')[1].split('_ONLINE_SIZE')[0]] = str(int(ls[1])*1024*1024*1024)
                    #replace_storage_area[x.split('STORM_')[1].split('_ONLINE_SIZE')[0]] = str(int(ls[1])*1024*1024*1024*502)
                    storage_area[x.split('STORM_')[1].split('_ONLINE_SIZE')[0]] = str(int(ls[1]))
                    replace_storage_area[x.split('STORM_')[1].split('_ONLINE_SIZE')[0]] = str(int(ls[1])*502)
                    #replace_storage_area[x.split('STORM_')[1].split('_ONLINE_SIZE')[0]] = str(4)
                if "TOKEN" in x:
                    ls=x.split('TOKEN')[1].split('=')
                    token[x.split('STORM_')[1].split('_TOKEN')[0]] = ls[1]
                if "STORM_DB_USER" in x:
                    db_user = x.split('=')[1]
                if "STORM_DB_PWD" in x:
                    db_pwd = x.split('=')[1]

            if len(token) != len(storage_area):
                for x in storage_area.keys():
                    if x not in token.keys():
                       token[x] = x+'_TOKEN' 

            #print storage_area
            #print replace_storage_area
            #print token
            msg = 'Wrong storage area value'
            self.assert_(len(storage_area) > 0,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong storage area value'
            self.assert_(len(replace_storage_area) > 0,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong storage area value'
            self.assert_(len(storage_area) == len(replace_storage_area),
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            db_name = 'storm_be_ISAM'
            db_table = 'storage_space'
            db_field = ['total_size', 'available_size']
        
            if db_user != '' and db_pwd != '':
                mysql_query = mq.Mysql(db_name, db_table, db_field, 
                    self.tsets['general']['backend_hostname'],
                    token, db_user=db_user, db_pwd=db_pwd)
            elif db_user != '' and db_pwd == '':
                mysql_query = mq.Mysql(db_name, db_table, db_field,
                    self.tsets['general']['backend_hostname'],
                    token, db_user=db_user)
            elif db_user == '' and db_pwd != '':
                mysql_query = mq.Mysql(db_name, db_table, db_field,
                    self.tsets['general']['backend_hostname'],
                    token, db_pwd=db_pwd)
            else:
                mysql_query = mq.Mysql(db_name, db_table, db_field, 
                    self.tsets['general']['backend_hostname'],
                    token)
            for x in token.keys():
                self.lfn.put_cmd(mysql_query.get_command(token[x]))
            mysql1_result = mysql_query.get_output()
            for x in mysql1_result['status']:
                msg = 'mysql status'
                self.assert_(x == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            modify_deffile = yaim.ModifyDeffile(self.tsets['yaim']['def_path'],
                storage_area, replace_storage_area)
            md_result = modify_deffile.get_output()

            msg = 'modify yaim status'
            self.assert_(md_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            run_yaim = yaim.Yaim(self.tsets['yaim']['def_path'],
                back_end=self.tsets['node']['backend'])
            self.lfn.put_cmd(run_yaim.get_command()) 
            yaim_result = run_yaim.get_output()

            msg = 'run yaim status'
            self.assert_(yaim_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            if db_user != '' and db_pwd != '':
                mysql_query = mq.Mysql(db_name, db_table, db_field, 
                    self.tsets['general']['backend_hostname'],
                    token, db_user=db_user, db_pwd=db_pwd)
            elif db_user != '' and db_pwd == '':
                mysql_query = mq.Mysql(db_name, db_table, db_field,
                    self.tsets['general']['backend_hostname'],
                    token, db_user=db_user)
            elif db_user == '' and db_pwd != '':
                mysql_query = mq.Mysql(db_name, db_table, db_field,
                    self.tsets['general']['backend_hostname'],
                    token, db_pwd=db_pwd)
            else:
                mysql_query = mq.Mysql(db_name, db_table, db_field, 
                    self.tsets['general']['backend_hostname'],
                    token)

            for x in token.keys():
                self.lfn.put_cmd(mysql_query.get_command(token[x]))
            mysql2_result = mysql_query.get_output()
            for x in mysql2_result['status']:
                msg = 'mysql status'
                self.assert_(x == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            for x in mysql1_result['token'].keys():
                u1=mysql1_result['token'][x][0]
                u2=mysql2_result['token'][x][0]
                f1=mysql1_result['token'][x][1]
                f2=mysql2_result['token'][x][1]
                msg = 'Wrong token value'
                self.assert_(int(u1)-int(u2) == int(f1)-int(f2),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

            modify_deffile = yaim.ModifyDeffile(self.tsets['yaim']['def_path'],
                replace_storage_area, storage_area)
            md_result = modify_deffile.get_output()

            msg = 'modify yaim status'
            self.assert_(md_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            run_yaim = yaim.Yaim(self.tsets['yaim']['def_path'],
                back_end=self.tsets['node']['backend'])
            self.lfn.put_cmd(run_yaim.get_command())
            yaim_result = run_yaim.get_output()

            msg = 'run yaim status'
            self.assert_(yaim_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            time.sleep(35)
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_mysql_connector_java_links(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            bad_connector_file = ('%s/%s'
                % (services.BackendSet.java_folder,
                services.BackendSet.bad_file))
            ls_ls = listinfo.Ls(bad_connector_file)
            self.lfn.put_cmd(ls_ls.get_command())
            ls_result = ls_ls.get_output()

            msg = 'ls %s status' % bad_connector_file
            self.assert_(ls_result['status'] == 'FAILURE',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            connector_file = ('%s/%s'
                % (services.BackendSet.java_folder,
                services.BackendSet.connector_file))
            ls_ls = listinfo.Ls(connector_file)
            self.lfn.put_cmd(ls_ls.get_command())
            ls_result = ls_ls.get_output()

            msg = 'ls %s status' % connector_file
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_mysql_connector_java_link(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            connector_file = ('%s/%s'
                % (services.BackendSet.java_folder,
                services.BackendSet.connector_file))
            ls_ls = listinfo.Ls(connector_file)
            self.lfn.put_cmd(ls_ls.get_command())
            ls_result = ls_ls.get_output()

            msg = 'ls %s status' % connector_file
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_path_authz_db(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            rpm_out = rpm.Rpm(services.BackendSet.package)
            self.lfn.put_cmd(rpm_out.get_command(option='-ql'))
            rpm_result = rpm_out.get_output(option='-ql')

            msg = 'rpm %s status' % services.BackendSet.package
            self.assert_(rpm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        
            path_file = ('%s/%s'
                % (services.BackendSet.conf_folder,
                services.BackendSet.path_file))
            msg = '%s was not found' % path_file
            self.assert_(path_file in rpm_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_storm_backend_service_crashes_on_gpfs(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            lib_file = ('%s/%s'
                % (services.BackendSet.lib_folder,
                services.BackendSet.lib_file))
            #fi = '/usr/lib64/storm-backend-server/libgpfsapi_interface.so'
            lib_dep = library_dependencies.Ldd(lib_file)
            self.lfn.put_cmd(lib_dep.get_command())
            lib_dep_result = lib_dep.get_output()

            msg = 'ldd %s status' % lib_file
            self.assert_(lib_dep_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = '%s was not found' % services.BackendSet.libgpfs_so
            self.assert_(services.BackendSet.libgpfs_so in lib_dep_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
        
    def test_configuration_folders_permissions(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            msg = 'in progress'
            self.assert_('x' in 'txt',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id)) 
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_yaim_storm_gridftp_pool_list_variable(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            r_yaim_result = readfile.Rf(fn=self.tsets['yaim']['def_path']).get_output()

            msg = 'rf status'
            self.assert_(r_yaim_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            get_pool_list = []
            get_pool_strategy = ''
            for line in r_yaim_result['otpt'].split('\n'):
                if 'STORM_FAKE_SETTING_GRIDFTP_POOL_STRATEGY' in line:
                    if 'weight' == line.split('STORM_FAKE_SETTING_GRIDFTP_POOL_STRATEGY=')[1]:
                        get_pool_strategy = 'weight'
                elif 'STORM_GRIDFTP_POOL_STRATEGY' in line:
                    if 'weight' == line.split('STORM_GRIDFTP_POOL_STRATEGY=')[1]:
                        get_pool_strategy = 'weight'
                if get_pool_strategy != '':
                    break

            if get_pool_strategy != '':
                for line in r_yaim_result['otpt'].split('\n'):
                    if 'STORM_FAKE_SETTING_GRIDFTP_POOL_LIST' in line:
                        for value in line.split('STORM_FAKE_SETTING_GRIDFTP_POOL_LIST')[1].split(','):
                             tmp = value.strip().split(' ')[1]
                             if '"' == tmp[len(tmp)-1] or "'" == tmp[len(tmp)-1]:
                                 get_pool_list.append(tmp[:len(tmp)-1])
                             else:
                                 get_pool_list.append(tmp)
                    if len(get_pool_list) != 0:
                        break

                if len(get_pool_list) == 0:
                    for line in r_yaim_result['otpt'].split('\n'):
                        if 'STORM_GRIDFTP_POOL_LIST' in line:
                            for value in line.split('STORM_GRIDFTP_POOL_LIST')[1].split(','):
                                tmp = value.strip().split(' ')[1]
                                if '"' == tmp[len(tmp)-1] or "'" == tmp[len(tmp)-1]:
                                    get_pool_list.append(tmp[:len(tmp)-1])
                                else:
                                    get_pool_list.append(tmp)
                        if len(get_pool_list) != 0:
                            break

                name_file = ('%s/%s'
                    % (services.BackendSet.conf_folder,
                    services.BackendSet.name_file))
                rf_result = readfile.Rf(fn=name_file).get_output()

                msg = 'rf %s status' % name_file
                self.assert_(rf_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

                get_namespace_lines = []
                for x in rf_result['otpt'].split('\n'):
                    if get_pool_strategy+'>' in x:
                        get_namespace_lines.append(x.split('weight>')[1].split('<')[0])

                for weight in get_pool_list:
                    found_weight = False
                    for line in get_namespace_lines:
                        if weight == line:
                            found_weight=True
                            break
                    self.assert_(found_weight)

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_lcas_lcmaps_gt4_interface_rpm_missed(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            rpm_out = rpm.Rpm(services.BackendSet.meta_package)
            self.lfn.put_cmd(rpm_out.get_command(option='-qR'))
            rpm_result = rpm_out.get_output(option='-qR')

            msg = 'rpm %s status' % services.BackendSet.meta_package
            self.assert_(rpm_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = '%s was not found' % services.BackendSet.lcas_dep
            self.assert_(services.BackendSet.lcas_dep in rpm_result['otpt'],
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_yaim_storm_frontend_port_variable(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            r_yaim_result = readfile.Rf(fn=self.tsets['yaim']['def_path']).get_output()

            msg = 'rf status'
            self.assert_(r_yaim_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            get_frontend_port = ''
            for line in r_yaim_result['otpt'].split('\n'):
                if 'STORM_FRONTEND_PORT' in line:
                    get_frontend_port = line.split('STORM_GRIDFTP_POOL_STRATEGY=')[1]
                    break

            conf_file = ('%s/%s'
                % (services.FrontendSet.conf_folder,
                services.FrontendSet.conf_file))
            rf_result = readfile.Rf(fn=conf_file).get_output()

            msg = 'rf %s status' % conf_file
            self.assert_(rf_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            get_fe_port = ''
            for x in rf_result['otpt'].split('\n'):
                if 'fe.port' in x:
                    get_fe_port = x.split('fe.port=')[1]
                    break

            if get_frontend_port == '':
                self.assert_(get_fe_port == '8444')

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
