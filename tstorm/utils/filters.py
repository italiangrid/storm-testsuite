import sys
import os
import exceptions

class FiltersError(exceptions.Exception):
    pass

class Filters:
    def __init__(self, value):
        if ';' not in value:
           if value.count('=') > 1:
               raise FiltersError('The value is not well specified')
        self.filters = value.split(';')

    def __print_check_tests_types_msg(self,run=''):
        msg = 'This script only runs the following types of tests:\n'
        for val in self.get_tests_types(run=run):
            msg += val + '\n'
        print msg

    def __check_tests_types(self, values, run=''):
        if run == 'sanity':
            if len(values) > 1:
                self.__print_check_tests_types_msg(run=run)
                raise FiltersError('Filters are not correct for sanity tests')
            elif 'DT' not in values:
                self.__print_check_tests_types_msg(run=run)
                raise FiltersError('Filters are not correct for sanity tests')
        elif run == 'stress':
            if len(values) > 1:
                self.__print_check_tests_types_msg(run=run)
                raise FiltersError('Filters are not correct for sanity tests')
            elif 'LT' not in values:
                self.__print_check_tests_types_msg(run=run)
                raise FiltersError('Filters are not correct for sanity tests')
        else:
            if 'DT' in values:
                self.__print_check_tests_types_msg(run=run)
                raise FiltersError('Filters are not correct for tests')

    def __print_check_tests_data_structure_msg(self):
        msg = 'This parameter only considers the following parameters:\n'
        for val in self.get_tests_data_structure():
            msg += val + '\n'
        print msg

    def __check_tests_data_structure(self, values):
        for val in values:
            if val == 'o':
                self.__print_check_tests_data_structure_msg()
                raise FiltersError('Filters are not correct for tests')
            for x in self.get_tests_data_structure():
                if val != x:
                    self.__print_check_tests_data_structure_msg()
                    raise FiltersError('Filters are not correct for tests')

    def get_tests_types(self,run=''):
        if run == 'sanity':
            return ('DT')
        elif run == 'stress':
            return ('LT')
        return ('AT', 'ST', 'UT', 'LT')

    def get_tests_data_structure(self):
        return ('t', 'test', \
            'r', 'regression', 'rfc', 'i', 'id', 'idenpotent', \
            'range', 'n', 'name', 'd', 'description')

    def get_filters(self,run=''):
        tmp_filter_tests_details = {}
        for filter in self.filters:
            if 't' == filter.split('=')[0] or 'test' == filter.split('=')[0]:
                tmp_filter_tests_details['t'] = \
                    [val.strip() for val in filter.split('=')[1].split(',')]
                self.__check_tests_types(tmp_filter_tests_details['t'],run=run)
            elif 'r' == filter.split('=')[0] or \
                'regression' == filter.split('=')[0]:
                tmp_filter_tests_details['r'] = filter.split('=')[1]
            elif 'i' == filter.split('=')[0] or \
                'idenpotent' == filter.split('=')[0]:
                tmp_filter_tests_details['i'] = filter.split('=')[1]
            elif 'o' == filter.split('=')[0] or \
                'output' == filter.split('=')[0]:
                tmp_filter_tests_details['o'] = filter.split('=')[1]
            elif 'f' == filter.split('=')[0] or \
                'format' == filter.split('=')[0]:
                tmp_filter_tests_details['f'] = \
                    [val.strip() for val in filter.split('=')[1].split(',')]
                self.__check_tests_data_structure(tmp_filter_tests_details['f'])
            else:
                raise FiltersError('Filters are not well specified')

        return tmp_filter_tests_details
