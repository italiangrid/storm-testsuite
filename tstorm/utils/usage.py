

def usage_version(opt=True):
    if not opt:
        print """- version is not followed by any value"""
    else:
        print """                   [-v|--version] """

def usage_noreport(opt=True):
    if not opt:
        print """- noreport is not followed by any value"""
    else:
        print """                   [--noreport] """

def usage_novoms(opt=True):
    if not opt:
        print """- novoms is not followed by any values"""
    else:
        print """                   [--novoms]"""

def usage_list(opt=True):
    if not opt:
        print """- list is not followed by any values"""
    else:
        print """                   [-l|--list]"""

def usage_conf(opt=True):
    if not opt:
        print """- conf is followed by a value"""
    else:
        print """                   [-c|--conf] """

def usage_dest_file(opt=True):
    if not opt:
        print """- destfile is followed by a value"""
    else:
        print """                   [-d|--destfile] """

def usage_storm_release(opt=True):
    if not opt:
        print """- storm-release is followed by a value"""
    else:
        print """                   [-r|--storm-release]"""

def usage_ids(opt=True):
        if not opt:
            print """- ids is followed by a sequence of id values separated """
            print """  by , and between '"""
        else:
            print """                   [-i|--ids] """

def usage_file_ids(opt=True):
    if not opt:
        print """- file-ids is followed by a value """
    else:
        print """                   [-f|--file-ids] """

def usage_filter_list(opt=True,run=''):
    if not opt:
        print """- filter-list is followed by a sequence of values separated"""
        print """  by ; and between ', the values of which are"""
        if run == 'sanity':
            print """  t|test=DT filters in relation with the type of tests """
        elif run == 'stress':
            print """  t|test=LT filters in relation with the type of test"""
        else:
            print """  t|test=sequence of types of tests separated by , as """
            print """      (AT,UT,ST,LT) that filters in relation with the """
            print """      the type of test"""
        print """  r|regression=false|true that expresses if the test """
        print """      belongs to the regression category"""
        print """  idenpotent=false|true that expresses if the test belongs """
        print """      to the idenpotent category"""
        print """  o|output=filename that allows user to save ids in the """
        print """      specified filename"""
        print """  f|format=n|name,d|description,range,rfc,i|id,idenpotent that """
        print """      allows user to specify the order of print of test """
        print """      information"""
    else:
        print """                   [-s|--filter-list] """

def usage_nostressreport(opt=True):
    if not opt:
        print """- nostressreport is not followed by any value"""
    else:
        print """                   [--nostressreport] """

def usage_number_cycles(opt=True):
    if not opt:
        print """- number-cycles is followed by a value"""
    else:
        print """                   [-n|--number-cycles] """

def usage_number_hours(opt=True):
    if not opt:
        print """- number-hours is followed by a value"""
    else:
        print """                   [--number-hours] """

def usage_refresh_report(opt=True):
    if not opt:
        print """- refresh-report is followed by a value that"""
        print """    represents time in seconds"""
    else:
        print """                   [--refresh-report] """

def usage_example_noreport(cmd=''):
    print """Example: if you want to run tests without producing a report"""
    print '    %s --noreport' % cmd

def usage_example_ids(cmd=''):
    print """Example: if you want to run tests providing tests sequence"""
    print '    %s -i ' % cmd

def usage_example_number_cycles(cmd=''):
    print """Example: if you want to run tests for n cycles"""
    print '    %s -n 2' % cmd

def usage_example_filter_list(cmd='',run=''):
    print """Example: if you want to get tests information providing a """
    print """filter"""
    if run == 'sanity':
        print "    %s --filter-list 't=DT;regression=true;f=n,d,rfc,id'" % cmd
    elif run == 'stress':
        print "    %s --filter-list 't=LT;regression=true;f=n,d,rfc,id'" % cmd
    else:
        print "    %s --filter-list 't=AT,UT,ST,LT;regression=true;f=n,d,rfc,id'" % cmd

def get_usage(run=''):
    if run == 'sanity':
        cmd = 'tstorm-sanity-test'
    elif run == 'stress':
        cmd = 'tstorm-stress-test'
    else:
        cmd = 'tstorm-test'

    print 'Usage: %s [-h|--help] ' % cmd
    usage_version()
    usage_noreport()
    
    if run == 'stress':
        usage_nostressreport()
        usage_number_cycles()
        usage_number_hours()
        usage_refresh_report()

    if run not in ('sanity', 'stress'):
        usage_novoms()

    if run != 'stress':
        usage_list()
        usage_filter_list()
        usage_ids()
        usage_file_ids()
        usage_conf()

    if run not in ('sanity', 'stress'):
        usage_dest_file()

    usage_storm_release()
    print """where:"""
    usage_version(opt=False)
    usage_noreport(opt=False)

    if run == 'stress':
        usage_nostressreport(opt=False)
        usage_number_cycles(opt=False)
        usage_number_hours(opt=False)
        usage_refresh_report(opt=False)

    if run not in ('sanity', 'stress'):
        usage_novoms(opt=False)

    if run != 'stress':
        usage_list(opt=False)
        usage_filter_list(opt=False,run=run)
        usage_ids(opt=False)
        usage_file_ids(opt=False)
        usage_conf(opt=False)

    if run not in ('sanity', 'stress'):
        usage_dest_file(opt=False)

    usage_storm_release(opt=False)

    usage_example_noreport(cmd=cmd)
    if run != 'stress':
        usage_example_ids(cmd=cmd)
        usage_example_filter_list(cmd=cmd, run=run)
    if run == 'stress':
        usage_example_number_cycles(cmd=cmd)
