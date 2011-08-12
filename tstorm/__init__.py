__author__ = 'Elisabetta Ronchieri'

VERSION = (1, 0, 4, 1)

def get_version():
    version = '%s.%s.%s-%s' % (VERSION[0], VERSION[1], VERSION[2], VERSION[3])
    print version 
    from tstorm.utils.version import get_svn_revision
    svn_rev = get_svn_revision()
    if svn_rev != u'SVN-unknown':
        version = "%s %s" % (version, svn_rev)
    print version
    return version
