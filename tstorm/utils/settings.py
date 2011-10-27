import sys
import datetime
import time
import os
import json

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

def get_tp_info(tpfnc='tstorm-tp.json'):
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

def is_valid(tp_info):
  '''Check validity of the test plan conf file'''

  result=False

  kw='test_plan'

  tp_keys = ['common_tests',
    'basic_tests',
    'regression_tests',
    'basic_tests_novoms',
    'regression_conftests',
    'regression_ldaptests',
    'tape_tests']

  available_methods = ['cksm_ts',
    'https_ts',
    'https_voms_ts',
    'cs_ts',
    'cw_ts',
    'eight_digit_string_checksum_ts',
    'non_ascii_chars_ts',
    'unsupported_protocols_ts',
    'dt_ts',
    'http_ts',
    'glue_info_ts',
    'glue_storage_share_capacity_ts',
    'glue_available_space_ts',
    'glue_used_space_ts',
    'glue_available_space_info_service_ts',
    'size_ts',
    'update_used_space_upon_pd_ts',
    'update_free_space_upon_rm_ts',
    'storm_backend_age_ts',
    'conf_ts',
    'access_tape_ts',
    'backend_cron_conf_rt',
    'backend_server_status_rt',
    'backend_logrotate_conf_rt',
    'backend_gridhttps_rt',
    'yaim_version_file_rt',
    'gridhttps_plugin_links_rt',
    'size_in_namespace_file_rt',
    'mysql_connector_java_links_rt']

  for x in tp_info:
    if x == kw:
      result=True
      break

  for x in tp_info[kw]:
    if x in tp_keys:
      result=True
      for y in tp_info[x]:
        if y not in available_methods:
          return False
    else:
      return False

  return result
