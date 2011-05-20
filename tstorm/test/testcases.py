import datetime
import time
import sys
import unittest
from tstorm.test import sequence_functionalities as sf

def test_suite(conf, ifn, dfn, bifn):
  s = unittest.TestSuite()
  s.addTest(sf.SequenceFunctionalities('test_settings',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_ping',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_dd',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_ls_bt',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_mkdir_bc',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_mkdir_ac',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_ls_ac',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_cp_bt',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_ls_at',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_cp_at',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_rm',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_rmdir',conf, ifn, dfn, bifn))
  s.addTest(sf.SequenceFunctionalities('test_rm_lf',conf, ifn, dfn, bifn))
  
  return s

if __name__ == '__main__':
  tfn = '/etc/tstorm.ini'
  t=datetime.datetime.now()
  ts=str(time.mktime(t.timetuple()))
  ifn = '/tmp/tstorm-input-file-' + ts + '.txt'
  dfn = '/a/b/tstorm-output-file-' + ts + '.txt'
  back_ifn = '/tmp/tstorm-back-input-file-' + ts + '.txt'
  if len(sys.argv) > 0:
    tfn = sys.argv[1]

  runner = unittest.TextTestRunner(verbosity=2).run(test_suite(tfn,ifn,dfn,back_ifn))
