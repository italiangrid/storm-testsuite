import sys
import datetime
import time
import os
import json
import check_testplan as ctp

def set_inpt_fn(n_df, n_dfn, subdir=True):
  '''Set Input filename (ifn), Back filename (bfn) and Destinatin filename (dfn)'''

  t=datetime.datetime.now()
  ts=str(time.mktime(t.timetuple()))

  ifn = '/tmp/tstorm-input-file-' + ts + '.txt'
  bfn = '/tmp/tstorm-back-input-file-' + ts + '.txt'

  if n_df:
    if '/' in n_dfn:
      dfn = '/'
      tmp_d = os.path.dirname(n_dfn).split('/')[1:]
      for x in tmp_d:
        dfn = dfn + x + ts + '/'
      dfn = dfn + os.path.basename(n_dfn) + '.' + ts
  else:
    if subdir:
      dfn = '/a'+ ts + '/b' + ts + '/tstorm-output-file-' + ts + '.txt'
    else:
      dfn = '/tstorm-output-file-' + ts + '.txt'

  return ifn,dfn,bfn

def get_tpj_info(tpfnc='tstorm-tp.json'):
  '''Get Test Plan Information from the configuration file of testplan'''
  dirname=os.path.dirname(sys.argv[0])
  configpath = os.path.join(dirname, "../", ".")
  conffile=configpath+tpfnc

  try:
    tp_info=json.read(open(conffile,'r').read())
    
  except (IOError,json.ReadException):
        #dbglog("No stfunc.conf file found or wrong json syntax")
    print "wrong conf file"
    sys.exit(2)
  return tp_info

def print_tpj_template(tpfnc='tstorm-tp.json.template'):
  '''Print Test Plan Information from the configuration template file of testplan'''
  dirname = os.path.dirname(sys.argv[0])
  configpath = os.path.join(dirname, "../", ".")
  conffile = configpath+tpfnc

  try:
    fl=open(conffile,'r')
    tpj_tmtp=fl.readlines()
    for x in tpj_tmtp:
      print x
    fl.close()
    
  except IOError:
    print "I/O error"
    sys.exit(2)
  except:
    print "Unexpected error:", sys.exc_info()[0]
    sys.exit(2)

def is_valid(tp_info):
  '''Check validity of the test plan conf file'''

  result=False

  a=ctp.CheckTestplan()
  kw=a.get_key_word()
  tp_categories=a.get_test_plan_categories()
  available_methods=a.get_test_suites()

  for x in tp_info:
    if x == kw:
      result=True
      break

  try:
    for x in tp_info[kw]:
      if x in tp_categories:
        result=True
        for y in tp_info[x]:
          if y not in available_methods:
            return False
      else:
        return False
  except KeyError:
    return False

  return result
