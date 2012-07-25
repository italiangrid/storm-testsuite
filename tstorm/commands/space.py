__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class StoRMRs:
    '''StoRM Reserve Space'''
    def __init__(self, endpoint, accesspoint, space_token_descr):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.space_token_descr = space_token_descr
        self.cmd = {
            'name': 'clientSRM',
            'rqst_protocol': 'httpg',
            'port': '8444'}
        self.wrong_request = {
            'port': '8443'}
        self.otpt = {
            'status':'',
            'statusCode':[],
            'explanation':[],
            'spaceToken': ''}

    def get_command(self, wrong_request=False, wrong_option=False):
        a = self.cmd['name'] + ' rs '
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
        a += ' -d ' + self.space_token_descr 
        a += ' -r 0,0 -a 1000000 '
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
                    elif x == 'spaceToken':
                        self.otpt['spaceToken'] =a[1].split('spaceToken')[1].split('"')[1]
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

class StoRMGst:
    '''StoRM Get Space Token'''
    def __init__(self, endpoint, accesspoint, space_token_descr):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.space_token_descr = space_token_descr
        self.cmd = {
            'name': 'clientSRM',
            'rqst_protocol': 'httpg',
            'port': '8444'}
        self.wrong_request = {
            'port': '8443'}
        self.otpt = {
            'status':'',
            'statusCode':[],
            'explanation':[],
            'arrayOfSpaceTokens': ''}

    def get_command(self, wrong_request=False, wrong_option=False):
        #a = self.cmd['name'] + ' gst  -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -d ' + self.st_descr
        a = self.cmd['name'] + ' gst '
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
        a += ' -d ' + self.space_token_descr
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
                    elif x == 'arrayOfSpaceTokens':
                        self.otpt['arrayOfSpaceTokens'] =a[1].split('arrayOfSpaceTokens')[1].split('"')[1] 
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

class StoRMGsm:
    '''StoRM Get Space Token'''
    def __init__(self, endpoint, accesspoint, space_token_id):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.space_token_id = space_token_id
        self.cmd = {
            'name': 'clientSRM',
            'rqst_protocol': 'httpg',
            'port': '8444'}
        self.wrong_request = {
            'port': '8443'}
        self.otpt = {
            'status':'',
            'statusCode':[],
            'explanation':[],
            'unusedSize': ''}

    def get_command(self, wrong_request=False, wrong_option=False):
        a = self.cmd['name'] + ' gsm '
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
        a += ' -s ' + self.space_token_id
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
                    elif x == 'unusedSize':
                        self.otpt['unusedSize'] =a[1].split('unusedSize')[1].split('=')[1].split('\n')[0]
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
