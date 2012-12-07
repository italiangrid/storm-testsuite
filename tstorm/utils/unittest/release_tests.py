'''
Created on Aug 7, 2012

@author: joda
'''
import unittest
from tstorm.utils import release

class ReleaseTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_with_wrong_input(self):
        try:
            release.Release('banane')
        except release.ReleaseError:
            pass
    
    def test_init_with_infinity(self):
        release.Release('*')
        pass    
    
    def test_init_with_wrong_one_size_input(self):
        try:
            release.Release('-')
        except release.ReleaseError:
            pass
        
        try:
            release.Release('1')
        except release.ReleaseError:
            pass
    
    def test_init_with_wrong_release_input(self):
        try:
            release.Release('1.2.3')
        except release.ReleaseError:
            pass
        try:
            release.Release('1-2-3')
        except release.ReleaseError:
            pass
        try:
            release.Release('1-2.3')
        except release.ReleaseError:
            pass
        try:
            release.Release('1.2-3')
        except release.ReleaseError:
            pass
        try:
            release.Release('1.2.3-')
        except release.ReleaseError:
            pass
        try:
            release.Release('1-2-3.')
        except release.ReleaseError:
            pass
        try:
            release.Release('1-2-3-4')
        except release.ReleaseError:
            pass
        try:
            release.Release('1.2.3.4')
        except release.ReleaseError:
            pass
        try:
            release.Release('1.2')
        except release.ReleaseError:
            pass
        
    def test_init_with_release(self):
        release.Release('1.2.3-1')
        pass  
               
    def test_if_release_is_infinity(self):
        my_release = release.Release('*')
        self.failIf(not my_release.is_infinity())
        pass
    
    def test_if_release_is_not_infinity(self):
        my_release = release.Release('1.2.3-1')
        self.failIf(my_release.is_infinity())
        pass           
               
    def test_release(self):
        my_release = release.Release('1.2.3-1')
        self.assertEqual(len(my_release.get_release()), 4)
        pass

    def test_if_current_release_is_not_greater_than_infinity(self):
        current_release = release.Release('1.2.3-1')
        new_release = release.Release('*')
        
        self.failIf(current_release.is_greater(new_release))
        pass
    
    def test_if_infinity_is_not_greater_than_infinity(self):
        current_release = release.Release('*')
        new_release = release.Release('*')
        
        self.failIf(current_release.is_greater(new_release))
        pass

    def test_if_current_release_is_greater_than_release(self):
        current_release = release.Release('1.2.3-1')
        new_release = release.Release('1.2.2-3')
        
        self.failIf(not current_release.is_greater(new_release))
        pass
    
    def test_if_infinity_is_greater_than_release(self):
        current_release = release.Release('*')
        new_release = release.Release('1.2.2-3')
        
        self.failIf(not current_release.is_greater(new_release))
        pass

    def test_if_current_release_is_not_greater_than_release(self):
        current_release = release.Release('1.2.3-1')
        new_release = release.Release('1.2.4-3')
        
        self.failIf(current_release.is_greater(new_release))
        pass

    def test_if_current_release_is_not_lower_than_infinity(self):
        current_release = release.Release('1.2.3-1')
        new_release = release.Release('*')
        
        self.failIf(not current_release.is_lower(new_release))
        pass
    
    def test_if_infinity_is_not_lower_than_infinity(self):
        current_release = release.Release('*')
        new_release = release.Release('*')
        
        self.failIf(current_release.is_lower(new_release))
        pass

    def test_if_current_release_is_lower_than_release(self):
        current_release = release.Release('1.2.2-1')
        new_release = release.Release('1.2.3-3')
        
        self.failIf(not current_release.is_lower(new_release))
        pass
    
    def test_if_infinity_is_lower_than_release(self):
        current_release = release.Release('*')
        new_release = release.Release('1.2.2-3')
        
        self.failIf(current_release.is_lower(new_release))
        pass

    def test_if_current_release_is_not_lower_than_release(self):
        current_release = release.Release('1.2.4-1')
        new_release = release.Release('1.2.2-3')
        
        self.failIf(current_release.is_lower(new_release))
        pass

    def test_if_current_release_is_not_greater_and_equal_than_infinity(self):
        current_release = release.Release('1.2.3-1')
        new_release = release.Release('*')
        
        self.failIf(current_release.is_greater_and_equal(new_release))
        pass
    
    def test_if_infinity_is_not_greater_and_equal_than_infinity(self):
        current_release = release.Release('*')
        new_release = release.Release('*')
        
        self.failIf(not current_release.is_greater_and_equal(new_release))
        pass

    def test_if_current_release_is_greater_and_equal_than_release(self):
        current_release = release.Release('1.2.3-3')
        new_release = release.Release('1.2.3-3')
        
        self.failIf(not current_release.is_greater_and_equal(new_release))
        pass
    
    def test_if_infinity_is_greater_and_equal_than_release(self):
        current_release = release.Release('*')
        new_release = release.Release('1.2.2-3')
        
        self.failIf(current_release.is_greater_and_equal(new_release))
        pass

    def test_if_current_release_is_not_greater_and_equal_than_release(self):
        current_release = release.Release('1.2.1-1')
        new_release = release.Release('1.2.2-3')
        
        self.failIf(current_release.is_greater_and_equal(new_release))
        pass


    def test_if_current_release_is_not_lower_and_equal_than_infinity(self):
        current_release = release.Release('1.2.3-1')
        new_release = release.Release('*')
        
        self.failIf(not current_release.is_lower_and_equal(new_release))
        pass
    
    def test_if_infinity_is_not_lower_and_equal_than_infinity(self):
        current_release = release.Release('*')
        new_release = release.Release('*')
        
        self.failIf(not current_release.is_lower_and_equal(new_release))
        pass

    def test_if_current_release_is_lower_and_equal_than_release(self):
        current_release = release.Release('1.2.3-3')
        new_release = release.Release('1.2.3-3')
        
        self.failIf(not current_release.is_lower_and_equal(new_release))
        pass
    
    def test_if_infinity_is_lower_and_equal_than_release(self):
        current_release = release.Release('*')
        new_release = release.Release('1.2.2-3')
        
        self.failIf(current_release.is_lower_and_equal(new_release))
        pass

    def test_if_current_release_is_not_lower_and_equal_than_release(self):
        current_release = release.Release('1.2.5-1')
        new_release = release.Release('1.2.2-3')
        
        self.failIf(current_release.is_lower_and_equal(new_release))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()