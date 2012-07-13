import sys
import os

class ReleaseError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg

class Release:
    def __init__(self, release):
        try:
            if len(release) == 1 and type(release) is srt:
                if release == '*':
                    self.infinity = true;
                else:
                    raise VersionError(2, 'release is not set to *')
            elif len(release) > 1 and '-' in release and '.' in release:
                tmp = map(int, release.replace('-','.').split('.'))
                if len(tmp) == 4 :
                    self.release == tmp
                else:
                    raise VersionError(2, 'release is not set to x.y.z-w')
            else: 
                raise VersionError(2, 'release is not well specified')
        except :
            raise VersionError(2, 'release is not well specified')
        
                
    def is_greater(value):
        if type(self.version) is str:
            return False
        if self.version > value:
            return True
        return False

    def is_greater_and_equal(value):
        if type(self.version) is str:
            return True
        if self.version >= value:
            return True
        return False

    #returns tue if this objctr is lower than the provided parameter that is a Release object  
    def is_lower(value):
        if self.infinity :
            if value.isInfinity :
                return False
            else
                return False
        return self.version < value.getVersion

    def is_lower_and_equal(value):
        if type(self.version) is str:
            return True
        if self.version <= value:
            return True
        return False
