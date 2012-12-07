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
        usage.usage_version(opt='false')
        usage.usage_version(opt=True)

    def test_usage_noreport_with_noopt(self):
        usage.usage_noreport()

    def test_usage_noreport_with_opt(self):
        usage.usage_noreport(opt=False)
        usage.usage_noreport(opt='false')
        usage.usage_noreport(opt=True)

    def test_usage_novoms_with_noopt(self):
        usage.usage_novoms()

    def test_usage_novoms_with_opt(self):
        usage.usage_novoms(opt=False)
        usage.usage_novoms(opt='false')
        usage.usage_novoms(opt=True)

    def test_usage_list_with_noopt(self):
        usage.usage_list()

    def test_usage_list_with_opt(self):
        usage.usage_list(opt=False)
        usage.usage_list(opt='false')
        usage.usage_list(opt=True)

    def test_usage_conf_with_noopt(self):
        usage.usage_conf()

    def test_usage_conf_with_opt(self):
        usage.usage_conf(opt=False)
        usage.usage_conf(opt='false')
        usage.usage_conf(opt=True)

    def test_usage_dest_file_with_noopt(self):
        usage.usage_dest_file()

    def test_usage_dest_file_with_opt(self):
        usage.usage_dest_file(opt=False)
        usage.usage_dest_file(opt='false')
        usage.usage_dest_file(opt=True)

    def test_usage_storm_release_with_noopt(self):
        usage.usage_storm_release()

    def test_usage_storm_release_with_opt(self):
        usage.usage_storm_release(opt=False)
        usage.usage_storm_release(opt='false')
        usage.usage_storm_release(opt=True)

    def test_usage_ids_with_noopt(self):
        usage.usage_ids()

    def test_usage_ids_with_opt(self):
        usage.usage_ids(opt=False)
        usage.usage_ids(opt='false')
        usage.usage_ids(opt=True)

    def test_usage_filter_list_with_noopt(self):
        usage.usage_filter_list()

    def test_usage_filter_list_with_opt(self):
        usage.usage_filter_list(opt=False)
        usage.usage_filter_list(opt='false')
        usage.usage_filter_list(opt=True)
        usage.usage_filter_list(opt=False, run='sanity')
        usage.usage_filter_list(opt=False, run='stress')
        usage.usage_filter_list(opt=False, run='what')
        usage.usage_filter_list(opt=True, run='')

    def test_usage_nostressreport_with_noopt(self):
        usage.usage_nostressreport()

    def test_usage_nostressreport_with_opt(self):
        usage.usage_nostressreport(opt=False)
        usage.usage_nostressreport(opt='false')
        usage.usage_nostressreport(opt=True)

    def test_usage_number_cycles_with_noopt(self):
        usage.usage_number_cycles()

    def test_usage_number_cycles_with_opt(self):
        usage.usage_number_cycles(opt=False)
        usage.usage_number_cycles(opt='false')
        usage.usage_number_cycles(opt=True)

    def test_usage_number_hours_with_noopt(self):
        usage.usage_number_hours()

    def test_usage_number_hours_with_opt(self):
        usage.usage_number_hours(opt=False)
        usage.usage_number_hours(opt='false')
        usage.usage_number_hours(opt=True)

    def test_usage_refresh_report_with_noopt(self):
        usage.usage_refresh_report()

    def test_usage_refresh_report_with_opt(self):
        usage.usage_refresh_report(opt=False)
        usage.usage_refresh_report(opt='false')
        usage.usage_refresh_report(opt=True)

    def test_usage_example_noreport_with_noopt(self):
        usage.usage_example_noreport()

    def test_usage_example_noreport_with_opt(self):
        usage.usage_example_noreport(cmd='tstorm-tests')
        usage.usage_example_noreport(cmd='tstorm-stress-tests')
        usage.usage_example_noreport(cmd='')

    def test_usage_example_ids_with_noopt(self):
        usage.usage_example_ids()

    def test_usage_example_ids_with_opt(self):
        usage.usage_example_ids(cmd='tstorm-tests')
        usage.usage_example_ids(cmd='tstorm-stress-tests')
        usage.usage_example_ids(cmd='')

    def test_usage_example_number_cycles_with_noopt(self):
        usage.usage_example_number_cycles()

    def test_usage_example_number_cycles_with_opt(self):
        usage.usage_example_number_cycles(cmd='tstorm-tests')
        usage.usage_example_number_cycles(cmd='tstorm-stress-tests')
        usage.usage_example_number_cycles(cmd='')

    def test_usage_example_filter_list_with_noopt(self):
        usage.usage_example_filter_list()

    def test_usage_example_filter_list_with_opt(self):
        usage.usage_example_filter_list(cmd='tstorm-tests')
        usage.usage_example_filter_list(cmd='tstorm-stress-tests')
        usage.usage_example_filter_list(cmd='')
        usage.usage_example_filter_list(cmd='tstorm-tests', run='sanity')
        usage.usage_example_filter_list(cmd='tstorm-stress-tests', run='stress')
        usage.usage_example_filter_list(cmd='', run='')

    def test_get_usage_with_noopt(self):
        usage.get_usage()

    def test_get_usage_with_opt(self):
        usage.get_usage(run='sanity')
        usage.get_usage(run='stress')
        usage.get_usage(run='what')
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
