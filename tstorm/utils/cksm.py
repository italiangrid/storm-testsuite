__author__ = 'Elisabetta Ronchieri'

import sys
from zlib import adler32
BLOCKSIZE=4*1024*1024

class CksmLf:
  def __init__(self, ifn):
    self.ifn = ifn
    self.otpt = {
      'Checksum': ''}

  def get_output(self):
    fp=open(self.ifn)
    val=1
    while True:
      data = fp.read(BLOCKSIZE)
      if not data:
        break
      val = adler32(data, val)
    if val < 0:
      val += 2**32

    self.otpt['Checksum'] = str(hex(val)[2:10].zfill(8).lower()) +  ' (ADLER32)'
    return self.otpt
