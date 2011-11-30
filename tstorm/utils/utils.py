#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import os
import commands

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
              return True
    return False

def run_voms_proxy_info():
    a=()
    if cmd_exist('voms-proxy-info'):
        a=commands.getstatusoutput('voms-proxy-info --all')
    return a

def get_proxy_path():
    a=run_voms_proxy_info()
    if len(a) > 0 and a[0] == 0:
        return 'PASS', a[1].split('path')[1].split(':')[1].split('\n')[0]

    return 'FAILURE', ''

def get_uuid():
    return commands.getoutput('uuidgen')

