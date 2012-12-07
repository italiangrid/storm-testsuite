__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class InfoSystem:
    def __init__(self, bh, ip, sad, attrs={}):
        self.behn = bh
        self.info_port = ip
        self.sa_descr = sad
        self.attrs = attrs
        self.cmd = {
            'name': 'curl',
            'protocol': 'http',
            'port': self.info_port
            }
        self.otpt = {
            'status':'',
            'busy-space':'',
            'used-space':'',
            'unavailable-space':'',
            'reserved-space':'',
            'total-space':'',
            'free-space':'',
            'available-space':''
            }

    def get_command(self, in_write=False):
        opt = ' -s '
        opt += self.cmd['protocol'] + '://' + self.behn + ':' + self.cmd['port']
        opt += '/info/status/' + self.sa_descr + '_TOKEN'

        if in_write is False:
            a = self.cmd['name'] + ' -X GET ' + opt
        else:
            s = ''

            for x in self.attrs.keys():
                s += x  + '=' + self.attrs[x]
                s += '&'

            opt += '/update?' + s[:-1]
            a = self.cmd['name'] + ' -X PUT ' + opt

        return a

    def run_command(self, in_write=False):
        a=()
        if utils.cmd_exist(self.cmd["name"]):
            a=commands.getstatusoutput(self.get_command(in_write=in_write))
        return a

    def get_output(self, in_write=False):
        a=self.run_command(in_write=in_write)
        if len(a) > 0 and a[0] == 0:
            for x in self.otpt:
                if x == 'status':
                    self.otpt[x] = 'PASS'
                else:
                    y = a[1].split('\n')
                    if x in y[0]:
                        self.otpt[x] = y[0].split('"'+x+'":')[1].split(',')[0].split('}}')[0]
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
