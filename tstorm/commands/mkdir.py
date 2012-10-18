__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class SrmMkdir:
    def __init__(self, endpoint, accesspoint, dfn):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.dfn = dfn
        self.cmd = {
            'name': 'srmmkdir',
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
        dtc=self.dfn.split('/')
        dtc=dtc[1:]
        y='/'
        for x in dtc:
            if x != '':
                a=self.run_command(y + x)
                y = y + x + '/'
                self.otpt['path'].append(y)
                if len(a) > 0 and a[0] == 0:
                    self.otpt['status'].append('PASS')
                else:
                    self.otpt['status'].append('FAILURE')

        return self.otpt

class StoRMMkdir:
    '''StoRM Mkdir'''
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
            'path':[],
            'status':[],
            'statusCode':[],
            'explanation':[]}

    def get_command(self, pt, wrong_request=False, wrong_option=False):
        #a = self.cmd['name'] + ' mkdir -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + pt
        a = self.cmd['name'] + ' mkdir '
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
        dtc=self.dst_filename.split('/')
        dtc=dtc[1:]
        y='/'
        for x in dtc:
            if x != '':
                a=self.run_command(y + x, wrong_request=wrong_request,
                    wrong_option=wrong_option)
                y = y + x + '/'
                self.otpt['path'].append(y)
                if len(a) > 0 and a[0] == 0:
                    if 'SRM_SUCCESS' in a[1]:
                        for w in self.otpt:
                            if w == 'status':
                                self.otpt['status'].append('PASS')
                            else:
                                yy = a[1].split('\n')
                                for z in yy:
                                    if w in z:
                                        self.otpt[w].append(z.split(w)[1].split('="')[1].split('"')[0])
                    else:
                        self.otpt['status'].append('FAILURE')
                else:
                    self.otpt['status'].append('FAILURE')

        return self.otpt 
