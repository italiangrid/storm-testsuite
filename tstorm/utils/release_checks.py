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
                    self.release == release
                else:
                    raise VersionError(2, 'release is not set to *')
            elif len(release) > 1 and '-' in release and '.' in release:
                tmp = map(int, release.replace('-','.').split('.'))
                if len(release.replace('-','.').split('.')) == 4 and tmp:
                    self.release == tmp
                else:
                    raise VersionError(2, 'release is not set to x.y.z-w')
        except:
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

    def is_lower(value):
        if type(self.version) is str:
            return False
        if self.version < value:
            return True
        return False

    def is_lower_and_equal(value):
        if type(self.version) is str:
            return True
        if self.version <= value:
            return True
        return False
