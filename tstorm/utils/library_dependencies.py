__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Ldd:
    def __init__(self, library):
        self.library = library
        self.cmd = {
            'name':'ldd'
            }
        self.otpt = {
            'status':'',
            'otpt':''}

    def get_command(self):
        a = self.cmd['name']
        a += ' ' + self.pn
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
            self.otpt['otpt'] = a[1]
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
