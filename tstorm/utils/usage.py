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
        print ("  -l, --list                        enable the list of all the" +
            " tests for a given\n " +
            "                                   StoRM release\n" +
            "  -s, --filter-list='SEQUENCE'      specify a sequence of " +
            "values separated by ; \n" +
            "                                    and between , the values of which are:")
        if run == 'sanity':
            print ('                                    t|test=DT filters in relation with\n' +
                '                                        the type of tests ')
        else:
            print ('                                    t|test=sequence of types of tests\n' + 
                '                                        separated by , as AT,UT,ST,LT\n'+
                '                                        that filters in relation with the\n'+
                '                                        type of test\n' +
                '                                    r|regression=false|true that expresses\n'+ 
                '                                        if the test belongs to the regression\n' +
                '                                        category\n' +
                '                                    idenpotent=false|true that expresses\n'+
                '                                        if the test belongs to the idenpotent\n' +
                '                                        category\n' +
                '                                    o|output=filename that allows user to\n'+
                '                                        save test identifiers in the specified\n'+
                '                                        filename\n' +
                '                                    f|format=n|name,d|description,range,rfc,i|id,idenpotent\n' +
                '                                        allows user to specify the order\n'+
                '                                        of print of tests information')
        usage_example_filter_list(cmd=cmd,run=run)
        print ("  -i, --ids='SEQUENCE'              specify a sequence of values separated by ,\n" +
            "                                    the values of which are the tests identifiers\n" +
            "                                    to be executed\n" +  
            "  -f, --file-ids=FILEIDS            specify the file name that contains\n" +
            "                                    the list of tests identifiers to be executed")

    print '  -c, --conf=CONFFILE               specify the configuration file'    

    if run not in ('sanity', 'stress'):
        print '  -d, --destfile=DESTFILE           specify the destination file'

    print ('  -r, --storm-release=<major-release.minor-release.revision-release>-age\n'+
        '                                    specify the StoRM release\n\n'
        'SELinux options:\n' +
        '  -h, --help                        display this help and exit\n' +
        '  -v, --version                     output version information and' +
        ' exit')
