import os

def is_bin(cmd):
  return os.path.exists(cmd) and os.access(cmd, os.X_OK)

def cmd_exist(cmd):
  fpath, fname = os.path.split(cmd)
  if fpath:
    if is_bin(cmd):
      return True
  else:
    for path in os.environ["PATH"].split(os.pathsep):
      tmp_cmd = os.path.join(path,cmd)
      if is_bin(tmp_cmd):
        cmd['name'] = tmp_cmd
        return True
  return False
