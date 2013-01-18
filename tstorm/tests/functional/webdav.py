__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
import inspect

from tstorm.utils import utils
from tstorm.utils import config
from tstorm.commands import curl

class WebdavTest(unittest.TestCase):
    def __init__(self, testname, tfn, ifn, dfn, bifn, uid, lfn):
        super(WebdavTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.ifn = ifn
        self.dfn = dfn
        self.bifn = bifn
        self.id = uid.get_id()
        self.lfn = lfn

    def test_webdav_get_directory_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['read_anonymous']))

            get_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(get_curl.get_command(operation='GET'))
            curl_result = get_curl.get_output(operation='GET')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_file_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_overwritten_file_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT', overwrite=True))
            curl_result = put_curl.get_output(operation='PUT', overwrite=True)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_body_in_file_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT', body=True, body_text='text file'))
            curl_result = put_curl.get_output(operation='PUT', body=True, body_text='text file')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_body_in_overwritten_file_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT', body=True, body_text='text file', overwrite=True))
            curl_result = put_curl.get_output(operation='PUT', body=True, body_text='text file', overwrite=True)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()


    def test_webdav_mkcol_directory_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(operation='MKCOL'))
            curl_result = mkcol_curl.get_output(operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(operation='DELETE'))
            curl_result = mkcol_curl.get_output(operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_file_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(operation='MKCOL'))
            curl_result = mkcol_curl.get_output(operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            delete_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(delete_curl.get_command(operation='DELETE'))
            curl_result = delete_curl.get_output(operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(operation='DELETE'))
            curl_result = mkcol_curl.get_output(operation='DELETE')
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_directory_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(operation='MKCOL'))
            curl_result = mkcol_curl.get_output(operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(operation='DELETE'))
            curl_result = mkcol_curl.get_output(operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_full_directory_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(operation='MKCOL'))
            curl_result = mkcol_curl.get_output(operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(operation='DELETE'))
            curl_result = mkcol_curl.get_output(operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_propfind_directory_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PROPFIND'))
            curl_result = put_curl.get_output(operation='PROPFIND')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_options_directory_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='OPTIONS'))
            curl_result = put_curl.get_output(operation='OPTIONS')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_copy_file_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(put_curl.get_command(operation='COPY', new_file=self.dfn+'x'))
            curl_result = put_curl.get_output(operation='COPY', new_file=self.dfn+'x')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_copy_full_directory_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(operation='MKCOL'))
            curl_result = mkcol_curl.get_output(operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            new_id = utils.get_uuid()
            self.lfn.put_cmd(mkcol_curl.get_command(operation='COPY', new_file='/test-'+new_id))
            curl_result = mkcol_curl.get_output(operation='COPY', new_file='/test-'+new_id)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_move_file_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(put_curl.get_command(operation='MOVE', new_file=self.dfn+'x'))
            curl_result = put_curl.get_output(operation='MOVE', new_file=self.dfn+'x')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_move_full_directory_over_http_as_anonymous(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('http://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['http_port'],
                self.tsets['http']['write_anonymous']))

            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(operation='MKCOL'))
            curl_result = mkcol_curl.get_output(operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(operation='PUT'))
            curl_result = put_curl.get_output(operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            new_id = utils.get_uuid()
            self.lfn.put_cmd(mkcol_curl.get_command(operation='MOVE', new_file='/test-'+new_id))
            curl_result = mkcol_curl.get_output(operation='MOVE', new_file='/test-'+new_id)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_get_directory_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            get_curl = curl.Curl(request_uri, self.ifn, self.dfn)
            self.lfn.put_cmd(get_curl.get_command(use_proxy=True, operation='GET'))
            curl_result = get_curl.get_output(use_proxy=True, operation='GET')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_file_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True, operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True, operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_overwritten_file_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True, operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True, operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True, operation='PUT', overwrite=True))
            curl_result = put_curl.get_output(use_proxy=True, operation='PUT', overwrite=True)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_body_in_file_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True, operation='PUT', body=True, body_text='text file'))
            curl_result = put_curl.get_output(use_proxy=True, operation='PUT', body=True, body_text='text file')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_body_in_overwritten_file_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True, operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True, operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True, operation='PUT', body=True, body_text='text file', overwrite=True))
            curl_result = put_curl.get_output(use_proxy=True, operation='PUT', body=True, body_text='text file', overwrite=True)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_mkcol_directory_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='DELETE'))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_file_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True, operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_proxy=True, operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True, operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True, operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            delete_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(delete_curl.get_command(use_proxy=True, operation='DELETE'))
            curl_result = delete_curl.get_output(use_proxy=True, operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True, operation='DELETE'))
            curl_result = mkcol_curl.get_output(use_proxy=True, operation='DELETE')
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_directory_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='DELETE'))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_full_directory_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='DELETE'))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_propfind_directory_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='PROPFIND'))
            curl_result = put_curl.get_output(use_proxy=True, operation='PROPFIND')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_options_directory_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='OPTIONS'))
            curl_result = put_curl.get_output(use_proxy=True,operation='OPTIONS')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_copy_file_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='COPY', new_file=self.dfn+'x'))
            curl_result = put_curl.get_output(use_proxy=True,operation='COPY', new_file=self.dfn+'x')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_copy_full_directory_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            new_id = utils.get_uuid()
            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='COPY', new_file='/test-'+new_id))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='COPY', new_file='/test-'+new_id)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_move_file_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='MOVE', new_file=self.dfn+'x'))
            curl_result = put_curl.get_output(use_proxy=True,operation='MOVE', new_file=self.dfn+'x')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_move_full_directory_over_https_with_voms(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['voms']))

            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_proxy=True,operation='PUT'))
            curl_result = put_curl.get_output(use_proxy=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            new_id = utils.get_uuid()
            self.lfn.put_cmd(mkcol_curl.get_command(use_proxy=True,operation='MOVE', new_file='/test-'+new_id))
            curl_result = mkcol_curl.get_output(use_proxy=True,operation='MOVE', new_file='/test-'+new_id)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_get_directory_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            get_curl = curl.Curl(request_uri, self.ifn, self.dfn)
            self.lfn.put_cmd(get_curl.get_command(use_cert=True, operation='GET'))
            curl_result = get_curl.get_output(use_cert=True, operation='GET')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_file_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True, operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True, operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_overwritten_file_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True, operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True, operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True, operation='PUT', overwrite=True))
            curl_result = put_curl.get_output(use_cert=True, operation='PUT', overwrite=True)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_body_in_file_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True, operation='PUT', body=True, body_text='text file'))
            curl_result = put_curl.get_output(use_cert=True, operation='PUT', body=True, body_text='text file')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_put_body_in_overwritten_file_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True, operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True, operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            #put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True, operation='PUT', body=True, body_text='text file', overwrite=True))
            curl_result = put_curl.get_output(use_cert=True, operation='PUT', body=True, body_text='text file', overwrite=True)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_mkcol_directory_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='DELETE'))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_file_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True, operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_cert=True, operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True, operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True, operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            delete_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(delete_curl.get_command(use_cert=True, operation='DELETE'))
            curl_result = delete_curl.get_output(use_cert=True, operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True, operation='DELETE'))
            curl_result = mkcol_curl.get_output(use_cert=True, operation='DELETE')
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_directory_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))
            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='MKCOL')
            
            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='DELETE'))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_delete_full_directory_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))
            id = utils.get_uuid()

            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='DELETE'))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='DELETE')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_propfind_directory_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='PROPFIND'))
            curl_result = put_curl.get_output(use_cert=True, operation='PROPFIND')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_options_directory_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='OPTIONS'))
            curl_result = put_curl.get_output(use_cert=True,operation='OPTIONS')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_copy_file_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='COPY', new_file=self.dfn+'x'))
            curl_result = put_curl.get_output(use_cert=True,operation='COPY', new_file=self.dfn+'x')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_copy_full_directory_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            new_id = utils.get_uuid()
            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='COPY', new_file='/test-'+new_id))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='COPY', new_file='/test-'+new_id)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_move_file_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            put_curl = curl.Curl(request_uri,self.ifn,self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='MOVE', new_file=self.dfn+'x'))
            curl_result = put_curl.get_output(use_cert=True,operation='MOVE', new_file=self.dfn+'x')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_webdav_move_full_directory_over_https_with_user_cert(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            request_uri = ('https://%s:%s/%s'
                % (self.tsets['general']['gridhttp_server_hostname'],
                self.tsets['general']['https_port'],
                self.tsets['https']['site']))

            id = utils.get_uuid()
            mkcol_curl = curl.Curl(request_uri,self.ifn,'/test-'+id)
            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='MKCOL'))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='MKCOL')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            put_curl = curl.Curl(request_uri,self.ifn,'/test-'+id+self.dfn)
            self.lfn.put_cmd(put_curl.get_command(use_cert=True,operation='PUT'))
            curl_result = put_curl.get_output(use_cert=True,operation='PUT')

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            new_id = utils.get_uuid()
            self.lfn.put_cmd(mkcol_curl.get_command(use_cert=True,operation='MOVE', new_file='/test-'+new_id))
            curl_result = mkcol_curl.get_output(use_cert=True,operation='MOVE', new_file='/test-'+new_id)

            msg = 'curl status'
            self.assert_(curl_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
