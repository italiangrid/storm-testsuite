__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import sys
import os
import unittest
import getopt
from tstorm.test import functionalities as fu

def usage():
    print "Usage:  python testsutie.py [-c|--conf] [-d|--destfile]"
    print """Example: python testsutie.py -c tstorm.ini -d /qui/quo/qua"""

def test_suite(conf, ifn, dfn, bifn):
  s = unittest.TestSuite()
  s.addTest(fu.Functionalities('test_settings',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_ping',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_dd',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_ls_bt',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_mkdir_bc',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_mkdir_ac',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_ls_ac',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_cp_bt',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_ls_at',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_cp_at',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_rm',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_rmdir',conf, ifn, dfn, bifn))
  s.addTest(fu.Functionalities('test_rm_lf',conf, ifn, dfn, bifn))
  
  return s

if __name__ == '__main__':
  tfn = '/etc/tstorm/tstorm.ini'

  t=datetime.datetime.now()
  ts=str(time.mktime(t.timetuple()))
  ifn = '/tmp/tstorm-input-file-' + ts + '.txt'
  dfn = '/a'+ ts + '/b' + ts + '/tstorm-output-file-' + ts + '.txt'
  back_ifn = '/tmp/tstorm-back-input-file-' + ts + '.txt'

  try:
    opts, args = getopt.getopt(sys.argv[1:], "hc:d:", ["help","conf","destfile"])
  except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(2)
  
  n_df = False
  for o, v in opts:
    if o in ("-h", "--help"):
      usage()
      sys.exit()
    elif o in ("-c", "--conf"):
      tfn = v
    elif o in ("-d", "--destfile"):
      n_dfn = v
      n_df = True
    else:
      assert False, "unhandled option"

  if n_df:
    t=datetime.datetime.now()
    ts=str(time.mktime(t.timetuple()))
    if '/' in n_dfn:
      dfn = '/'
      tmp_d = os.path.dirname(n_dfn).split('/')[1:]
      for x in tmp_d:
        dfn = dfn + x + ts + '/'
      dfn = dfn + os.path.basename(n_dfn) + '.' + ts

  runner = unittest.TextTestRunner(verbosity=2).run(test_suite(tfn,ifn,dfn,back_ifn))
