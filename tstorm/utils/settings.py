__author__ = 'Elisabetta Ronchieri'

import sys
import datetime
import time
import os
import simplejson
import check_testplan as ctp
import utils


def set_inpt_fn(n_df, n_dfn, path='', subdir=True):
    '''Set Input filename (ifn), Back filename (bfn) and Destinatin filename (dfn)'''

    #t=datetime.datetime.now()
    #ts=str(time.mktime(t.timetuple()))

    id = utils.get_uuid()
    #ifn = path + '/tstorm-input-file-' + ts + '.txt'
    #bfn = path + '/tstorm-back-input-file-' + ts + '.txt'
    ifn = path + '/tstorm-input-file-' + id + '.txt'
    bfn = path + '/tstorm-back-input-file-' + id + '.txt'

    if n_df:
        if '/' in n_dfn:
            dfn = '/'
            tmp_d = os.path.dirname(n_dfn).split('/')[1:]
            for x in tmp_d:
                dfn = dfn + x + id + '/'
                #dfn = dfn + x + ts + '/'
            #dfn = dfn + os.path.basename(n_dfn) + '.' + ts
            dfn = dfn + os.path.basename(n_dfn) + '.' + id
    else:
        if subdir:
            dfn = '/a'+ id + '/b' + id + '/tstorm-output-file-' + id + '.txt'
            #dfn = '/a'+ ts + '/b' + ts + '/tstorm-output-file-' + ts + '.txt'
        else:
            dfn = '/tstorm-output-file-' + id + '.txt'
            #dfn = '/tstorm-output-file-' + ts + '.txt'

    return ifn,dfn,bfn

def get_json_file_information(file_name = 'tstorm-tp.json'):
    '''Get Test Plan Information from the configuration file of testplan'''

    json_file = get_configuration_file(file_name)

    try:
        tp_info=simplejson.load(open(json_file,'r'))
    except ValueError, err:
        print "Wrong json file: %s" % err
        sys.exit(2)
      
    return tp_info

def get_configuration_paths():
    '''Get the path where you can find configuration file'''

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

    result=True

    paths = get_configuration_paths()

    for x in paths:
        if not os.path.isdir(x):
            #print 'path %s does not exist ' % x
            result=False
            break
        else:
            print 'path %s exist ' % x

    return result

def get_configuration_path(file_name='map_tests_ids.json'):
    '''Get the configuration path'''
    print file_name
    configuration_path = os.path.dirname(file_name)

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

def is_tests_sequence_valid(ts_info, uid):
    '''Check validity of the tests sequence'''
    result=False

    for x in ts_info:
        for y in uid:
            if x == y[0]:
                result=True
        if not result:
            break

    return result

def file_exists(file_name):
    '''Check if the file exists'''

    if os.path.isfile(file_name):
        return True

    return False

def get_tests_sequence(file_name):
    '''Get Tests Sequence from file'''

    in_file = open(file_name,"r")
    text = in_file.read()
    in_file.close()
    sequence = []

    for x in text.split('\n'):
        r = x.strip()
        if r != '':
            sequence.append(r)

    return sequence
