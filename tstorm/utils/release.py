import sys
import os

class ReleaseError(Exception):
    def __init__(self, msg):
        self.args = msg
        self.errmsg = msg

class Release:
    def __init__(self, value):
        self.infinity = False

        if len(value) == 1 and type(value) is srt:
            if value == '*':
                self.infinity = True;
            else:
                raise VersionError('release is not set to *')
        elif len(value) > 1 and '-' in value and '.' in value:
            tmp = map(int, value.replace('-','.').split('.'))
            if len(tmp) == 4 :
                self.release == tmp
            else:
                raise VersionError('release is not set to x.y.z-w')
        else: 
            raise VersionError('release is not well specified')
    
    def get_release(self):
        return self.release

    def is_infinity(self):
        return self.infinity
                
    def is_greater(value):
        if self.infinity:
            if value.is_infinity():
                return False
            else:
                return True
        elif value.is_infinity():
            return False
        elif self.version > value.get_release():
            return True
        else:
            return False

    def is_greater_and_equal(value):
        if self.infinity:
            if value.is_infinity():
                return True
            else:
                return False
        elif value.is_infinity():
            return False
        elif self.version >= value.get_release():
            return True
        else:
            return False

    #returns tue if this objctr is lower than the provided parameter that is a Release object  
    def is_lower(value):
        if self.infinity:
            #if value.is_infinity():
            #    return False
            #else:
            #    return False
            return False
        elif value.is_infinity():
            return True
        elif self.version < value.get_release():
            return True
        else:
            return False

    def is_lower_and_equal(value):
        if self.infinity:
            if value.is_infinity():
                return True
            else:
                return False
        elif value.is_infinity():
            return True
        elif self.version <= value.get_release():
            return True
        else:
            return False
