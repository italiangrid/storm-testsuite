__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Rpm:
    def __init__(self, pn):
        self.pn = pn
        self.cmd = {
            'name':'rpm',
            'package':' -qa ',
            'conffile':' -qc '}
        self.otpt = {
            'status':'',
            'otpt':''}

    def get_command(self, conffile=False):
        a = self.cmd['name']
        if conffile:
            a += self.cmd['conffile'] 
        else:
            a += self.cmd['package'] + '| grep '
        a += self.pn
        return a

    def run_command(self, conffile=False):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(conffile=conffile))
        return a

    def get_output(self, conffile=False):
        a=self.run_command(conffile=conffile)
        if a[0] == 0:
            self.otpt['status'] = 'PASS'
            self.otpt['otpt'] = a[1]
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
