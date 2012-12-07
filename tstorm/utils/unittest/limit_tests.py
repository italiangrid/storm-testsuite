'''
Created on Jul 31, 2012

@author: joda
'''
import unittest
from tstorm.utils import limit


class LimitTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_with_wrong_input(self):
        try:
            limit.Limit('banane')
        except limit.LimitError:
            pass
        else:
            self.fail("expected a LimitError")
        pass

    def test_init_with_extreme_inf_excluded(self):
        limit.Limit('(')
        pass
    
    def test_init_with_extreme_sup_excluded(self):
        limit.Limit(')')
        pass
    
    def test_init_with_extreme_inf_included(self):
        limit.Limit('[')
        pass
    
    def test_init_with_extreme_sup_included(self):
        limit.Limit(']')
        pass
    
    def test_if_extreme_included_is_inf(self):
        my_limit = limit.Limit('[')
        self.failIf(not my_limit.is_inf())
        pass
    
    def test_if_extreme_included_is_not_sup(self):
        my_limit = limit.Limit('[')
        self.failIf(my_limit.is_sup())
        pass
    
    def test_if_is_inf(self):
        my_limit = limit.Limit('(')
        self.failIf(not my_limit.is_inf())
        pass
    
    def test_if_is_not_sup(self):
        my_limit = limit.Limit('(')
        self.failIf(my_limit.is_sup())
        pass
    
    def test_if_extreme_included_is_sup(self):
        my_limit = limit.Limit(']')
        self.failIf(not my_limit.is_sup())
        pass
    
    def test_if_extreme_included_is_not_inf(self):
        my_limit = limit.Limit(']')
        self.failIf(my_limit.is_inf())
        pass
    
    def test_if_is_sup(self):
        my_limit = limit.Limit(')')
        self.failIf(not my_limit.is_sup())
        pass
    
    def test_if_is_not_inf(self):
        my_limit = limit.Limit(')')
        self.failIf(my_limit.is_inf())
        pass
    
    def test_if_extreme_is_included(self):
        my_limit = limit.Limit(')')
        self.failIf(my_limit.is_extreme_included())
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()