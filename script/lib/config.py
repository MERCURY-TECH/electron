#!/usr/bin/env python

import errno
import os
import platform
import sys


BASE_URL = 'http://gh-contractor-zcbenz.s3.amazonaws.com/libchromiumcontent'
LIBCHROMIUMCONTENT_COMMIT = 'f1ad1412461ba3345a27cfe935ffc872dba0ac5b'

PLATFORM = {
  'cygwin': 'win32',
  'darwin': 'darwin',
  'linux2': 'linux',
  'win32': 'win32',
}[sys.platform]

verbose_mode = False


def get_target_arch():
  # Always build 64bit on OS X.
  if PLATFORM == 'darwin':
    return 'x64'
  # Only build for host's arch on Linux.
  elif PLATFORM == 'linux':
    if platform.architecture()[0] == '32bit':
      return 'ia32'
    else:
      return 'x64'
  # On Windows it depends on user.
  elif PLATFORM == 'win32':
    try:
      target_arch_path = os.path.join(__file__, '..', '..', '..', 'vendor',
                                      'brightray', 'vendor', 'download',
                                      'libchromiumcontent', '.target_arch')
      with open(os.path.normpath(target_arch_path)) as f:
        return f.read().strip()
    except IOError as e:
      if e.errno != errno.ENOENT:
        raise
    # Build 32bit by default.
    return 'ia32'
  # Maybe we will support other platforms in future.
  else:
    return 'x64'


def enable_verbose_mode():
  print 'Running in verbose mode'
  global verbose_mode
  verbose_mode = True


def is_verbose_mode():
  return verbose_mode
