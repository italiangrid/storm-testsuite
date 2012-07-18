import sys
import os
import exceptions

class ReleaseError(exceptions.Exception):
    pass

class Release:
    def __init__(self, value):
        self.infinity = False
        if len(value) == 1 and type(value) is str:
            if value == '*':
                self.infinity = True;
            else:
                raise ReleaseError('release is not set to *')
        elif len(value) > 1 and '-' in value and '.' in value:
            try:
                tmp = map(int, value.replace('-','.').split('.'))
            except ValueError, er:
                raise ReleaseError('release is not set to x.y.z-w - %s' % value)
            if len(tmp) == 4 :
                self.release = tmp
            else:
                raise ReleaseError('release is not set to x.y.z-w')
        else: 
            raise ReleaseError('release is not well specified')
    
    def get_release(self):
        return self.release

    def is_infinity(self):
        return self.infinity
                
    def is_greater(self,value):
        if self.infinity:
            if value.is_infinity():
                print '1'
                return False
            else:
                print '2'
                return True
        elif value.is_infinity():
            print '3'
            return False
        elif self.release > value.get_release():
            print '4'
            return True
        else:
            print '5'
            return False

    def is_greater_and_equal(self,value):
        if self.infinity:
            if value.is_infinity():
                print '6'
                return True
            else:
                print '7'
                return False
        elif value.is_infinity():
            print '8'
            return False
        elif self.release >= value.get_release():
            print '9'
            return True
        else:
            print '10'
            return False

    #returns tue if this objctr is lower than the provided parameter that is a Release object  
    def is_lower(self,value):
        if self.infinity:
            #if value.is_infinity():
            #    return False
            #else:
            #    return False
            print '11'
            return False
        elif value.is_infinity():
            print '12'
            return True
        elif self.release < value.get_release():
            print '13'
            return True
        else:
            print '14'
            return False

    def is_lower_and_equal(self,value):
        if self.infinity:
            if value.is_infinity():
                print '15'
                return True
            else:
                print '16'
                return False
        elif value.is_infinity():
            print '17'
            return True
        elif self.release <= value.get_release():
            print '18'
            return True
        else:
            print '19'
            return False
