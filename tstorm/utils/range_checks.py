import sys
import os
from wndoes.utils import release_checks
from wnodes.utils import limit

class RangeError(Exceptions):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg

class RangeChecks:
    def __init__(self, range):
        self.sup = limit.Limit(range[len(range)-1])
        if not self.sup.is_sup():
            raise RangeError(2, 'Superior Limit is not well specified %s' % sup)

        self.inf = limit.Limit(range[0])
        if not self.inf.is_sup():
            raise RangeError(2, 'Inferior Limit is not well specified %s' % sup)
        if not ',' in range: 
            raise RangeError(2, 'Inferior Limit is not well specified %s' % sup)    
        extreme = range[1:len(range)-1].strip().split(',')
        self.min_release = release_checks.ReleaseChecks(extreme[0])
        self.max_release = release_checks.ReleaseChecks(extreme[1])
        if not (self.min_release.is_lower(self.max_release) and self.max_release.is_greater(self.min_release)):
           raise RangeError(2, 'Inferior Limit is not well specified %s' % sup)

       

    def is_included(self, release):
        #cambiare  i controlli sul tipo delle parentesi con chiamate a:
        #self.inf.is_extreme_included():
        if self.inf == '(' and self.sup == ')':
            
            if self.min_release.is_greater(release) and \
                self.max_release.is_lower(release):
                return True
        elif self.inf == '(' and self.sup == ']':
            if self.min_release.is_greater(release) and \
                self.max_release.is_lower_and_equal(release):
                return True
        elif self.inf == '[' and self.sup == ')':
            if self.min_release.is_greater_and_equal(release) and \
                self.max_release.is_lower(release):
                return True
        elif self.inf == '[' and self.sup == ']':
            if self.min_release.is_greater_and_equal(release) and \
                self.max_release.is_lower_and_equal(release):
                return True

        return False
