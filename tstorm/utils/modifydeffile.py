#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
from tstorm.utils import utils

class MDeffile:
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
