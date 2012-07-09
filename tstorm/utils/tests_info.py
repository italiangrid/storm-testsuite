import sys
import os

class TestsInfo:
    def __init__(self, mti_info, info={}):
        self.mti_info = mti_info
        self.info = info
        self.list_keys = {'i':0,'id':0,'t':1,'type':1,'r':2,'regression':3,'rfc':3,'idenpotent':4,'range':5,'n':6,'name':6,'d':7,'description':7}

    def __print_all_system_ids(self):
        print 'ID      RFC'
        for key, value in self.mti_info.items():
            if 'ts' in key and value[1] != 'DT':
                print '%s  %s' % (value[0], value[3])

    def __print_all_sanity_ids(self):
        print 'ID      RFC'
        for key, value in self.mti_info.items():
            if 'ts' in key and value[1] == 'DT':
                print '%s  %s' % (value[0], value[3])

    def __build_header_format(self):
        if 'f' not in self.info.keys():
            print 'ID      RFC'
        else:
            msg = ''
            for x in self.info['f']:
                msg += x + '       '
            print msg

    def __build_body_format(self, value):
        if 'f' not in self.info.keys():
            print '%s  %s' % (value[0], value[3])
        else:
            msg = ''
            for x in self.info['f']:
                msg += value[self.list_keys[x]] + '  '
            print msg

    def __print_with_filters(self):
        filter_info = []
        if 't' in self.info.keys() and 'r' in self.info.keys() and 'i' in self.info.keys():
            self.__build_header_format()
            for key, value in self.mti_info.items():
                if 'ts' in key:
                    for x in self.info['t']:
                        if x == value[1] and \
                            str(self.info['r']).lower() == str(value[2]).lower() and \
                            str(self.info['i']).lower() == str(value[3]).lower():
                            filter_info.append(value[0])
                            self.__build_body_format(value)
        elif 't' in self.info.keys() and 'r' in self.info.keys():
            self.__build_header_format()
            for key, value in self.mti_info.items():
                if 'ts' in key:
                    for x in self.info['t']:
                        if x == value[1] and \
                            str(self.info['r']).lower() == str(value[2]).lower():
                            filter_info.append(value[0])
                            self.__build_body_format(value)
        elif 't' in self.info.keys() and 'i' in self.info.keys():
            self.__build_header_format()
            for key, value in self.mti_info.items():
                if 'ts' in key:
                    for x in self.info['t']:
                        if x == value[1] and \
                            str(self.info['i']).lower() == str(value[3]).lower():
                            filter_info.append(value[0])
                            self.__build_body_format(value)
        elif 'r' in self.info.keys() and 'i' in self.info.keys():
            self.__build_header_format()
            for key, value in self.mti_info.items():
                if 'ts' in key:
                    if str(self.info['r']).lower() == str(self.value[2]).lower() and \
                        str(self.info['i']).lower() == str(value[3]).lower():
                        filter_info.append(value[0])
                        self.__build_body_format(value)
        elif 't' in self.info.keys():
            self.__build_header_format()
            for key, value in self.mti_info.items():
                if 'ts' in key:
                    for x in self.info['t']:
                        if x == value[1]:
                            filter_info.append(value[0])
                            self.__build_body_format(value)
        elif 'r' in self.info.keys():
            self.__build_header_format()
            for key, value in self.mti_info.items():
                if 'ts' in key:
                    if str(self.info['r']).lower() == str(value[3]).lower():
                        filter_info.append(value[0])
                        self.__build_body_format(value)
        elif 'i' in self.info.keys():
            self.__build_header_format()
            for key, value in self.mti_info.items():
                if 'ts' in key:
                    if str(self.info['i']).lower() == str(value[3]).lower():
                        filter_info.append(value[0])
                        self.__build_body_format(value)
        if 'o' in self.info.keys():
            df = open(self.info['o'], 'w')
            for id in filter_info:
                df.write(id + '\n')
            df.close() 
            
    # t=AT,FT r=true i=true o=profile-regression-check.txt
    def get_system_info(self):
        if len(self.info) == 0:
            self.__print_all_system_ids()
        else:
            self.__print_with_filters()

    def get_sanity_info(self):
        if len(self.info) == 0:
            self.__print_all_sanity_ids()
        else:
            self.__print_with_filters()

