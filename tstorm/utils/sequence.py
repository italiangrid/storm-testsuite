import sys
import os

class SequenceError:
    def __init__(self, msg):
        self.args = msg
        self.errmsg = msg

class Sequence:
    def __init__(self, value):
        if ' ' in value:
            raise SequenceError('The sequence contains empty space')
        self.sequence = [x.strip() for x in value.split(',')]

    def get_sequence(self):
        return self.sequence
