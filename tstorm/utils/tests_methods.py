import sys
import os
import random

class TestsMethods:
    def __init__(self, tests):
        self.tests = tests
 
    def get_methods(self):
        system_methods = {}
        for key, value in self.tests.items():
            if 'DT' != value.get_test_type():
                methods[key] = value
        return methods

    def get_sanity_methods(self):
        sanity_methods = {}
        for key, value in self.methods.items():
            if 'DT' == value.get_test_type():
                sanity_methods[key] = value
        return sanity_methods
