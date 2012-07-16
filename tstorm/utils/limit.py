import sys
import os
import exceptions

class LimitError(exceptions.Exception):
    pass

class Limit:
    def __init__(self, value):
        self.extreme_included = False
        if value in (')', ']', '(', '['):
            self.limit = value
            if value in (')', '('):
                #print 'd %s' % value
                self.extreme_included = False
            else:
                #print 'c %s' % value
                self.extreme_included = True
        else:
            raise LimitError('limit is not well specified %s' % value)
                
    def is_sup(self):
        if self.limit in (')',']'):
            return True
        return False

    def is_inf(self):
        if self.limit in ('(','['):
            return True
        return False

    def is_extreme_included(self):
        return self.extreme_included
