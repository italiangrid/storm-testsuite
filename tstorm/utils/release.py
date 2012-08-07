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
            except ValueError:
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
                return False
            else:
                return True
        elif value.is_infinity():
            return False
        elif self.release > value.get_release():
            return True
        else:
            return False

    def is_greater_and_equal(self,value):
        if self.infinity:
            if value.is_infinity():
                return True
            else:
                return False
        elif value.is_infinity():
            return False
        elif self.release >= value.get_release():
            return True
        else:
            return False

    #returns tue if this objctr is lower than the provided parameter that is a Release object  
    def is_lower(self,value):
        if self.infinity:
            return False
        elif value.is_infinity():
            return True
        elif self.release < value.get_release():
            return True
        else:
            return False

    def is_lower_and_equal(self,value):
        if self.infinity:
            if value.is_infinity():
                return True
            else:
                return False
        elif value.is_infinity():
            return True
        elif self.release <= value.get_release():
            return True
        else:
            return False
