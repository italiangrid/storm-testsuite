import sys
import os

class LimitError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg

class Limit:
    def __init__(self, value):
        if value in (')', ']', '(', '['):
            self.limit = value
        else:
            raise LimitError(3, 'limit is not well specified %s' % value)
                
    def is_sup():
        if self.limit in (')',']'):
            return True
        return False

    def is_inf(value):
        if self.limit in ('(','['):
            return True
        return False
