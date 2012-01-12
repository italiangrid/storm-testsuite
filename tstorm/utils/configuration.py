#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import ConfigParser
import os

class LoadConfiguration:
    def __init__(self, conf='/etc/tstorm.ini'):
        self.configuration_file = conf
        self.sections = {'general':'', 
            'ping':'', 
            'https':'',
            'http':'',
            'tape':'',
            'bdii':'',
            'yaim':'',
            'log':'',
            'node':'']

    def get_test_settings(self):
        '''Returns test settings'''

        parser = ConfigParser.ConfigParser()
        
        test_settings = {}

        try:
            parser.read(self.conf_fn)
        
            sections = parser.sections()
    
            if len(sections) <= len(self.sections.keys()):
                if sections in self.sections.keys():
                    for section in sections:
                        test_settings[section] = {}
                        for option in parser.options(section):
                            test_settings[section][option] = parser.get(section, option)
                     
        except ConfigParser.ParsingError, err:
            print 'Could not parse:', err
   
        print test_settings

        return test_settings
