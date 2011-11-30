#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Mysql:
    def __init__(self, db_name, db_table, db_field, db_host, value, token, db_user='storm', db_pwd='storm'):
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
                   'token':[],
                   'value':{}}
        self.value = value
        self.token = token

    def get_command(self, alias):
        s = ''

        for x in self.db['field']:
            s += x
            s += ','
        
        opt = ' -u ' + self.db['user']
        opt += ' -h ' + self.db['host']
        opt += ' -s ' + self.db['name']
        opt += ' --passwrod=' + self.db['pwdname']
        query = ' -e '
        query += "'select " + s[:-1]
        query += ' from ' + self.db['table'] + ' where alias = ' + '"DTEAM_TOKEN"' + "'"
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
            self.otpt['token'].append(x)
            if a[0] == 0:
                self.otpt['status'].append('PASS')
                y=a[1].split('\n')[0].split(' ')
                for z in self.db['field']:
                    self.otpt['value'][z] = y[z.index()]
            else:
                self.otpt['status'].append('FAILURE')
                

        return self.otpt

            if len(a) > 0 and a[0] == 0:
                if 'SRM_SUCCESS' in a[1]:
                    for x in self.otpt:
                        if x == 'status':
                            self.otpt['status'].append('PASS')
                        else:
                            yy = a[1].split('\n')
                            for z in yy:
                                if x in z:
                                    self.otpt[x].append(z.split(x)[1].split('="')[1].split('"')[0])
                else:
                    self.otpt['status'].append('FAILURE')
            else:
                self.otpt['status'].append('FAILURE')
            y=os.path.dirname(y)
