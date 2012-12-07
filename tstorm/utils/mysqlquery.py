__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Mysql:
    def __init__(self, db_name, db_table, db_field, db_host, token, db_user='storm', db_pwd='storm'):
        self.db = {
            'name': db_name,
            'table': db_table,
            'host': db_host,
            'user': db_user,
            'pwd': db_pwd,
            'field': db_field
            }
        self.storage_space = ['total_size', 'available_size', 'free_size']
        self.cmd = {
            'name':'mysql'}
        self.otpt = {
            'status':[],
            'token':{}}
        self.token = token

    def get_command(self, alias_value):
        s = ''

        for x in self.db['field']:
            s += x
            s += ','
        
        opt = ' -u ' + self.db['user']
        opt += ' -h ' + self.db['host']
        opt += ' -s ' + self.db['name']
        opt += ' --password=' + self.db['pwd']
        query = " -e 'select "
        query += s[:-1]
        query += ' from ' + self.db['table'] + ' where alias = ' + '"' + alias_value + '"' + "'"
        a = self.cmd['name'] + opt + query     

        return a

    def run_command(self, alias):
        a=()
        if utils.cmd_exist(self.cmd['name']):
            a=commands.getstatusoutput(self.get_command(alias))
        return a

    def get_output(self):
        for x in self.token:
            a=self.run_command(self.token[x])
            #print 'mysql ', a
            if a[0] == 0:
                self.otpt['status'].append('PASS')
                y=a[1].split('\n')[0].split('\t')
                self.otpt['token'][self.token[x]]=[]
                for z in y:
                    self.otpt['token'][self.token[x]].append(z)
            else:
                self.otpt['status'].append('FAILURE')

        return self.otpt
