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

    def __print_ids(self,run=''):
        print 'ID      RFC'
        for key, value in self.tests.items():
            if run == 'sanity':
                if value.get_test_type() == 'DT':
                    print '%s  %s' % (value.get_id(), value.get_rfc())
            else:
                if value.get_test_type() != 'DT':
                    print '%s  %s' % (value.get_id(), value.get_rfc())

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
            print '%s  %s' % (value.get_id(), value.get_rfc())
        else:
            msg = ''
            for x in info['f']:
                msg += eval('value.' + self.list_keys[x]) + '  '
            print msg

    def __print_ids_with_filters(self,info={},run=''):
        filter_info = []
        self.__build_header_format(info)
        for key, value in self.tests.items():
            if run == 'sanity':
                if value.get_test_type() != 'DT':
                    continue
            elif value.get_test_type() == 'DT':
                continue
            if 't' in info.keys() and 'r' in info.keys() and 'i' in info.keys():
                for x in info['t']:
                    if x == value.get_test_type() and \
                        str(info['r']).lower() == str(value.is_regression()).lower() and \
                        str(info['i']).lower() == str(value.is_idenpotent()).lower():
                        filter_info.append(value.get_id())
                        self.__build_body_format(value, info)
            elif 't' in info.keys() and 'r' in info.keys():
                for x in info['t']:
                    if x == value.get_test_type() and \
                        str(info['r']).lower() == str(value.is_regression()).lower():
                        filter_info.append(value.get_id())
                        self.__build_body_format(value, info)
            elif 't' in info.keys() and 'i' in info.keys():
                for x in info['t']:
                    if x == value.get_test_type(): 
                        #print 'uffa %s %s' % (str(info['i']).lower(), str(value.is_idenpotent()).lower())
                        if str(info['i']).lower() == str(value.is_idenpotent()).lower():
                            filter_info.append(value.get_id())
                            self.__build_body_format(value, info)
            elif 'r' in info.keys() and 'i' in info.keys():
                if str(info['r']).lower() == str(value.is_regression()).lower() and \
                    str(info['i']).lower() == str(value.is_idenpotent).lower():
                    filter_info.append(value.get_id())
                    self.__build_body_format(value, info)
            elif 't' in info.keys():
                for x in info['t']:
                    if x == value.get_test_type():
                        filter_info.append(value.get_id())
                        self.__build_body_format(value, info)
            elif 'r' in info.keys():
                if str(info['r']).lower() == str(value.is_regression()).lower():
                    filter_info.append(value.get_id())
                    self.__build_body_format(value, info)
            elif 'i' in info.keys():
                if str(info['i']).lower() == str(value.is_idenpotent()).lower():
                    filter_info.append(value.get_id())
                    self.__build_body_format(value, info)
            if 'o' in info.keys():
                df = open(info['o'], 'w')
                for id in filter_info:
                    df.write(id + '\n')
                df.close()

    def get_info(self, info = {}, run=''):
        if len(info) == 0:
            self.__print_ids(run=run)
        else:
            self.__print_ids_with_filters(info=info,run=run)

    def get_methods(self, tests, run=''):
        methods = {}
        for key, value in tests.items():
            if run == 'sanity':
                if 'DT' == value.get_test_type():
                    methods[key] = value
                else:
                    continue
            elif run == 'stress':
                if 'DT' != value.get_test_type() and \
                    value.is_idenpotent() and \
                    not value.is_regression():
                    methods[key] = value
                else:
                    continue
            elif 'DT' != value.get_test_type():
                methods[key] = value
        return methods

    def get_sanity_methods(self, tests):
        sanity_methods = {}
        for key, value in tests.items():
            if 'DT' == value.get_test_type():
                sanity_methods[key] = value
        return sanity_methods

    def get_valid_tests(self, release):
        for key, value in self.data.items():
            for val in value[3]:
                if range.Range(val[1]).is_included(release):
                    test_structure = test.TestStructure(value, val[0], val[1])
                    if key in self.tests.keys():
                        self.tests[key+str(random.random())[0:5]] = test_structure
                    else:
                        self.tests[key] = test_structure
        return self.tests

    
