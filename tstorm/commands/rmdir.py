#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class SrmRmdir:
    def __init__(self, endpoint, accesspoint, dfn):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.dfn = dfn
        self.cmd = {
                   'name': 'srmrmdir',
                   'protocol': 'srm'}
        self.otpt = {
                    'status':[],
                    'path':[]}

    def get_command(self, pt):
        a=self.cmd['name'] + ' -2 -debug '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + pt
      
        return a

    def run_command(self, dtc):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(dtc))
        return a

    def get_output(self):  
        y=self.dfn
        while y != '/':
            a=self.run_command(y)
            self.otpt['path'].append(y)
            if len(a) > 0 and a[0] == 0:
                self.otpt['status'].append('PASS')
            else:
                self.otpt['status'].append('FAILURE')
            y=os.path.dirname(y)

        return self.otpt

class StoRMRmdir:
    '''StoRM Rmdir'''
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
            'status':[],
            'statusCode':[],
            'explanation':[]}

    def get_command(self, pt, wrong_request=False, wrong_option=False):
        #a = self.cmd['name'] + ' rmdir -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + pt
        a = self.cmd['name'] + ' rmdir '
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
        a += self.accesspoint + pt
        return a

    def run_command(self, dtc, wrong_request=False, wrong_option=False):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(dtc,
                wrong_request=wrong_request, wrong_option=wrong_option))
        return a

    def get_output(self, wrong_request=False, wrong_option=False):
        y=self.dst_filename
        while y != '/':
            a=self.run_command(y, wrong_request=wrong_request,
                wrong_option=wrong_option)
            if len(a) > 0 and a[0] == 0:
                if 'SRM_SUCCESS' in a[1]:
                    for x in self.otpt:
                        if x == 'status':
                            self.otpt['status'].append('PASS')
                        else:
                            yy = a[1].split('\n')
                            for z in yy:
                                if x in z:
                                    self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
                else:
                    self.otpt['status'].append('FAILURE')
            else:
                self.otpt['status'].append('FAILURE')
            y=os.path.dirname(y)

        return self.otpt
    

