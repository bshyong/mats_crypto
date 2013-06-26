# (c) 2013 Benjamin Shyong.  All rights reserved.
import base64

def hex2b64(input):
  return base64.b64encode(bytearray.fromhex(input))