__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class RmLf:
    def __init__(self, fn='input-file', bfn='back-input-file'):
        self.ifn = fn
        self.bfn = bfn
        self.cmd = {
            'name': 'rm'}
        self.otpt = {
            'status':''}

    def get_command(self):
        if self.bfn != '':
            a = self.cmd['name'] + ' -f  ' + self.ifn + ' ' + self.bfn
        else:
            a = self.cmd['name'] + ' -f  ' + self.ifn
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
