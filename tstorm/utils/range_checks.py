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
        try:
            self.sup = limit.Limit(range[len(range)-1])
            if not self.sup.is_sup():
                raise RangeError(2, 'Superior Limit is not well specified %s' % sup)

            self.inf = limit.Limit(range[0])
            if not self.inf.is_sup():
                raise RangeError(2, 'Inferior Limit is not well specified %s' % sup)

            extreme = range[1:len(range)-1].strip().split(',')
            self.min_release = release_checks.ReleaseChecks(extreme[0])
            self.max_release = release_checks.ReleaseChecks(extreme[1])

        except limit.LimitError:
            raise RangeError(2, 'Extreme Limit is not well specified %s' % sup)
        except release_checks.ReleaseError:
            raise RangeError(2, 'Release is not well specified %s' % sup)

    def is_included(self, release):
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
