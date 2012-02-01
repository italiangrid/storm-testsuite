#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import ConfigParser
import os

class LoadConfiguration:
    def __init__(self, conf_file = 'tstorm.ini'):
        self.configuration_file = conf_file
        self.parser = ConfigParser.ConfigParser()
        self.sections = {
            'ping':{'versioninfo':'',
                'backend_type':'',
                'backend_version':''},
            'general':{'endpoint':'',
                'accesspoint':'',
                'spacetoken':'',
                'gridftp_server_hostname':'',
                'gridhttp_server_hostname':'',
                'http_port':'',
                'https_port':'',
                'backend_hostname':'',
                'info_port':''},
            'https':{'no_voms':'',
                'voms':'',
                'no_auth':'',
                'sftn':''},
            'http':{'no_voms':'',
                'voms':''},
            'tape':{'accesspoint':''},
            'bdii':{'endpoint':'',
                'basedn':'',
                'glue_two_basedn':''},
            'yaim':{'def_path':''},
            'log':{},
            'node':{'backend':'',
                'frontend':'',
                'gridftp':'',
                'gridhttps':''}}

    def __get_sections(self):
        '''Returns sections'''

        try:
            self.parser.read(self.configuration_file)
        except ConfigParser.ParsingError, err:
            print 'Could not parse:', err

        sections = self.parser.sections()

        return sections

    def is_configuration_file_valid(self):
        '''Verify correctness of the configuration file'''
 
        sections = self.__get_sections()

        for section in sections:
            if section not in self.sections.keys():
                return False
            else:
               for option in self.parser.options(section):
                   if option not in self.sections[section].keys():
                       return False
   
        return True

    def get_test_settings(self):
        '''Returns test settings'''

        test_settings = {}

        sections = self.__get_sections()

        for section in sections:
            test_settings[section] = {}
            for option in self.parser.options(section):
                test_settings[section][option] = self.parser.get(section, option)
   
        return test_settings

    def print_configuration_file_template(self):
        '''Print Test Configuration Information from the configuration template file'''

        config_file_template = '\n'
        for section in self.sections.keys():
            config_file_template = config_file_template + '[' + section + ']\n'
            for option in self.sections[section].keys():
                config_file_template = config_file_template + option + '=<...>\n'
            config_file_template = config_file_template + '\n'

        print config_file_template
