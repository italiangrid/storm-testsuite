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

EXTRA_DIST = \
   tstorm-sanity.ini \
   tstorm-sanity-tp.json \
   tstorm-sanity-tp.json.template \
   tstorm.ini \
   tstorm-tp.json \
   tstorm-tp.json.template \
   map_tests_ids.json

tstormsanityconfdir = $(sysconfdir)/tstorm/sanity
dist_tstormsanityconf_DATA = tstorm-sanity.ini \
   tstorm-sanity-tp.json \
   tstorm-sanity-tp.json.template

tstormconfdir = $(sysconfdir)/tstorm/
dist_tstormconf_DATA = tstorm.ini \
   tstorm-tp.json \
   tstorm-tp.json.template

tstormcommonconfdir = $(sysconfdir)/tstorm/common
dist_tstormcommonconf_DATA = map_tests_ids.json

MAINTAINERCLEANFILES = Makefile.in

CLEANFILES=\
   *.in
