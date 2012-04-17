import datetime
import time
import os 
import unittest
from tstorm.utils import configuration
from tstorm.utils import ldapsearch as ls 
from tstorm.utils import infosystem as ins
from tstorm.utils import utils

__author__ = 'Elisabetta Ronchieri'

class LdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, uid, lfn, filter='', attributes=''):
        super(LdapTest, self).__init__(testname)
        self.tsets = configuration.LoadConfiguration(conf_file = tfn).get_test_settings()
        self.filter = filter
        self.attributes = attributes
        self.uid = uid
        self.lfn=lfn

    def test_glue_service(self):
        name = '''STORM BUG: GLUESERVICENAME AND GLUESERVIVETYPE CONTAIN WRONG
VALUES'''
        self.lfn.put_name(name)
        des = '''Yaim-Storm for GLUE2 configuration called a worng script
setting wrong values in the GlueServiceName and GlueServiceType attributes of
the GLUE1.3 schema.'''
        self.lfn.put_description(des)
        if self.uid.has_key('test_glue_service'):
            self.lfn.put_uuid(self.uid['test_glue_service'])
        else:
            print 'ADD UID for test_glue_service'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/143')
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            self.filter, self.attributes, self.tsets['bdii']['basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')
        self.assert_('emi.storm' not in ls_result['glue1.3']['GlueServiceType'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_glue_available_space_info_service(self):
        self.lfn.put_name('INFO SERVICE ALWAYS RETURNS A ZERO AVAILABLE SPACE')
        self.lfn.put_description('Info Service always returns a zero available space')
        if self.uid.has_key('test_glue_available_space_info_service'):
            self.lfn.put_uuid(self.uid['test_glue_available_space_info_service'])
        else:
            print 'ADD UID for test_glue_available_space_info_service'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/147')
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            self.filter, self.attributes, self.tsets['bdii']['basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        for x in ls_result['glue1.3']['GlueSALocalID']:
            #print x.split(':')[0].upper().replace('.','').replace('-','')
            info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                self.tsets['general']['info_port'],
                x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info_system.get_command())
            ins_result = info_system.get_output()
            self.assert_(int(ins_result['available-space']) > 0)

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_glue_available_space(self):
        self.lfn.put_name('WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB')
        self.lfn.put_description('Wrong calculation of SA_AVAILABLE_SPACE')
        if self.uid.has_key('test_glue_available_space'):
            self.lfn.put_uuid(self.uid['test_glue_available_space'])
        else:
            print 'ADD UID for test_glue_available_space'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/150')
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            self.filter, self.attributes, self.tsets['bdii']['basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        for x in ls_result['glue1.3']['GlueSALocalID']:
            ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                "(&(objectclass=GlueSA)(GlueSALocalID="+x+"))",
                ['GlueSAFreeOnlineSize','GlueSAStateAvailableSpace'],
                self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()
            self.assert_(ls_result['status'] == 'PASS')

            info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                self.tsets['general']['info_port'],
                x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info_system.get_command())
            ins_result = info_system.get_output()
            fskb=int(int(ins_result['available-space'])*1000*1000*1000/(1024*1024*1024))/1000
            self.assert_(int(ls_result['glue1.3']['GlueSAStateAvailableSpace']) == int(fskb))
            fsgb=int(int(ins_result['available-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(ls_result['glue1.3']['GlueSAFreeOnlineSize']) == int(fsgb))

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_glue_used_space(self):
        self.lfn.put_name('WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB')
        self.lfn.put_description('Wrong calculation of SA_USED_SPACE')
        if self.uid.has_key('test_glue_used_space'):
            self.lfn.put_uuid(self.uid['test_glue_used_space'])
        else:
            print 'ADD UID for test_glue_used_space'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/150')
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            self.filter, self.attributes, self.tsets['bdii']['basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        for x in ls_result['glue1.3']['GlueSALocalID']:
            ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                "(&(objectclass=GlueSA)(GlueSALocalID="+x+"))",
                ['GlueSAUsedOnlineSize', 'GlueSAStateUsedSpace'],
                self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()
            self.assert_(ls_result['status'] == 'PASS')

            info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                self.tsets['general']['info_port'],
                x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info_system.get_command())
            ins_result = info_system.get_output()
            uskb=int(int(ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/1000
            self.assert_(int(ls_result['glue1.3']['GlueSAStateUsedSpace']) == int(uskb))
            usgb=int(int(ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(ls_result['glue1.3']['GlueSAUsedOnlineSize']) == int(usgb))

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_size(self):
        self.lfn.put_name('GET_SIZE INCORRECTLY HANDLES THE INFO')
        self.lfn.put_description('Wrong calculation of SA_USED_SPACE')
        if self.uid.has_key('test_size'):
            self.lfn.put_uuid(self.uid['test_size'])
        else:
            print 'ADD UID for test_size'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/146')
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            self.filter, self.attributes, self.tsets['bdii']['basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        for x in ls_result['glue1.3']['GlueSALocalID']:
            ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                "(&(objectclass=GlueSA)(GlueSALocalID="+x+"))",
                ['GlueSATotalOnlineSize', 'GlueSAUsedOnlineSize',
                'GlueSAFreeOnlineSize', 'GlueSAReservedOnlineSize',
                'GlueSATotalNearlineSize'],
                self.tsets['bdii']['basedn'])
            self.lfn.put_cmd('')
            ls_result = ldap_search.get_output()
            self.assert_(ls_result['status'] == 'PASS')

            info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                self.tsets['general']['info_port'],
                x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info_system.get_command())

            ins_result = info_system.get_output()
            usgb=int(int(ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(ls_result['glue1.3']['GlueSAUsedOnlineSize']) == int(usgb))
            tsgb=int(int(ins_result['total-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(ls_result['glue1.3']['GlueSATotalOnlineSize']) == int(tsgb))
            fsgb=int(int(ins_result['free-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(ls_result['glue1.3']['GlueSAFreeOnlineSize']) == int(fsgb))
            rsgb=int(int(ins_result['reserved-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(ls_result['glue1.3']['GlueSAReservedOnlineSize']) >= int(rsgb))

            self.assert_(int(ls_result['glue1.3']['GlueSATotalNearlineSize']) >= 0)

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_info_service_failure(self):
        name = '''REST INFO SERVICE FAILURE'''
        self.lfn.put_name(name)
        des = '''Rest info service fails when non-mandatory parameters are
 missing'''
        self.lfn.put_description(des)
        if self.uid.has_key('test_info_service_failure'):
            self.lfn.put_uuid(self.uid['test_info_service_failure'])
        else:
            print 'ADD UID for test_info_service_failure'
            self.lfn.put_uuid(utils.get_uuid())
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/153')
        self.lfn.put_output()

        ldap_search = ls.LdapSearch(self.tsets['bdii']['endpoint'],
            self.filter, self.attributes, self.tsets['bdii']['basedn'])
        self.lfn.put_cmd('')
        ls_result = ldap_search.get_output()
        self.assert_(ls_result['status'] == 'PASS')

        x=ls_result['glue1.3']['GlueSALocalID'][0]
        info1_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
             self.tsets['general']['info_port'],
             x.split(':')[0].upper().replace('.','').replace('-',''))
        self.lfn.put_cmd(info1_system.get_command())
        ins1_result = info1_system.get_output()
        self.assert_(ins1_result['status'] == 'PASS')

        update_attrs={}
        update_attrs['used'] = '1024'
        update_attrs['unavailable'] = '1024'

        info2_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
             self.tsets['general']['info_port'],
             x.split(':')[0].upper().replace('.','').replace('-',''),
             attrs=update_attrs)
        self.lfn.put_cmd(info2_system.get_command(in_write=True))
        ins2_result = info2_system.get_output(in_write=True)
        self.assert_(ins2_result['status'] == 'PASS')

        info3_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
             self.tsets['general']['info_port'],
             x.split(':')[0].upper().replace('.','').replace('-',''))
        self.lfn.put_cmd(info3_system.get_command())
        ins3_result = info3_system.get_output()
        self.assert_(ins3_result['status'] == 'PASS')

        self.assert_(int(ins3_result['used-space']) == int(update_attrs['used']))
        new_busy = int(ins1_result['busy-space']) + int(ins3_result['used-space']) - int(ins1_result['used-space'])
        self.assert_(int(ins3_result['busy-space']) == new_busy)
        new_free = int(ins1_result['total-space']) - int(ins3_result['used-space'])
        self.assert_(int(ins3_result['free-space']) == new_free)
        new_available = int(ins1_result['total-space']) - int(ins3_result['used-space'])
        self.assert_(int(ins3_result['available-space']) == new_available)
        self.assert_(int(ins3_result['total-space']) == int(ins1_result['total-space']))
        self.assert_(int(ins3_result['reserved-space']) == int(ins1_result['reserved-space']))

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
