__author__ = 'Elisabetta Ronchieri'

import sys
import datetime
import time
import os
import simplejson
import check_testplan as ctp

def set_inpt_fn(n_df, n_dfn, subdir=True):
    '''Set Input filename (ifn), Back filename (bfn) and Destinatin filename (dfn)'''

    t=datetime.datetime.now()
    ts=str(time.mktime(t.timetuple()))

    ifn = '/tmp/tstorm-input-file-' + ts + '.txt'
    bfn = '/tmp/tstorm-back-input-file-' + ts + '.txt'

    if n_df:
        if '/' in n_dfn:
            dfn = '/'
            tmp_d = os.path.dirname(n_dfn).split('/')[1:]
            for x in tmp_d:
                dfn = dfn + x + ts + '/'
            dfn = dfn + os.path.basename(n_dfn) + '.' + ts
    else:
        if subdir:
            dfn = '/a'+ ts + '/b' + ts + '/tstorm-output-file-' + ts + '.txt'
        else:
            dfn = '/tstorm-output-file-' + ts + '.txt'

    return ifn,dfn,bfn

def get_json_file_information(file_name = 'tstorm-tp.json'):
    '''Get Test Plan Information from the configuration file of testplan'''

    json_file = get_configuration_file(file_name)

    try:
        tp_info=simplejson.load(open(json_file,'r'))
    except ValueError, e:
        #dbglog("No stfunc.conf file found or wrong json syntax")
        print "Value Error, wrong conf file"
        sys.exit(2)
        #raise SystemExit(e) 
    #except (IOError, e):
        #dbglog("No stfunc.conf file found or wrong json syntax")
        #print "IOError, wrong conf file"
        #sys.exit(2)
      
    return tp_info

def get_configuration_paths():
    '''Returns the path where you can find configuration file'''

    dir_name = os.path.dirname(sys.argv[0])

    paths = [os.path.join(dir_name, "../", "etc/tstorm/"),
        os.path.join(dir_name, "../", "../", "etc/tstorm/"),
        os.path.join(dir_name, "../", "etc/tstorm/sanity/"),
        os.path.join(dir_name, "../", "../", "etc/tstorm/sanity/"),
        os.path.join(dir_name, "../", "etc/tstorm/common/"),
        os.path.join(dir_name, "../", "../", "etc/tstorm/common/")]

    return paths 

def configuration_path_exists():
    '''Checks the existance of a given path'''

    result=False

    paths = get_configuration_paths()

    for x in paths:
        if os.path.isdir(x):
            #print 'path %s exist ' % x
            result=True
            break

    return result

def get_configuration_path():
    '''Returns the configuration path'''

    result=False

    paths = get_configuration_paths()

    for x in paths:
        if os.path.isdir(x):
            configuration_path = x
            #print 'path %s ' % x
            break

    return configuration_path

def configuration_file_exists(file_name='map_tests_ids.json'):
    '''Checks the existance of a given configuration file'''

    result=False

    paths = get_configuration_paths()

    for x in paths:
        if os.path.isfile(os.path.join(x,file_name)):
            #print 'file %s exist ' % (x+file_name)
            result=True
            break

    return result

def get_configuration_file(file_name='map_tests_ids.json'):
    '''Returns the configuration file'''

    configuration_file=''

    paths = get_configuration_paths()

    for x in paths:
        if os.path.isfile(os.path.join(x,file_name)):
            configuration_file=(x+file_name)
            #print 'file %s ' % configuration_file
            break

    return configuration_file 

def print_json_file_template(file_name = 'tstorm-tp.json.template'):
    '''Print Test Plan Information from the configuration template file of testplan'''

    json_file = get_configuration_file(file_name)

    try:
        fl=open(json_file,'r')
        json_lines=fl.readlines()
        for line in json_lines:
            print line
        fl.close()
    except IOError:
        print "I/O error"
        sys.exit(2)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        sys.exit(2)

def print_configuration_file_template(file_name = 'tstorm.ini.template'):
    '''Print Test Configuration Information from the configuration template file'''

    #json_file = get_configuration_file(file_name)

    #try:
    #    fl=open(json_file,'r')
    #    json_lines=fl.readlines()
    #    for line in json_lines:
    #        print line
    #    fl.close()
    #except IOError:
    #    print "I/O error"
    #    sys.exit(2)
    #except:
    #    print "Unexpected error:", sys.exc_info()[0]
    #    sys.exit(2)

def is_json_file_valid(tp_info):
    '''Check validity of the test plan conf file'''

    result=False

    a=ctp.CheckTestplan()
    kw=a.get_key_word()
    tp_categories=a.get_test_plan_categories()
    available_methods=a.get_test_suites()

    for x in tp_info:
        if x == kw:
            result=True
            break

    try:
        for x in tp_info[kw]:
            if x in tp_categories:
                result=True
                for y in tp_info[x]:
                  if y not in available_methods:
                      return False
            else:
                return False
    except KeyError:
        return False

    return result
