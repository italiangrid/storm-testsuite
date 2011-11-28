__author__ = 'Elisabetta Ronchieri'

import datetime
import time
import os 
import unittest
from tstorm.utils import config
from tstorm.utils import ldapsearch as ls 
from tstorm.utils import infosystem as ins

class LdapTest(unittest.TestCase):
    def __init__(self, testname, tfn, lfn, basedn='mds-vo-name=resource,o=grid', filter="'objectClass=GlueService'", attributes='GlueServiceType GlueServiceName'):
        super(LdapTest, self).__init__(testname)
        self.tsets = config.TestSettings(tfn).get_test_sets()
        self.basedn = basedn
        self.filter = filter
        self.attributes = attributes
        self.lfn=lfn

    def test_glue_service(self):
        name = '''STORM BUG: GLUESERVICENAME AND GLUESERVIVETYPE CONTAIN WRONG
VALUES'''
        self.lfn.put_name(name)
        des = '''Yaim-Storm for GLUE2 configuration called a worng script
setting wrong values in the GlueServiceName and GlueServiceType attributes of
the GLUE1.3 schema.'''
        self.lfn.put_description(des)
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/143')
        self.lfn.put_output()

        lds = ls.LdapSearch(self.tsets['bdii']['endpoint'], self.attributes,
              self.basedn, self.filter)
        self.lfn.put_cmd(lds.get_command())
        self.ls_result = lds.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        self.assert_('emi.storm' not in self.ls_result['GlueServiceType'])

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_glue_storage_share_capacity(self):
        self.lfn.put_name('GLUE2 GLUE2STORAGESHARECAPACITY* SIZES ALWAYS ZERO')
        self.lfn.put_description('Glue2 GLUE2StorageShareCapacity* sizes always 0.')
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/147')
        self.lfn.put_output()

        lds = ls.LdapSearch(self.tsets['bdii']['endpoint'],
              'GLUE2StorageServiceCapacityFreeSize GLUE2StorageServiceCapacityUsedSize GLUE2StorageServiceCapacityTotalSize GLUE2StorageServiceCapacityReservedSize',
              'GLUE2GroupID=resource,o=glue',
              "'(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=online))'")
        self.lfn.put_cmd(lds.get_command())
        self.ls_result = lds.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')
        self.assert_(int(self.ls_result['GLUE2StorageServiceCapacityTotalSize']) != 0)

        lds = ls.LdapSearch(self.tsets['bdii']['endpoint'],
              'GLUE2StorageServiceCapacityFreeSize GLUE2StorageServiceCapacityUsedSize GLUE2StorageServiceCapacityTotalSize GLUE2StorageServiceCapacityReservedSize',
              'GLUE2GroupID=resource,o=glue',
              "'(&(objectclass=GLUE2StorageServiceCapacity)(GLUE2StorageServiceCapacityType=nearline))'")
        self.lfn.put_cmd(lds.get_command())
        self.ls_result = lds.get_output()
        if self.ls_result['status'] == 'PASS':
     	    self.assert_(self.ls_result['status'] == 'PASS')
            self.assert_(int(self.ls_result['GLUE2StorageServiceCapacityTotalSize']) >= 0)
        else:
            self.assert_(self.ls_result['status'] == 'FAILURE')

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_glue_available_space_info_service(self):
        self.lfn.put_name('INFO SERVICE ALWAYS RETURNS A ZERO AVAILABLE SPACE')
        self.lfn.put_description('Info Service always returns a zero available space')
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/147')
        self.lfn.put_output()

        lds = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GlueSALocalID',
              self.basedn, "'(objectclass=GlueSA)'")
        self.lfn.put_cmd(lds.get_command())
        self.ls_result = lds.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')

        for x in self.ls_result['GlueSALocalID']:
            info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                          self.tsets['general']['info_port'],
                          x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info_system.get_command())
            self.ins_result = info_system.get_output()
            self.assert_(int(self.ins_result['available-space']) > 0)

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_glue_available_space(self):
        self.lfn.put_name('WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB')
        self.lfn.put_description('Wrong calculation of SA_AVAILABLE_SPACE')
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/150')
        self.lfn.put_output()

        lds = ls.LdapSearch(self.tsets['bdii']['endpoint'], 'GlueSALocalID',
              self.basedn, "'(objectclass=GlueSA)'")
        self.lfn.put_cmd(lds.get_command())

        self.ls_result = lds.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')

        for x in self.ls_result['GlueSALocalID']:
            lds = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                  'GlueSAFreeOnlineSize GlueSAStateAvailableSpace',
                  self.basedn,
                  "'(&(objectclass=GlueSA)(GlueSALocalID="+x+"))'")
            self.lfn.put_cmd(lds.get_command())
            self.ls_result = lds.get_output()
            self.assert_(self.ls_result['status'] == 'PASS')

            info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                          self.tsets['general']['info_port'],
                          x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info_system.get_command())

            self.ins_result = info_system.get_output()
            fskb=int(int(self.ins_result['available-space'])*1000*1000*1000/(1024*1024*1024))/1000
            self.assert_(int(self.ls_result['GlueSAStateAvailableSpace']) == int(fskb))
            fsgb=int(int(self.ins_result['available-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(self.ls_result['GlueSAFreeOnlineSize']) == int(fsgb))

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_glue_used_space(self):
        self.lfn.put_name('WRONG CALCULATION OF SA_AVAILABLE_SIZE_KB AND SA_USED_SIZE_KB')
        self.lfn.put_description('Wrong calculation of SA_USED_SPACE')
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/150')
        self.lfn.put_output()

        lds = ls.LdapSearch(self.tsets['bdii']['endpoint'],
              'GlueSALocalID', self.basedn, "'(objectclass=GlueSA)'")
        self.lfn.put_cmd(lds.get_command())

        self.ls_result = lds.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')

        for x in self.ls_result['GlueSALocalID']:
            lds = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                  'GlueSAUsedOnlineSize GlueSAStateUsedSpace', self.basedn,
                  "'(&(objectclass=GlueSA)(GlueSALocalID="+x+"))'")
            self.lfn.put_cmd(lds.get_command())
            self.ls_result = lds.get_output()
            self.assert_(self.ls_result['status'] == 'PASS')

            info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                          self.tsets['general']['info_port'],
                          x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info_system.get_command())
            self.ins_result = info_system.get_output()
            uskb=int(int(self.ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/1000
            self.assert_(int(self.ls_result['GlueSAStateUsedSpace']) == int(uskb))
            usgb=int(int(self.ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(self.ls_result['GlueSAUsedOnlineSize']) == int(usgb))

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()

    def test_size(self):
        self.lfn.put_name('GET_SIZE INCORRECTLY HANDLES THE INFO')
        self.lfn.put_description('Wrong calculation of SA_USED_SPACE')
        self.lfn.put_ruid('https://storm.cnaf.infn.it:8443/redmine/issues/146')
        self.lfn.put_output()

        lds = ls.LdapSearch(self.tsets['bdii']['endpoint'],
              'GlueSALocalID', self.basedn, "'(objectclass=GlueSA)'")
        self.lfn.put_cmd(lds.get_command())
        self.ls_result = lds.get_output()
        self.assert_(self.ls_result['status'] == 'PASS')

        for x in self.ls_result['GlueSALocalID']:
            lds = ls.LdapSearch(self.tsets['bdii']['endpoint'],
                  'GlueSATotalOnlineSize GlueSAUsedOnlineSize GlueSAFreeOnlineSize GlueSAReservedOnlineSize GlueSATotalNearlineSize',
                  self.basedn,
                  "'(&(objectclass=GlueSA)(GlueSALocalID="+x+"))'")
            self.lfn.put_cmd(lds.get_command())

            self.ls_result = lds.get_output()
            self.assert_(self.ls_result['status'] == 'PASS')

            info_system = ins.InfoSystem(self.tsets['general']['backend_hostname'],
                          self.tsets['general']['info_port'],
                          x.split(':')[0].upper().replace('.','').replace('-',''))
            self.lfn.put_cmd(info_system.get_command())

            self.ins_result = info_system.get_output()
            usgb=int(int(self.ins_result['used-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(self.ls_result['GlueSAUsedOnlineSize']) == int(usgb))
            tsgb=int(int(self.ins_result['total-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(self.ls_result['GlueSATotalOnlineSize']) == int(tsgb))
            fsgb=int(int(self.ins_result['free-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(self.ls_result['GlueSAFreeOnlineSize']) == int(fsgb))
            rsgb=int(int(self.ins_result['reserved-space'])*1000*1000*1000/(1024*1024*1024))/(1000*1000*1000)
            self.assert_(int(self.ls_result['GlueSAReservedOnlineSize']) >= int(rsgb))

            self.assert_(int(self.ls_result['GlueSATotalNearlineSize']) >= 0)

        self.lfn.put_result('PASSED')
        self.lfn.flush_file()
