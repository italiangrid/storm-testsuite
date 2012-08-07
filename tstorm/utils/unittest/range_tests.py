'''
Created on Aug 7, 2012

@author: joda
'''
import unittest
from tstorm.utils import range
from tstorm.utils import limit

class RangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_with_wrong_range_input(self):
        try:
            range.Range('banane')
        except limit.LimitError:
            pass
        except range.RangeError:
            pass
                
        try:
            range.Range('banane)')
        except limit.LimitError:
            pass
        except range.RangeError:
            pass
        
    def test_init_with_wrong_sup_input(self):
        try:
            range.Range(',(')
        except range.RangeError:
            pass
        else:
            self.fail("expected a RangeError")
        pass

    def test_init_with_wrong_inf_input(self):
        try:
            range.Range(')a,)')
        except range.RangeError:
            pass
        else:
            self.fail("expected a RangeError")
        pass
    
    def test_init_with_wrong_range_input(self):
        try:
            range.Range('()')
        except range.RangeError:
            pass
        else:
            self.fail("expected a RangeError")
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()