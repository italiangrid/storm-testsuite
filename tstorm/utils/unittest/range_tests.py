'''
Created on Aug 7, 2012

@author: joda
'''
import unittest
from tstorm.utils import range
from tstorm.utils import release
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
        
        try:
            range.Range('()')
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
    
    def test_init_with_wrong_extreme_input(self):
        try:
            range.Range('(1.2.3-1,)')
        except release.ReleaseError:
            pass    
        except range.RangeError:
            pass
        else:
            self.fail("expected a RangeError")
        pass
    
    def test_init_with_wrong_extreme_inputs(self):
        try:
            range.Range('(1.2.3-1,1.2.2-1)')  
        except range.RangeError:
            pass
        else:
            self.fail("expected a RangeError")
        pass
       
    def test_init_with_range_input(self):
        range.Range('[1.2.3-1,1.2.10-4]')
        pass
    
    def test_if_release_is_included_in_range_included(self):
        a = range.Range('[1.2.3-1,1.2.10-4]')
        b = release.Release('1.2.5-2')
        self.failIf(not a.is_included(b))
        pass
    
    def test_if_release_is_not_included_in_range_included(self):
        a = range.Range('[1.2.3-1,1.2.10-4]')
        b = release.Release('1.3.5-2')
        self.failIf(a.is_included(b))
        pass
    
    def test_if_release_is_included_in_range_sup_included(self):
        a = range.Range('(1.2.3-1,1.2.10-4]')
        b = release.Release('1.2.5-2')
        self.failIf(not a.is_included(b))
        pass
    
    def test_if_release_is_included_in_range_inf_included(self):
        a = range.Range('[1.2.3-1,1.2.10-4)')
        b = release.Release('1.2.5-2')
        self.failIf(not a.is_included(b))
        pass
    
    def test_if_release_is_included_in_range(self):
        a = range.Range('(1.2.3-1,1.2.10-4)')
        b = release.Release('1.2.5-2')
        self.failIf(not a.is_included(b))
        pass
    
    def test_if_release_infinity_is_not_included_in_range_included(self):
        a = range.Range('[1.2.3-1,1.2.10-4]')
        b = release.Release('*')
        self.failIf(a.is_included(b))
        pass
    
    def test_if_release_infinity_is_included_in_range_infinity_included(self):
        a = range.Range('[*,*]')
        b = release.Release('*')
        self.failIf(not a.is_included(b))
        pass
    
    def test_if_release_infinity_is_included_in_range_infinity_sup_included(self):
        a = range.Range('(*,*]')
        b = release.Release('*')
        self.failIf(not a.is_included(b))
        pass
    
    def test_if_release_infinity_is_included_in_range_infinity_inf_included(self):
        a = range.Range('[*,*)')
        b = release.Release('*')
        self.failIf(not a.is_included(b))
        pass
             
    def test_if_release_infinity_is_not_included_in_range_sup_included(self):
        a = range.Range('(1.2.3-1,1.2.10-4]')
        b = release.Release('*')
        self.failIf(a.is_included(b))
        pass
    
    def test_if_release_infinity_is_not_included_in_range_inf_included(self):
        a = range.Range('[1.2.3-1,1.2.10-4)')
        b = release.Release('*')
        self.failIf(a.is_included(b))
        pass
    
    def test_if_release_infinity_is_not_included_in_range(self):
        a = range.Range('(1.2.3-1,1.2.10-4)')
        b = release.Release('*')
        self.failIf(a.is_included(b))
        pass        
              
    def test_if_release_infinity_is_included_in_range_infinity(self):
        a = range.Range('(*,*)')
        b = release.Release('*')
        self.failIf(not a.is_included(b))
        pass
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()