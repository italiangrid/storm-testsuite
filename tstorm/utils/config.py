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
      #print 'read conf file %s' % self.conf_fn
      parser.read(self.conf_fn)
    except ConfigParser.ParsingError,err:
      print 'Could not parse:', err
   
    for section in parser.sections():
      self.test_sets[section] = {}
      #print 'Main key %s' % section
      for option in parser.options(section):
        self.test_sets[section][option]= parser.get(section,option)
        #print 'key %s: value %s' % (option, self.test_sets[section][option])

    return self.test_sets
