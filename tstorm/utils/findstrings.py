#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Grep:
    def __init__(self, fn='/var/log/storm/storm-frontend-server.log'):
        self.ifn = fn
        self.cmd = {
                   'name':'grep'
                   }
        self.ipt_strings = 'Cannot add or update a child row: a foreign key constraint fails'
        self.otpt = {
                    'status':''}

    def get_command(self):
        a = self.cmd['name'] + '"' + self.ipt_strings + '" ' + self.ifn
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
