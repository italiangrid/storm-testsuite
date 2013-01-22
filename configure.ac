# Copyright (c) Istituto Nazionale di Fisica Nucleare (INFN). 2006-2010.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Authors: Elisabetta Ronchieri <elisabetta.ronchieri@cnaf.infn.it>
#

AC_PREREQ([2.59])
AC_INIT([tstorm], [2.0.1])
AC_CONFIG_AUX_DIR([./project])
AC_CONFIG_SRCDIR([tstorm/__init__.py])
AM_INIT_AUTOMAKE
AC_CONFIG_MACRO_DIR([m4])

# Release number
osdist=`cat /etc/redhat-release | awk 'BEGIN {FS="release "} {print $2}'| awk 'BEGIN {FS="."} {print $1}'| awk 'BEGIN {FS="("} {print $1}'`
AC_SUBST([TSTORM_OS], [el$osdist])
AC_SUBST([TSTORM_AGE_NUMBER], [9])

# Notices.
AC_COPYRIGHT([See LICENCE file for details])
AC_REVISION([$Revision: $])

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

if test "xel$osdist" = "xel6"; then
  tomcat_version='6'
else
  tomcat_version='5'
fi

AC_SUBST([TOMCATVERSION], [$tomcat_version])

if test "xel$osdist" = "xel6"; then
  mysql_connector_version='-5.1.12'
else
  mysql_connector_version=''
fi

AC_SUBST([MYSQLCONNECTORVERSION], [$mysql_connector_version])

AC_STORM([])

AC_CONFIG_HEADER([autogen/config.h])
AC_CONFIG_FILES([
   Makefile
   bin/Makefile
   conf/Makefile
   tstorm/Makefile
   tstorm/utils/Makefile
   tstorm/run/Makefile
   tstorm/commands/Makefile
   tstorm/tests/Makefile
   tstorm/tests/atomic/Makefile
   tstorm/tests/deployment/Makefile
   tstorm/tests/deployment/services.py
   tstorm/tests/deployment/regression/Makefile
   tstorm/tests/functional/Makefile
   tstorm/tests/functional/regression/Makefile
   tstorm/tests/load/Makefile
   tstorm.spec
])

AC_OUTPUT
