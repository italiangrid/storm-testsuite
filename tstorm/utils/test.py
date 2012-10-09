import sys
import os
import exceptions

class TestStructureError(exceptions.Exception):
    pass

class TestStructure:
    def __init__(self, value, rfc, range):
        if len(value) == 0:
            raise TestStructureError('Test structure is empty')
        elif len(value) > 8:
            raise TestStructureError('Test structure is not correct')
        self.id = value[0]
        self.type = value[1]
        self.regression = value[2]
        self.rfc = rfc
        self.range = range
        self.idenpotent = value[4]
        self.name = value[5]
        self.description = value[6]
        self.aggregator = value[7]

    def get_id(self):
        return self.id

    def get_test_type(self):
        return self.type
                
    def is_regression(self):
        return self.regression

    def get_rfc(self):
        return self.rfc

    def get_range(self):
        return self.range

    def is_idenpotent(self):
        return self.idenpotent

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_aggregator(self):
        return self.aggregator
