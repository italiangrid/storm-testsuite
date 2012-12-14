import datetime
import time
import os 
import unittest
from tstorm.utils import configuration
from tstorm.utils import ldapsearch as ls 
from tstorm.utils import infosystem as ins
from tstorm.utils import utils

__author__ = 'Elisabetta Ronchieri'

class InfoTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn, filter='', attributes=''):
        super(LdapTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.filter = filter
        self.attributes = attributes
        self.id = uid.get_id()
        self.lfn=lfn

    def test_available_space_info_service(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                self.filter, self.attributes, self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            for x in ls_result['glue1.3']['GlueSALocalID']:
                #print x.split(':')[0].upper().replace('.','').replace('-','')
                info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                    self.tsets['general']['info_port'],
                    x.split(':')[0].upper().replace('.','').replace('-',''))
                self.lfn.put_cmd(info_system.get_command())
                ins_result = info_system.get_output()

                msg = 'Wrong available space value'
                self.assert_(int(ins_result['available-space']) > 0,
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_available_space(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                self.filter, self.attributes, self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            for x in ls_result['glue1.3']['GlueSALocalID']:
                ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                    "(&(objectclass=GlueSA)(GlueSALocalID="+x+"))",
                    ['GlueSAFreeOnlineSize','GlueSAStateAvailableSpace'],
                    self.tsets['bdii']['basedn'])
                self.lfn.put_cmd('')
                ls_result = ldap_search.get_output()

                msg = 'ldap status'
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

                info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                    self.tsets['general']['info_port'],
                    x.split(':')[0].upper().replace('.','').replace('-',''))
                self.lfn.put_cmd(info_system.get_command())
                ins_result = info_system.get_output()
                fskb=int(int(ins_result['available-space'])*1000*1000*1000/(1024*1024*1024))/1000

                msg = 'Wrong GlueSAStateAvailableSpace value'
                self.assert_(int(ls_result['glue1.3']['GlueSAStateAvailableSpace']) == int(fskb),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

                fsgb=int(int(ins_result['available-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)

                msg = 'Wrong GlueSAFreeOnlineSize value'
                self.assert_(int(ls_result['glue1.3']['GlueSAFreeOnlineSize']) == int(fsgb),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_used_space(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                self.filter, self.attributes, self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap satus'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            for x in ls_result['glue1.3']['GlueSALocalID']:
                ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                    "(&(objectclass=GlueSA)(GlueSALocalID="+x+"))",
                    ['GlueSAUsedOnlineSize', 'GlueSAStateUsedSpace'],
                    self.tsets['bdii']['basedn'])
                self.lfn.put_cmd('')
                ls_result = ldap_search.get_output()

                msg = 'ldap status'
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

                info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                    self.tsets['general']['info_port'],
                    x.split(':')[0].upper().replace('.','').replace('-',''))
                self.lfn.put_cmd(info_system.get_command())
                ins_result = info_system.get_output()
                uskb=int(int(ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/1000

                msg = 'Wrong GlueSAStateUsedSpace value'
                self.assert_(int(ls_result['glue1.3']['GlueSAStateUsedSpace']) == int(uskb),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
                usgb=int(int(ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)

                msg = 'Wrong GlueSAUsedOnlineSize value'
                self.assert_(int(ls_result['glue1.3']['GlueSAUsedOnlineSize']) == int(usgb),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_size(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                self.filter, self.attributes, self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap search'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            for x in ls_result['glue1.3']['GlueSALocalID']:
                ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                    "(&(objectclass=GlueSA)(GlueSALocalID="+x+"))",
                    ['GlueSATotalOnlineSize', 'GlueSAUsedOnlineSize',
                    'GlueSAFreeOnlineSize', 'GlueSAReservedOnlineSize',
                    'GlueSATotalNearlineSize'],
                    self.tsets['bdii']['basedn'])
                self.lfn.put_cmd('')
                ls_result = ldap_search.get_output()

                msg = 'ldap status'
                self.assert_(ls_result['status'] == 'PASS',
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

                info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                    self.tsets['general']['info_port'],
                    x.split(':')[0].upper().replace('.','').replace('-',''))
                self.lfn.put_cmd(info_system.get_command())
    
                ins_result = info_system.get_output()
                usgb=int(int(ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)

                msg = 'Wrong GlueSAUsedOnlineSize value'
                self.assert_(int(ls_result['glue1.3']['GlueSAUsedOnlineSize']) == int(usgb),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
                tsgb=int(int(ins_result['total-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)

                msg = 'Wrog GlueSATotalOnlineSize value'
                self.assert_(int(ls_result['glue1.3']['GlueSATotalOnlineSize']) == int(tsgb),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
                fsgb=int(int(ins_result['free-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)

                msg = 'Wrong GlueSAFreeOnlineSize value'
                self.assert_(int(ls_result['glue1.3']['GlueSAFreeOnlineSize']) == int(fsgb),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
                rsgb=int(int(ins_result['reserved-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)

                msg = 'Wrong GlueSAReservedOnlineSize value'
                self.assert_(int(ls_result['glue1.3']['GlueSAReservedOnlineSize']) >= int(rsgb),
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))

                msg = 'Wrong GlueSATotalNearlineSize value'
                self.assert_(int(ls_result['glue1.3']['GlueSATotalNearlineSize']) >= 0,
                    '%s, %s - FAILED, %s, Test ID %s' %
                    (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()

    def test_service_failure(self):
        stack_value = inspect.stack()[0]
        path = stack_value[1]
        method = stack_value[3]

        try:
            ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                self.filter, self.attributes, self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()

            msg = 'ldap status'
            self.assert_(ls_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            x=ls_result['glue1.3']['GlueSALocalID'][0]
            info1_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                self.tsets['general']['info_port'],
                x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info1_system.get_command())
            ins1_result = info1_system.get_output()

            msg = 'info status'
            self.assert_(ins1_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            update_attrs={}
            update_attrs['used'] = '1024'
            update_attrs['unavailable'] = '1024'

            info2_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                self.tsets['general']['info_port'],
                x.split(':')[0].upper().replace('.','').replace('-',''),
                attrs=update_attrs)
            self.lfn.put_cmd(info2_system.get_command(in_write=True))
            ins2_result = info2_system.get_output(in_write=True)

            msg = 'info status'
            self.assert_(ins2_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            info3_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                self.tsets['general']['info_port'],
                x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info3_system.get_command())
            ins3_result = info3_system.get_output()

            msg = 'info status'
            self.assert_(ins3_result['status'] == 'PASS',
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong used value'
            self.assert_(int(ins3_result['used-space']) == int(update_attrs['used']),
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            new_busy = int(ins1_result['busy-space']) + int(ins3_result['used-space']) - int(ins1_result['used-space'])

            msg = 'Wrong busy value'
            self.assert_(int(ins3_result['busy-space']) == new_busy,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            new_free = int(ins1_result['total-space']) - int(ins3_result['used-space'])

            msg = 'Wrong free value'
            self.assert_(int(ins3_result['free-space']) == new_free,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
            new_available = int(ins1_result['total-space']) - int(ins3_result['used-space'])

            msg = 'Wrong available value'
            self.assert_(int(ins3_result['available-space']) == new_available,
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong total value'
            self.assert_(int(ins3_result['total-space']) == int(ins1_result['total-space']),
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))

            msg = 'Wrong reserved value'
            self.assert_(int(ins3_result['reserved-space']) == int(ins1_result['reserved-space']),
                '%s, %s - FAILED, %s, Test ID %s' %
                (path, method, msg, self.id))
        except AssertionError, err:
            print err
            self.lfn.put_result('FAILED')
        else:
            self.lfn.put_result('PASSED')

        self.lfn.flush_file()
