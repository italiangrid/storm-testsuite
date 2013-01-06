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

def usage_example_storm_release(cmd=''):
    print """Example: if you want to run tests specifying storm release"""
    print "    %s -r '<major-release.minor-release.revision-release>-age'" % cmd

def usage_example_ids(cmd=''):
    print """Example: if you want to run tests providing a sequence of test ids"""
    print "    %s -i '<test_id_1>,<test_id_2>" % cmd

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

    print ('Usage: %s [OPTION]\n'
        % cmd +
        'Run tests\n\n' +
        'Mandatory arguments to long options are mandatory for short options ' +
        'too\n')

    if run != 'stress':
        print '    --noreport  disable the generation of the report log file'
    
    if run == 'stress':
        print '    --report    enable the generation of the report log file'
        print '    --nostressreport  disable the generation of the stress report log file'
        print '    -n, --number-cycles=NUMBERCYCLES   specify the number of cycles in which stress tests are executed'
        print '    --number-hours=NUMBERHOURS  specify the number of hours in which stress tests are executed'
        print '    --refresh-report=SECONDS  specify the seconds after which the stress report is updated'

    if run not in ('sanity', 'stress'):
        print '    --novoms    run tests for which voms is not necessary'

    if run != 'stress':
        print '    -l, --list  enable the list of tests'
        print "    -s, --filter-list='SEQUENCE'  specify a sequence of values separated by ; and between , the value of which are"
        if run == 'sanity':
            print '        t|test=DT filters in relation with the type of tests '
        else:
            print '       t|test=sequence of types of tests separated by , as '
            print '            (AT,UT,ST,LT) that filters in relation with the '
            print '           the type of test'
        print '        r|regression=false|true that expresses if the test '
        print '            belongs to the regression category'
        print '        idenpotent=false|true that expresses if the test belongs '
        print '            to the idenpotent category'
        print '        o|output=filename that allows user to save ids in the '
        print '           specified filename'
        print '        f|format=n|name,d|description,range,rfc,i|id,idenpotent that '
        print '            allows user to specify the order of print of test '
        print '            information'
        print "    -i, --ids='<test_id_1>,<test_id_2>,...'  specify the list of tests identifiers to be executed"  
        print '    -f, --file-ids=FILEIDS specify the file name that contains the list of tests identifiers to be executed'

    print '    -c, --conf=CONFFILE  specify the configuration file'    

    if run not in ('sanity', 'stress'):
        print '    -d, --destfile=DESTFILE  specify the destination file'

    print '    -r, --storm-release=<major-release.minor-release.revision-release>-age  specify the StoRM release\n'

    print ('SELinux options:\n' +
        '    -h, --help display this help and exit\n' +
        '    -v, --version output version information and exit')
