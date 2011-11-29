#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class StoRMGst:
    def __init__(self, endpoint, accesspoint, st_descr):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.st_descr = st_descr
        self.cmd = {
                   'name': 'clientSRM',
                   'rqst_protocol': 'httpg'}
        self.otpt = {
                    'status':'',
                    'statusCode':[],
                    'explanation':[],
                    'arrayOfSpaceTokens': ''}

    def get_command(self):
        a = self.cmd['name'] + ' gst  -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -d ' + self.st_descr
        
        return a

    def run_command(self):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command())
        return a

    def get_output(self):
        a=self.run_command()
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
    def __init__(self, endpoint, accesspoint, st_id):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.st_id = st_id
        self.cmd = {
                   'name': 'clientSRM',
                   'rqst_protocol': 'httpg'}
        self.otpt = {
                   'status':'',
                   'statusCode':[],
                   'explanation':[],
                   'unusedSize': ''}

    def get_command(self):
        a = self.cmd['name'] + ' gsm -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.st_id
  
        return a

    def run_command(self):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command())
        return a

    def get_output(self):
        a=self.run_command()
        if len(a) > 0 and a[0] == 0:
            if 'SRM_SUCCESS' in a[1]:
                for x in self.otpt:
                    if x == 'status':
                        self.otpt['status'] = 'PASS'
                    elif x == 'unusedSize':
                        self.otpt['unusedSize'] =a[1].split('unusedSize')[1].split('=')[1].split('\n')[0]
                    else:
                        y = a[1].split('\n')
            else:
                self.otpt['status'] = 'FAILURE'
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
