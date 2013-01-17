__author__ = 'Elisabetta Ronchieri'

import unittest
from tstorm.tests.functional import webdav
from tstorm.tests import utilities 

def ts_webdav_get_directory_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(webdav.WebdavTest('test_webdav_get_directory_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_webdav_put_file_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_file_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_body_in_file_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_body_in_file_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_overwritten_file_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_overwritten_file_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_body_in_overwritten_file_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_body_in_overwritten_file_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_mkcol_directory_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_mkcol_directory_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_file_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_file_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_directory_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_directory_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_full_directory_over_http_as_anonymous(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_full_directory_over_http_as_anonymous',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_get_directory_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(webdav.WebdavTest('test_webdav_get_directory_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_webdav_put_file_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_file_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_body_in_file_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_body_in_file_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_overwritten_file_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_overwritten_file_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_body_in_overwritten_file_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_body_in_overwritten_file_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_mkcol_directory_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_mkcol_directory_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_file_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_file_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_directory_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_directory_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_full_directory_over_https_with_voms(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_full_directory_over_https_with_voms',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_get_directory_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(webdav.WebdavTest('test_webdav_get_directory_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    return s

def ts_webdav_put_file_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_file_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_body_in_file_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_body_in_file_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_overwritten_file_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_overwritten_file_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_put_body_in_overwritten_file_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_put_body_in_overwritten_file_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_mkcol_directory_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_mkcol_directory_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_file_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_file_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_directory_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_directory_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s

def ts_webdav_delete_full_directory_over_https_with_user_cert(conf, ifn, dfn, bifn, uid, lfn):
    s = unittest.TestSuite()
    s.addTest(utilities.UtilitiesTest('test_cr_lf',conf, ifn, bifn, uid, lfn))
    s.addTest(webdav.WebdavTest('test_webdav_delete_full_directory_over_https_with_user_cert',conf, ifn, dfn, bifn, uid, lfn))
    s.addTest(utilities.UtilitiesTest('test_rm_lf',conf, ifn, bifn, uid, lfn))
    return s
