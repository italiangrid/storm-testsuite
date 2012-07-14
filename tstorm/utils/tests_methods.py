import sys
import os
import random
from tstorm.utils import range
from tstorm.utils import test

class TestsMethods:
    def __init__(self, mti_info, release, sequence=[]):
        self.methods = {}

        for key, value in mti_info.items():
            if 'ts' in key:
                if len(sequence) == 0 or \
                    value[0] in sequence:
                    for val in value[3]:
                       if range.Range(val[1]).is_included(release):
                           test_structure = test.TestStructure(value, val[0], val[1])
                           if key in self.methods.keys():
                               self.methods[key+str(random.random())[0:5]] = test_structure
                           else:
                               self.methods[key] = test_structure
 
    def get_system_methods(self):
        system_methods = {}
        for key, value in self.methods.items():
            if 'DT' != value.get_test_type():
                system_methods[key] = value
        return system_methods

    def get_sanity_methods(self):
        sanity_methods = {}
        for key, value in self.methods.items():
            if 'DT' == value.get_test_type():
                sanity_methods[key] = value
        return sanity_methods
