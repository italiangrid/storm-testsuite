import exceptions
from tstorm.utils import release
from tstorm.utils import limit

class RangeError(exceptions.Exception):
    pass

class Range:
    def __init__(self, range_value):
        self.sup = limit.Limit(range_value[len(range_value)-1])
        if not self.sup.is_sup():
            raise RangeError('Superior Limit is not well specified - %s' % self.sup)
            
        self.inf = limit.Limit(range_value[0])
        if not self.inf.is_inf():
            raise RangeError('Inferior Limit is not well specified - %s' % self.inf)

        if ',' not in range_value:
            raise RangeError('Range is not well specified - %s' % range_value)

        extreme = range_value[1:len(range_value)-1].strip().split(',')
        if len(extreme) == 2:
            self.min_release = release.Release(extreme[0])
            self.max_release = release.Release(extreme[1])
        #else:
        #    raise RangeError('Range is not well specified - %s' % range)

        if not self.min_release.is_infinity():
            if not self.max_release.is_infinity():
                if not (self.min_release.is_lower(self.max_release) and \
                    self.max_release.is_greater(self.min_release)):
                    msg = 'The couple Min,Max is not well specified in'
                    msg += 'the range - ' + range_value
                    raise RangeError(msg)

    def is_included(self, value):
        if self.inf.is_extreme_included():
            if self.sup.is_extreme_included():
                if self.min_release.is_infinity() and self.max_release.is_infinity():
                    return True
                else:
                    if self.min_release.is_lower_and_equal(value) and \
                        self.max_release.is_greater_and_equal(value):
                        return True
                    else:
                        return False
            else:
                if self.min_release.is_infinity() and self.max_release.is_infinity():
                    return True
                else:
                    if self.min_release.is_lower_and_equal(value) and \
                        self.max_release.is_greater(value):
                        return True
                    else:
                        return False
        else:
            if self.sup.is_extreme_included():
                if self.min_release.is_infinity() and self.max_release.is_infinity():
                    return True
                else:
                    if self.min_release.is_lower(value) and \
                        self.max_release.is_greater_and_equal(value):
                        return True
                    else:
                        return False
            else:
                if self.min_release.is_infinity() and self.max_release.is_infinity():
                    return True
                else:
                    if self.min_release.is_lower(value) and \
                        self.max_release.is_greater(value):
                        return True
                    else:
                        return False
