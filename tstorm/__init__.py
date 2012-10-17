__author__ = 'Elisabetta Ronchieri'

VERSION = (2, 0, 0, 4)

def get_version():
    version = '%s.%s.%s-%s' % (VERSION[0], VERSION[1], VERSION[2], VERSION[3])
    from tstorm.utils.version import get_svn_revision
    svn_rev = get_svn_revision()
    if svn_rev != u'SVN-unknown':
        version = "%s %s" % (version, svn_rev)
    return version

def get_release():
    release = VERSION[3]
    return release

def get_storm_release():
    return '1.10.0-1'
