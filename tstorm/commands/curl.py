__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Curl:
    def __init__(self, request_uri, ifn, dfn):
        self.request_uri = request_uri
        self.ifn = ifn
        self.dfn = dfn
        self.cmd = {
            'name': 'curl'}
        self.otpt = {
            'status':'',
            'value':''}
        self.state,self.p_path=utils.get_proxy_path()

    def get_command(self, use_cert=False, use_proxy=False, operation='GET', body=False, body_text='', overwrite=False):
        cmd = self.cmd['name']
        if use_proxy:
            ssl_opt=(' --cacert $HOME/.globus/usercert.pem --cert %s'
                % self.p_path +
                ' --capath /etc/grid-security/certificates ')
        elif use_cert:
            ssl_opt=(' --cert $HOME/.globus/usercert.pem --key $HOME/.globus/userkey.pem'
                +
                ' --capath /etc/grid-security/certificates ')
        else:
            ssl_opt=' '
      
        cmd += ' -v %s' % ssl_opt

        if operation == 'GET':
            cmd += ' -X GET %s' % self.request_uri
        elif operation == 'PUT':
            if body:
               cmd += ' -X PUT %s %s%s' % (self.ifn, self.request_uri, self.dfn)
            else:
               cmd += ' -T %s %s%s' % (self.ifn, self.request_uri, self.dfn)
            if body:
                cmd += ' --data-ascii "%s"' % body_text
            if overwrite:
                cmd += ' --header "Overwrite: T"'
        elif operation == 'MKCOL':
            cmd += ' -X MKCOL %s%s' % (self.request_uri, self.dfn)
        elif operation == 'DELETE':
            cmd += ' -X DELETE %s%s' % (self.request_uri, self.dfn)
        return cmd

    def run_command(self, use_cert=False, use_proxy=False, operation='GET', body=False, body_text='', overwrite=False):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(use_cert=use_cert, use_proxy=use_proxy, operation=operation, body=body, body_text=body_text, overwrite=overwrite))
        return a

    def get_output(self, use_cert=False, use_proxy=False, operation='GET', body=False, body_text='', overwrite=False):
        if self.state == 'FAILURE':
            self.otpt['status'] = self.state
            return self.otpt

        a=self.run_command(use_cert=use_cert, use_proxy=use_proxy, operation=operation, body=body, body_text=body_text, overwrite=overwrite)
        if len(a) > 0 and a[0] == 0:
            if 'HTTP/1.1 200 OK' in a[1]:
                self.otpt['status'] = 'PASS'
            elif 'HTTP/1.1 201 Created' in a[1]:
                self.otpt['status'] = 'PASS'
            elif 'HTTP/1.1 204 No Content' in a[1]:
                self.otpt['status'] = 'PASS'
            else:
                self.otpt['status'] = 'FAILURE'
            self.otpt['value'] = a[1]
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt

