#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Yaim:
    def __init__(self, backend=True, frontend=True, gridftp=True):
        self.be = backend
        self.fe = frontend
        self.gftp = gridftp
        self.cmd = {
                   'name':'yaim'}
        self.otpt = {
                   'status':''}

    def get_command(self):
        a = self.cmd['name'] + ' if=/dev/urandom of='+ self.ifn + ' bs=' + self.cmd['size'] + ' count=1'
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
        else:
            self.otpt['status'] = 'FAILURE'

        return self.otpt
