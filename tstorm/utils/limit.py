import sys
import os

class LimitError(Exception):
    def __init__(self, msg):
        self.args = (msg)
        self.errmsg = msg

class Limit:
    def __init__(self, value):
        if value in (')', ']', '(', '['):
            self.limit = value
            if value in (')', '('):
                self.extreme_included = False
            else:
                self.extreme_included = True
        else:
            raise LimitError('limit is not well specified %s' % value)
                
    def is_sup():
        if self.limit in (')',']'):
            return True
        return False

    def is_inf(value):
        if self.limit in ('(','['):
            return True
        return False

    def is_extreme_included(value):
        return self.extreme_included
