import sys
import os

class RangeChecks:
    def __init__(self, storm_release, range):
        self.storm_release = storm_release.replace('-','.')
        self.sup = range[len(range)-1]
        self.inf = range[0]
        self.range = \
            range[1:len(range)-1].replace('-','.').strip().split(',')

    def __check_outer(self):
        if (self.sup == ')' or self.sup == ']') and \
            (self.inf == '(' or self.inf == '['):
            return True
        return False

    def __check_release(self, val):
        if len(val.split('.')) == 4:
            return True
        return False

    def __check_int_type(self, val):
        if not map(int, val):
            return False
        return True

    def __check_str_type(self, val):
        if val != '*':
            return False
        return True

    def __check_size(self):
        if len(self.range[0]) != len(self.range[1]):
            if self.__check_int_type(self.range[0]) and \
                self.__check_int_type(self.range[1]):
                return False
        return True

    def __check_type(self, val):
        if self.__check_str_type(val):
            return True
        if self.__check_int_type(val):
            return True
        return False

    def __check_run_test(self):
        if self.inf == '(' and self.sup == ')':
            if self.__check_str_type(self.range[0]) and self.__check_str_type(self.range[1]):
                return True
            elif self.__check_str_type(self.range[0]) and self.__check_int_type(self.range[1]):
                if self.storm_revision < self.range[1]:
                    return True
            elif self.__check_int_type(self.range[0]) and self.__check_str_type(self.range[1]):
                if self.storm_revision > self.range[0]:
                    return True
            elif self.__check_int_type(self.range[0]) and self.__check_int_type(self.range[1]):
                if self.storm_revision > self.range[0] and self.storm_revision < self.range[1]:
                    return True
        elif self.inf == '(' and self.sup == ']':
            if self.__check_str_type(self.range[0]) and self.__check_str_type(self.range[1]):
                return True
            elif self.__check_str_type(self.range[0]) and self.__check_int_type(self.range[1]):
                if self.storm_revision <= self.range[1]:
                    return True
            elif self.__check_int_type(self.range[0]) and self.__check_str_type(self.range[1]):
                if self.storm_revision > self.range[0]:
                    return True
            elif self.__check_int_type(self.range[0]) and self.__check_int_type(self.range[1]):
                if self.storm_revision > self.range[0] and self.storm_revision <= self.range[1]:
                    return True
        elif self.inf == '[' and self.sup == ')':
            if self.__check_str_type(self.range[0]) and self.__check_str_type(self.range[1]):
                return True
            elif self.__check_str_type(self.range[0]) and self.__check_int_type(self.range[1]):
                if self.storm_revision < self.range[1]:
                    return True
            elif self.__check_int_type(self.range[0]) and self.__check_str_type(self.range[1]):
                if self.storm_revision >= self.range[0]:
                    return True
            elif self.__check_int_type(self.range[0]) and self.__check_int_type(self.range[1]):
                if self.storm_revision >= self.range[0] and self.storm_revision < self.range[1]:
                    return True
        elif self.inf == '[' and self.sup == ']':
            if self.__check_str_type(self.range[0]) and self.__check_str_type(self.range[1]):
                return True
            elif self.__check_str_type(self.range[0]) and self.__check_int_type(self.range[1]):
                if self.storm_revision <= self.range[1]:
                    return True
            elif self.__check_int_type(self.range[0]) and self.__check_str_type(self.range[1]):
                if self.storm_revision >= self.range[0]:
                    return True
            elif self.__check_int_type(self.range[0]) and self.__check_int_type(self.range[1]):
                if self.storm_revision >= self.range[0] and self.storm_revision <= self.range[1]:
                    return True

        return False

    def is_valid(self):
        if not self.__check_outer():
            return False
        if not self.__check_release(self.storm_release):
            return False
        if not self.__check_size():
            return False
        for x in self.range:
            if not self.__check_type(x):
                return False
        if not self.__check_run_test():
            return False
        return True
