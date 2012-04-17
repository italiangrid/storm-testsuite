__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class StoRMAf:
    '''StoRM Abort File'''
    def __init__(self, endpoint, accesspoint, dst_filename, request_token):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.dst_filename = dst_filename
        self.request_token = request_token
        self.cmd = {
            'name': 'clientSRM',
            'rqst_protocol': 'httpg',
            'protocol': 'srm',
            'port': '8444'}
        self.wrong_request = {
            'port': '8443'}
        self.otpt = {
            'status':'',
            'statusCode':[],
            'explanation':[]}

    def get_command(self, wrong_request=False, wrong_option=False):
        a = self.cmd['name'] + ' af '
        if wrong_option:
            a += '-f '
        else:
            a += '-e '
        if wrong_request:
            a += self.cmd['rqst_protocol'] + '://'
            a += self.endpoint + ':' + self.wrong_request['port'] + '/'
        else:
            a += self.cmd['rqst_protocol'] + '://'
            a += self.endpoint + ':' + self.cmd['port'] + '/'
        a += ' -s ' + self.cmd['protocol'] + '://' 
        a += self.endpoint + ':' + self.cmd['port'] + '/srm/managerv2?SFN=/'
        a += self.accesspoint + self.dst_filename
        a += ' -t ' + self.request_token
        return a

    def run_command(self, wrong_request=False, wrong_option=False):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(
                wrong_request=wrong_request,
                wrong_option=wrong_option))
        return a

    def get_output(self, wrong_request=False, wrong_option=False):
        a=self.run_command(wrong_request=wrong_request,
            wrong_option=wrong_option)
        if len(a) > 0 and a[0] == 0:
            if 'SRM_SUCCESS' in a[1]:
                for x in self.otpt:
                    if x == 'status':
                        self.otpt['status'] = 'PASS'
                    else:
                        y = a[1].split('\n')
                        for z in y:
                            if x in z:
                                self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
            else:
                self.otpt['status'] = 'FAILURE'
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt

class StoRMAr:
    '''StoRM Abort Request'''
    def __init__(self, endpoint, accesspoint, request_token):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.request_token = request_token
        self.cmd = {
            'name': 'clientSRM',
            'rqst_protocol': 'httpg',
            'port': '8444'}
        self.wrong_request = {
            'port': '8443'}
        self.otpt = {
            'status':'',
            'statusCode':[],
            'explanation':[]}

    def get_command(self, wrong_request=False, wrong_option=False):
        #a = self.cmd['name'] + ' ar -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -t ' + self.rtoken
        a = self.cmd['name'] + ' ar '
        if wrong_option:
            a += '-f '
        else:
            a += '-e '
        if wrong_request:
            a += self.cmd['rqst_protocol'] + '://'
            a += self.endpoint + ':' + self.wrong_request['port'] + '/'
        else:
            a += self.cmd['rqst_protocol'] + '://'
            a += self.endpoint + ':' + self.cmd['port'] + '/'
        a += ' -t ' + self.request_token
        return a

    def run_command(self, wrong_request=False, wrong_option=False):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(
                wrong_request=wrong_request,
                wrong_option=wrong_option))
        return a

    def get_output(self, wrong_request=False, wrong_option=False):
        a=self.run_command(wrong_request=wrong_request,
            wrong_option=wrong_option)
        if len(a) > 0 and a[0] == 0:
            if 'SRM_SUCCESS' in a[1]:
                for x in self.otpt:
                    if x == 'status':
                        self.otpt['status'] = 'PASS'
                    else:
                        y = a[1].split('\n')
                        for z in y:
                            if x in z:
                                self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
            else:
                self.otpt['status'] = 'FAILURE'
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
