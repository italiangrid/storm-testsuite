__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class SrmRm:
    def __init__(self, endpoint, accesspoint, dfn):
        self.endpoint = endpoint
        self.accesspoint = accesspoint
        self.dfn = dfn
        self.cmd = {
            'name': 'srmrm',
            'protocol': 'srm'}
        self.otpt = {
            'status':'',
            'VersionInfo': '',
            'backend_type': '',
            'backend_version': ''}

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
            self.otpt['status'] = 'PASS'
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt

class StoRMRm:
    '''StoRM RM'''
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
        #a = self.cmd['name'] + ' rm -e ' + self.cmd['rqst_protocol'] + '://' + self.endpoint + ':8444/' + ' -s ' + self.cmd['protocol'] + '://' + self.endpoint + ':8444/srm/managerv2?SFN=/' + self.accesspoint + self.dst_filename
        a = self.cmd['name'] + ' rm '
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
                                self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
            else:
                self.otpt['status'] = 'FAILURE'
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
