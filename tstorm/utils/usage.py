def usage_example_filter_list(cmd='',run=''):
    print ('                                    Example: if you want to get tests\n'+
        '                                    information providing a filter:')
    if run == 'sanity':
        print "                                    %s --filter-list 't=DT;regression=true;f=n,d,rfc,id'" % cmd
    elif run == 'stress':
        print "                                    %s --filter-list 't=LT;regression=true;f=n,d,rfc,id'" % cmd
    else:
        print "                                    %s --filter-list 't=AT,UT,ST,LT;regression=true;f=n,d,rfc,id'" % cmd

def usage_tests(parameters,run=''):
    print ("  --noreport                        disable the generation of" +
        " the report log file.\n" +
        "                                    The DEFAULT value is %s.\n"
        % change_val(parameters['report']) +
        "  -l, --list                        print the list of all the" +
        " specified tests\n " +
        " -s, --filter-list='SEQUENCE'      specify a sequence of " +
        "filtering options separated by ';' " +
        "                                    Available options are:"
        "                                    t|test=list of test types separated by ',':\n" +
        "                                        Available test types are:\n" +
        "                                        AT Atomic Test\n"+
        "                                        UT Utility Test\n"+
        "                                        ST System Test\n"+
        "                                        LT Load Test\n"+
        "                                    r|regression=false|true that expresses\n"+
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

def usage_sanity_tests(parameters,run=''):
    print ("  --noreport                        disable the generation of" +
        " the report log file.\n" +
        "                                    The DEFAULT value is %s.\n"
        % change_val(parameters['report']) +
        "  -l, --list                        print the list of all the" +
        " specified tests\n " +
        " -s, --filter-list='SEQUENCE'      specify a sequence of " +
        "filtering options separated by ';' \n" +
        "                                    Available options are:\n"
        "                                    t|test=test type\n" +
        "                                        Available test type is:\n"+
        "                                        DT Deployment Test\n"+
        "                                    r|regression=false|true that expresses\n"+
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

def usage_stress_tests(parameters):
    print ('  --report                          enable the generation of' +
        ' the report log file.\n'+
        '                                    The DEFAULT value is %s.\n'
        % parameters['report'] +
        '  --nostressreport                  disable the generation of' +
        ' the stress report\n'+
        '                                    log file. The DEFAULT value ' +
        'is %s.\n' % change_val(parameters['stress_report']) +
        '  -n, --number-tests=NUMBERTESTS  specify the number of' +
        ' tests in which stress\n'+
        '                                    tests are executed. The DEFAULT' +
        ' value is %s.\n' % str(parameters['number_tests']) +
        '  --number-hours=NUMBERHOURS        specify the number of' +
        ' hours in which stress\n'+
        '                                    tests are executed. The DEFAULT' +
        ' value is %s.\n' % str(parameters['number_hours']) +
        '  --refresh-report=SECONDS          specify the seconds' +
        ' after which the stress\n'+
        '                                    report file is updated. The DEFAULT \n' +
        '                                    value is %s.'
        % str(parameters['refresh_report']))

def usage_just_tests(parameters):
    print ('  --novoms                          run tests for which voms' +
        ' is not necessary.\n' +
        '                                    The DEFAULT value is %s.\n'
        % change_val(parameters['voms'])+
        '  -d, --destfile=DESTFILE           specify the destination file')
    
def usage_all_tests(cmd):
    print ('Usage: %s [OPTION]\n'
        % cmd +
        'Run tests\n\n' +
        'OPTION\n'
        '  -c, --conf=CONFFILE               specify the configuration file\n'
        '  -r, --storm-release=<major-release.minor-release.revision-age>\n'+
        '                                    specify the StoRM target release\n\n'
        '  -h, --help                        display this help and exit\n' +
        '  -v, --version                     output version information and' +
        ' exit')

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
    
    usage_all_tests(cmd)
 
    if run == 'stress':
        usage_stress_tests(parameters)

    if run not in ('sanity', 'stress'):
        usage_just_tests(parameters)

    if run != 'stress':
        if run == 'sanity':
            usage_sanity_tests(parameters,run=run)    
        else:
            usage_tests(parameters,run=run)

    usage_all_tests()
