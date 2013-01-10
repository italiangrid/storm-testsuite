def usage_example_filter_list(cmd='',run=''):
    print ('                                    Example: if you want to get tests\n'+
        '                                    information providing a filter:')
    if run == 'sanity':
        print "                                    %s --filter-list 't=DT;regression=true;f=n,d,rfc,id'" % cmd
    elif run == 'stress':
        print "                                    %s --filter-list 't=LT;regression=true;f=n,d,rfc,id'" % cmd
    else:
        print "                                    %s --filter-list 't=AT,UT,ST,LT;regression=true;f=n,d,rfc,id'" % cmd

def change_val(value):
    if value:
        return False
    return True

def get_usage(parameters, run=''):
    if run == 'sanity':
        cmd = 'tstorm-sanity-tests'
    elif run == 'stress':
        cmd = 'tstorm-stress-tests'
    else:
        cmd = 'tstorm-tests'

    print ('Usage: %s [OPTION]\n'
        % cmd +
        'Run tests\n\n' +
        'OPTION')

    if run != 'stress':
        print ('  --noreport                        disable the generation of' +
            ' the report log file.\n' +
            '                                    The DEFAULT of which is %s.'
            % change_val(parameters['report']))
    
    if run == 'stress':
        print ('  --report                          enable the generation of' +
            ' the report log file.\n'+
            '                                    The DEFAULT of which is %s.\n'
            % parameters['report'] +
            '  --nostressreport                  disable the generation of' +
            ' the stress report\n'+
            '                                    log file. The DEFAULT of ' +
            'which is %s.\n' % change_val(parameters['stress_report']) +
            '  -n, --number-cycles=NUMBERCYCLES  specify the number of' +
            ' cycles in which stress\n'+
            '                                    tests are executed. The DEFAULT' +
            ' of which is %s.\n' % str(parameters['number_cycles']) +
            '  --number-hours=NUMBERHOURS        specify the number of' +
            ' hours in which stress\n'+
            '                                    tests are executed. The DEFAULT' +
            ' of which is %s.\n' % str(parameters['number_hours']) +
            '  --refresh-report=SECONDS          specify the seconds' +
            ' after which the stress\n'+
            '                                    report file is updated. The DEFAULT of\n' +
            '                                    which is %s.'
            % str(parameters['refresh_report']))

    if run not in ('sanity', 'stress'):
        print ('  --novoms                          run tests for which voms' +
            ' is not necessary.\n' +
            '                                    The DEFAULT of which is %s.'
            % change_val(parameters['voms']))

    if run != 'stress':
        print ("  -l, --list                        print the list of all the" +
            " specified tests\n " +
            " -s, --filter-list='SEQUENCE'      specify a sequence of " +
            "filtering options separated by ';' \n" +
            "                                    Available options are:")
        if run == 'sanity':
            print ('                                    t|test=test type\n' +
                '                                        Available test type is:\n'+
                '                                        DT Deployment Test')
        else:
            print ("                                    t|test=list of test types separated by ',':\n" + 
                "                                        Available test types are:\n" +
                "                                        AT Atomic Test\n"+
                "                                        UT Utility Test\n"+
                "                                        ST System Test\n"+
                "                                        LT Load Test")
        print ("                                    r|regression=false|true that expresses\n"+ 
            "                                        if the test belongs to the regression\n" +
            "                                        category\n" +
            "                                    idenpotent=false|true that expresses\n"+
            "                                        if the test belongs to the idenpotent\n" +
            "                                        category\n" +
            "                                    o|output=filename that allows user to\n"+
            "                                        save test identifiers in the specified\n"+
            "                                        filename\n" +
            "                                    f|format=list of tests information, fields \n"+
            "                                        separated by ',', printed following the \n"+
            "                                        order of the format:\n"+
            "                                        n|name        is the name of the test\n"+
            "                                        d|description is the description of the test\n"+
            "                                        range         specifies the range in which the test is valid\n"+
            "                                        rfc           is the rfc identifier specified in the TestPlan\n"+
            "                                        i|id          is the test identifier\n"+
            "                                        idenpotent    specifies if the test is idenpotent or not\n" +
            "                                        r|regression  specifies if the test is a regression one or not")
        usage_example_filter_list(cmd=cmd,run=run)
        print ("  -i, --ids='SEQUENCE'              specify a sequence of tests identifiers\n" +
            "                                    separated by ','. Only the specified tests will\n" +
            "                                    be executed.\n"
            "  -f, --file-ids=FILEIDS            specify the file name that contains\n" +
            "                                    the list of tests identifiers to be executed")

    print '  -c, --conf=CONFFILE               specify the configuration file'    

    if run not in ('sanity', 'stress'):
        print '  -d, --destfile=DESTFILE           specify the destination file'

    print ('  -r, --storm-release=<major-release.minor-release.revision-age>\n'+
        '                                    specify the StoRM target release\n\n'
        '  -h, --help                        display this help and exit\n' +
        '  -v, --version                     output version information and' +
        ' exit')
