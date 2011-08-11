import datetime
import time
import os

def set_inpt_fn(n_df,n_dfn,subdir=True):
  t=datetime.datetime.now()
  ts=str(time.mktime(t.timetuple()))

  ifn = '/tmp/tstorm-input-file-' + ts + '.txt'
  back_ifn = '/tmp/tstorm-back-input-file-' + ts + '.txt'

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

  return ifn,dfn,back_ifn
