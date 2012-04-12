#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class LcgBol:
    def __init__(self, endpoint, accesspoint, dfn):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.dfn = dfn
        self.cmd = {
            'name': 'lcg-bringonline',
            'protocol': 'srm'}
        self.otpt = {
            'status':'',
            'requestToken':''}

    def get_command(self):
        a= self.cmd['name'] + ' -b --verbose -T srmv2 '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
        return a

    def run_command(self):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command())
        return a

    def get_output(self):
        a=self.run_command()
        if len(a) > 0 and a[0] == 0:
            for x in self.otpt:
                if x == 'status':
                    self.otpt['status'] = 'PASS'
                else:
                    y = a[1].split('\n')
                    for z in y:
                        if 'Token' in z:
                            self.otpt['requestToken']=z.split('Token:')[1].split(' ')[1]          
        else:
            self.otpt['status'] = 'FAILURE'
        return self.otpt

class SrmBol:
    def __init__(self, endpoint, accesspoint, dfn):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.dfn = dfn
        self.cmd = {
            'name': 'srm-bring-online',
            'protocol': 'srm'}
        self.otpt = {
            'status':'',
            'requestToken':''}

    def get_command(self):
        a= self.cmd['name'] + ' -2 -debug '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
        return a

    def run_command(self):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command())
        return a

    def get_output(self):
        a=self.run_command()
        if len(a) > 0 and a[0] == 0:
            for x in self.otpt:
                if x == 'status':
                    self.otpt['status'] = 'PASS'
                else:
                    y = a[1].split('\n')
                    for z in y:
                        if x in z:
                            self.otpt[x]=z.split(x)[1].split('= ')[1]
        else:
            self.otpt['status'] = 'FAILURE'
        return self.otpt

class StoRMBol:
    '''StoRM Bring Online'''
    def __init__(self, endpoint, accesspoint, dst_filename):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.dst_filename = dst_filename
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
        #a = self.cmd['name'] + ' bol -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn + ' -p'
        a = self.cmd['name'] + ' bol '
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
        a += ' -p'
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
                if 'SRM_NOT_SUPPORTED' in a[1]:
                    self.otpt['status'] = 'FAILURE'
                else:
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

class StoRMSbol:
    '''StoRM Status Of Bring Online Request'''
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
        #a = self.cmd['name'] + ' sbol -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dst_filename + ' -t ' + self.turl
        a = self.cmd['name'] + ' sbol '
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
                if 'SRM_NOT_SUPPORTED' in a[1]:
                    self.otpt['status'] = 'FAILURE'
                else:
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
