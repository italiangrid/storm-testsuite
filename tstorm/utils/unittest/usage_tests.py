'''
Created on Jul 31, 2012

@author: joda
'''
import unittest
from tstorm.utils import usage


class UsageTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_usage_version_with_noopt(self):
        usage.usage_version()

    def test_usage_version_with_opt(self):
        usage.usage_version(opt=False)
        usage.usage_version(opt=false)
        usage.usage_version(opt='what')
        usage.usage_version(opt=true)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
