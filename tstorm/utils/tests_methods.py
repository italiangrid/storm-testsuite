import sys
import os

class TestsMethods:
    def __init__(self, mti_info, sequence=[]):
        self.methods = {}

        for key, value in mti_info.items():
            if 'ts' in key:
                if len(sequence) == 0:
                    self.methods[key] = (value[1], value[2], value[8])
                elif value[0] in sequence:
                    self.methods[key] = (value[1], value[2], value[8])
 
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
