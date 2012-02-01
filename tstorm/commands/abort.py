#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class StoRMAr:
    def __init__(self, endpoint, accesspoint, rtoken):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.rtoken = rtoken
        self.cmd = {
                   'name': 'clientSRM',
                   'rqst_protocol': 'httpg',
                   'protocol': 'srm'}
        self.otpt = {
                   'status':'',
                   'statusCode':[],
                   'explanation':[]}

    def get_command(self):
        a = self.cmd['name'] + ' ar -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -t ' + self.rtoken
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
