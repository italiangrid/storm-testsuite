__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Rpm:
    def __init__(self, pn):
        self.pn = pn
        self.cmd = {
            'name':'rpm'}
        self.otpt = {
            'status':'',
            'otpt':''}

    def get_command(self, option='-qa'):
        a = self.cmd['name']
        if option == '-qa':
            a += ' ' + option + ' | grep '
        elif option in ('-ql', '-qr'):
            a += ' ' + option + ' '
        a += self.pn
        return a

    def run_command(self, option='-qa'):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(option=option))
        return a

    def get_output(self, option='-qa'):
        a=self.run_command(option=option)
        if a[0] == 0:
            self.otpt['status'] = 'PASS'
            self.otpt['otpt'] = a[1]
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
