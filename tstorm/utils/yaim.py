#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class Yaim:
    def __init__(self, yaim_def, back_end='no', front_end='no', grid_ftp='no', grid_https='no'):
        self.be = back_end
        self.fe = front_end
        self.gftp = grid_ftp
        self.ghttps = grid_https
        self.yaim_def = yaim_def
        self.cmd = {
                   'name':'/opt/glite/yaim/bin/yaim'}
        self.otpt = {
                   'status':''}

    def get_command(self):
        node = ' '
        if self.be == 'yes':
            node += '-n se_storm_backend '
        if self.fe == 'yes':
            node += '-n se_storm_frontend '
        if self.gftp == 'yes':
            node += '-n se_storm_gridftp '
        if self.ghttps == 'yes':
            node += '-n se_storm_gridhttps '
        a = self.cmd['name'] + ' -c -d 6 -s ' + self.yaim_def + node + ' &> /dev/null'
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
    def __init__(self, fn, source_text, replace_text):
        self.ifn = fn
        self.source_text = source_text
        self.replace_text = replace_text
        self.otpt = {
                    'status':''}

    def replace_text_in_file(self, source, replace):
        try:
            f = open(self.ifn,'r')
            text = f.read()
            f.close 
            f1 = open(self.ifn,'w')
            f1.write(text.replace(source, replace))
            f1.close
            return 'PASS' 
        except IOError:
            return 'FAILURE'

    def get_output(self):
        source_replace_text = {}
        for x in self.source_text.keys():
            source_replace_text[x] = []
        for x in self.source_text.keys():
            source_replace_text[x].append('STORM_'+x+'_ONLINE_SIZE='+str(self.source_text[x]))
        for x in self.replace_text.keys():
            source_replace_text[x].append('STORM_'+x+'_ONLINE_SIZE='+str(self.replace_text[x]))
        for x in source_replace_text:
            self.otpt['status'] = self.replace_text_in_file(source_replace_text[x][0], source_replace_text[x][1])

        return self.otpt
