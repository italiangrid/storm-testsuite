#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

from distutils.core import setup
from distutils.command.install_data import install_data
from distutils.command.install import INSTALL_SCHEMES
import os

cmdclasses = {'install_data': install_data}


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
print root_dir
if root_dir != '':
    os.chdir(root_dir)
tstorm_dir = 'tstorm'

for dirpath, dirnames, filenames in os.walk(tstorm_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

conf_dir = 'conf'
for dirpath, dirnames, filenames in os.walk(conf_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

# Dynamically calculate the version based on django.VERSION.
version = __import__('tstorm').get_version()
if u'SVN' in version:
    version = ' '.join(version.split(' ')[:-1])
release = __import__('tstorm').get_release()

name = "emi-t-storm"

setup(
    name = name,
    version = version.replace(' ', '-'),
    url = 'http://www.storm.it/',
    author = 'StoRM Product Team',
    author_email = 'storm-support@lists.infn.it',
    license = 'Apache',
    description = 'A functional Python testsuite that verifies the StoRM services.',
    download_url = 'to be defined',
    packages = packages,
    scripts = ['bin/tstorm-tp', 'bin/tstorm-test-id'],
    data_files = [
                 ('share/doc/'+ name + '-'+version+'/',['README', 'LICENSE', 'AUTHORS', 'INSTALL']),
                 ('etc/'+name+'/', ['conf/tstorm.ini', 'conf/tstorm-tier1.ini', 'conf/tstorm-tp.json.template', 'conf/tstorm-tp.json', 'conf/map_test_id.json'])]
)
