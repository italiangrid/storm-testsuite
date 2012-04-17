__author__ = 'Elisabetta Ronchieri'

import ConfigParser
import os

class TestSettings:
    def __init__(self, conf='/etc/tstorm.ini'):
        self.conf_fn = conf
        self.test_sets = {}

    def get_test_sets(self):
        parser = ConfigParser.ConfigParser()
        try:
            parser.read(self.conf_fn)
        except ConfigParser.ParsingError,err:
            print 'Could not parse:', err
   
        for section in parser.sections():
            self.test_sets[section] = {}
            for option in parser.options(section):
                self.test_sets[section][option]= parser.get(section,option)

        return self.test_sets
