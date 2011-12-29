#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

from distutils.core import setup
import os

# Dynamically calculate the version based on django.VERSION.
version = __import__('tstorm').get_version()
if u'SVN' in version:
    version = ' '.join(version.split(' ')[:-1])
release = __import__('tstorm').get_release()

name = "tstorm"

setup(
    name = name,
    version = version.replace(' ', '-'),
    url = 'http://www.storm.it/',
    author = 'StoRM Product Team',
    author_email = 'storm-support@lists.infn.it',
    license = 'Apache',
    description = 'A functional Python testsuite that verifies the StoRM services.',
    download_url = 'to be defined',
    packages = ['tstorm', 'tstorm/commands', 'tstorm/utils', 'tstorm/test'],
    scripts = ['bin/tstorm-tp', 'bin/tstorm-test-id'],
    data_files = [
                 ('share/doc/'+ name + '-'+version+'/',['README', 'LICENSE', 'AUTHORS', 'INSTALL']),
                 ('etc/'+name+'/', ['conf/tstorm.ini', 'conf/tstorm-tp.json.template', 'conf/tstorm-tp.json', 'conf/map_test_id.json'])]
)
