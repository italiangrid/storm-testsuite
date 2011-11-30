#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Mysql:
    def __init__(self, db_name, db_table, db_field, db_host, value, db_user='storm', db_pwd='storm'):
        self.ifn = fn
        self.cmd = {
                   'name':'mysql'}
        self.otpt = {
                   'status':''}

    def get_command(self):
        a = self.cmd['name'] + ' if=/dev/urandom of='+ self.ifn + ' bs=' + self.cmd['size'] + ' count=1'        
        mysql -u storm -h omii005-vm01.cnaf.infn.it -s storm_be_ISAM --password=storm -e 'select total_size, available_size from storage_space where alias = "DTEAM_TOKEN"'
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
