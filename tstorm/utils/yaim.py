#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Yaim:
    def __init__(self, yaim_def, back_end=False, front_end=False, grid_ftp=False, grid_https=False):
        self.be = back_end
        self.fe = front_end
        self.gftp = grid_ftp
        self.ghttps = grid_https
        self.yaim_def = yaim_def
        self.cmd = {
                   'name':'yaim'}
        self.otpt = {
                   'status':''}

    def get_command(self):
        node = ' '
        if self.be is True:
            node += '-n se_storm_backend '
        if self.fe is True:
            node += '-n se_storm_frontend '
        if self.gftp is True:
            node += '-n se_storm_gridftp '
        if self.ghttps is True:
            node += '-n se_storm_gridhttps '
        a = self.cmd['name'] + ' -c -d 6 -s ' + self.yaim_dev + node
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

class ModifyDeffile:
    def __init__(self, source_text, replace_text, fn):
        self.ifn = fn
        self.source_text = source_text
        self.replace_text = replace_text
        self.otpt = {
                    'status':''}

    def get_output(self):
        try:
            f = open(self.ifn,'r')
            text = f.read()
            f.close()
            f = open(self.ifn,'w')
            source_replace_text = {}
            for x in self.source_text.keys():
                source_replace_text[x] = []
            for x in self.source_text.keys():
                source_replace_text[x].append(x+'='+str(self.source_text[x]))
            for x in self.replace_text.keys():
                source_replace_text[x].append(x+'='+str(self.replace_text[x]))
            for x in source_replace_text:
                f.write(text.replace(source_replace_text[x][0], source_replace_text[x][1])
            f.close()
            self.otpt['status'] = 'PASS'
        except IOError:
            self.otpt['status'] = 'FAILURE'
            pass

        return self.otpt
