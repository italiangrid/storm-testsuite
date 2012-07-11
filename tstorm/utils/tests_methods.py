import sys
import os
from tstorm.utils import range_checks

class TestsMethods:
    def __init__(self, mti_info, storm_release, sequence=[]):
        self.methods = {}

        for key, value in mti_info.items():
            if 'ts' in key:
                if len(sequence) == 0 or \
                   value[0] in sequence:
                    for val in value[3]:
                       if range_checks.RangeChecks(self.storm_release, val[1]).is_valid():
                           self.methods[key] = (value[1], value[2], value[7])
                #elif value[0] in sequence:
                #    self.methods[key] = (value[1], value[2], value[7])
 
    def get_system_methods(self):
        system_methods = {}
        for key, value in self.methods.items():
            if 'DT' != value[0]:
                system_methods[key] = (value[0], value[1], value[2])
        return system_methods

    def get_sanity_methods(self):
        sanity_methods = {}
        for key, value in self.methods.items():
            if 'DT' == value[0]:
                sanity_methods[key] = (value[0], value[1], value[2]) 
        return sanity_methods
