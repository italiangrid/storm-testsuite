import sys
import os
from tstorm.utils import range
from tstorm.utils import test

class TestsError:
    def __init__(self, msg):
        self.args = msg
        self.errmsg = msg

class Tests:
    def __init__(self, data):
        self.list_keys = {
           'i':'get_id()', 'id':'get_id()',
           't':'get_test_type()', 'type':'get_test_type()',
           'r':'is_regression()', 'regression':'is_regression()',
           'rfc':'get_rfc()',
           'idenpotent':'is_idenpotent()',
           'range':'get_range()',
           'n':'get_name()', 'name':'get_name()',
           'd':'get_description()', 'description':'det_description()'}

        self.data = data
        self.tests = {}
        for key, value in data().items():
             for val in value[3]:
                 if range.Range(val[1]).is_included(release):
                     test_structure = test.TestStructure(value, val[0], val[1])
                     if key in self.tests.keys():
                         self.tests[key+str(random.random())[0:5]] = test_structure
                     else:
                         self.tests[key] = test_structure

    def __print_all_ids(self):
        print 'ID      RFC'
        for key, value in self.tests.items():
            if value.get_test_type() != 'DT':
                print '%s  %s' % (value.get_test_type(), value.get_rfc())

    def __print_all_sanity_ids(self):
        print 'ID      RFC'
        for key, value in self.tests.items():
            if value.get_test_type() == 'DT':
                print '%s  %s' % (value.get_test_type(), value.get_rfc())

    def __build_header_format(self, info):
        if len(info) == 0:
            raise TestsError('Input is wrong')
        elif not type(info) is dict:
            raise TestsError('Input is wrong')
        elif 'f' not in info.keys():
            print 'ID      RFC'
        else:
            msg = ''
            for x in info['f']:
                msg += x + '       '
            print msg

    def __build_body_format(self, value, info):
        if len(info) == 0:
            raise TestsError('Input is wrong')
        elif not type(info) is dict:
            raise TestsError('Input is wrong')
        elif 'f' not in info.keys():
            print '%s  %s' % (value.get_test_type(), value.get_rfc())
        else:
            msg = ''
            for x in info['f']:
                msg += eval(value.list_keys[x]) + '  '
            print msg

    def __print_with_filters(self, info={}):
        filter_info = []
        if 't' in info.keys() and 'r' in info.keys() and 'i' in info.keys():
            self.__build_header_format(info)
            for key, value in self.tests.items():
                for x in info['t']:
                    if x == value.get_test_type() and \
                        str(info['r']).lower() == str(value.get_regression()).lower() and \
                        str(info['i']).lower() == str(value.get_idenpotent()).lower():
                        filter_info.append(value.get_id())
                        self.__build_body_format(value, info)
        elif 't' in info.keys() and 'r' in info.keys():
            self.__build_header_format(info)
            for key, value in self.tests.items():
                for x in info['t']:
                    if x == value.get_test_type() and \
                        str(info['r']).lower() == str(value.get_regression()).lower():
                        filter_info.append(value.get_id())
                        self.__build_body_format(value, info)
        elif 't' in info.keys() and 'i' in info.keys():
            self.__build_header_format(info)
            for key, value in self.tests.items():
                for x in info['t']:
                    if x == value.get_test_type() and \
                        str(info['i']).lower() == str(value.get_idenpotent()).lower():
                        filter_info.append(value.get_id())
                        self.__build_body_format(value, info)
        elif 'r' in info.keys() and 'i' in info.keys():
            self.__build_header_format(info)
            for key, value in self.tests.items():
                if str(info['r']).lower() == str(self.value.get_regression()).lower() and \
                    str(info['i']).lower() == str(value.get_idenpotent).lower():
                    filter_info.append(value.get_id())
                    self.__build_body_format(value, info)
        elif 't' in info.keys():
            self.__build_header_format(info)
            for key, value in self.tests.items():
                for x in info['t']:
                    if x == value.get_test_type():
                        filter_info.append(value.get_id())
                        self.__build_body_format(value, info)
        elif 'r' in info.keys():
            self.__build_header_format(info)
            for key, value in self.tests.items():
                if str(info['r']).lower() == str(value.get_regression()).lower():
                    filter_info.append(value.get_id())
                    self.__build_body_format(value, info)
        elif 'i' in info.keys():
            self.__build_header_format(info)
            for key, value in self.mti_info.items():
                if str(info['i']).lower() == str(value.idenpotent()).lower():
                    filter_info.append(value.get_id())
                    self.__build_body_format(value, info)
        if 'o' in info.keys():
            df = open(info['o'], 'w')
            for id in filter_info:
                df.write(id + '\n')
            df.close()

    def get_info(self, info = {}):
        if len(info) == 0:
            self.__print_all_system_ids()
        else:
            self.__print_with_filters(info=info)

    def get_sanity_info(self, info={}):
        if len(info) == 0:
            self.__print_all_sanity_ids()
        else:
            self.__print_with_filters(info=info)

    def get_methods(self, tests):
        system_methods = {}
        for key, value in tests.items():
            if 'DT' != value.get_test_type():
                methods[key] = value
        return methods

    def get_sanity_methods(self, tests):
        sanity_methods = {}
        for key, value in tests.items():
            if 'DT' == value.get_test_type():
                sanity_methods[key] = value
        return sanity_methods

    def get_valid_tests(self, release):
        for key, value in self.data().items():
            for val in value[3]:
                if range.Range(val[1]).is_included(release):
                    test_structure = test.TestStructure(value, val[0], val[1])
                    if key in self.tests.keys():
                        self.tests[key+str(random.random())[0:5]] = test_structure
                    else:
                        self.tests[key] = test_structure
        return self.tests

    
