AC_INIT(tstorm, 1.2.0, www.cnaf.infn.it)
AC_CONFIG_SRCDIR([tstorm/__init__.py])
AC_CONFIG_AUX_DIR([./project])

AC_COPYRIGHT([Copyright (C) 2009 the wnodes authors.
This file is distributed under the same license as the x package.])

AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AM_MAINTAINER_MODE

dnl check for python
AM_PATH_PYTHON
# TODO: Check dependencies
AC_PROG_CC

#Environment.
WORKDIR=`pwd`
AC_SUBST(WORKDIR)

TSTORM_VERSION=[`$PYTHON -c "
print __import__('tstorm').get_version();"`]
AC_MSG_RESULT([$TSTORM_VERSION])

TSTORM_AGE=5

if test "$host_cpu" = "x86_64"; then
  t=${libdir##/lib}
  if test "$t" != 64; then
    libdir=${libdir}64
    AC_MSG_RESULT([yes. Set libdir to $libdir])
  else
    AC_MSG_RESULT([no. Set libdir to $libdir])
  fi
else
  AC_MSG_RESULT([no. $host_cpu])
fi

AC_CONFIG_HEADER([autogen/config.h])
AC_CONFIG_FILES([
   Makefile
   bin/Makefile
   conf/Makefile
   tstorm/Makefile
   tstorm/utils/Makefile
   tstorm/commands/Makefile
   tstorm.spec
])

AC_OUTPUT
