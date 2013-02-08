__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class LcgLs:
    def __init__(self, endpoint, accesspoint, dfn):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.dfn = dfn
        self.cmd = {
            'name': 'lcg-ls',
            'protocol': 'srm'}
        self.otpt = {
            'status':'',
            'Checksum': '',
            'fileLocality': ''}

    def get_command(self):
        a= self.cmd['name'] + ' -l -b -D srmv2 '+ self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dfn
        return a

    def run_command(self):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command())
        return a

    def get_output(self):
        a=self.run_command()
        if len(a) > 0 and a[0] == 0:
            self.otpt['status'] = 'PASS'
            x=a[1].split('\n')
            k=self.otpt.keys()
            for y in x:
                if 'ONLINE_AND_NEARLINE' in y:
                    self.otpt['fileLocality']='ONLINE_AND_NEARLINE'
                elif 'ONLINE' in y:
                    self.otpt['fileLocality']='ONLINE'
                elif 'NEARLINE' in y:
                    self.otpt['fileLocality']='NEARLINE'
                elif 'Checksum' in y:
                    self.otpt['Checksum'] = y.split(':')[1][1:]
        else:
            self.otpt['status'] = 'FAILURE'
        return self.otpt

class StoRMLs:
    '''StoRM LS'''
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
            'explanation':[],
            'fileLocality':'',
            'checkSumType':'',
            'checkSumValue':''}
        self.map = {
            '0': 'ONLINE',
            '1': 'NEARLINE',
            '2': 'ONLINE_AND_NEARLINE'}

    def get_command(self, wrong_request=False, wrong_option=False):
        a = self.cmd['name'] + ' ls '
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
        a += self.accesspoint + self.dst_filename + ' -l'
        return a

    def run_command(self, wrong_request=False, wrong_option=False):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(
                wrong_request=wrong_request, wrong_option=wrong_option))
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
                              if x == 'fileLocality':
                                  self.otpt[x] = self.map[z.split(x)[1].split('=')[1]]
                              elif x in ('checkSumType', 'checkSumValue'):
                                  self.otpt[x] = z.split(x)[1].split('="')[1].split('"')[0]
                              else:
                                  self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
            else:
                self.otpt['status'] = 'FAILURE'
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt

class Ls:
    def __init__(self, fn='input-file'):
        self.ifn = fn
        self.cmd = {
            'name':'ls'}
        self.otpt = {
            'status':'',
            'size':''}

    def get_command(self):
        a = self.cmd['name'] + ' -al '+ self.ifn
        return a

    def run_command(self):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command())
        return a

    def get_output(self):
        a=self.run_command()
        if a[0] == 0:
            self.otpt['status'] = 'PASS'
            self.otpt['size'] = a[1].split(' ')[4]
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
