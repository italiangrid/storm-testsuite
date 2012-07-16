import sys
import os
import exceptions

class SequenceError(exceptions.Exception):
    pass

class Sequence:
    def __init__(self, value):
        if ' ' in value:
            raise SequenceError('The sequence contains empty space')
        self.sequence = [x.strip() for x in value.split(',')]

    def get_sequence(self):
        return self.sequence
