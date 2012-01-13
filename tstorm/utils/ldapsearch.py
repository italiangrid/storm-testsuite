#!/usr/bin/python

__author__ = 'Elisabetta Ronchieri'

import commands
import os
import ldap
from tstorm.utils import utils

class LdapSearch:
    def __init__(self, endpoint, attributes, basedn='mds-vo-name=resource,o=grid', filter='objectClass=GlueService'):
        self.endpoint = endpoint
        self.basedn = basedn
        self.filter = filter
        self.attributes = attributes
        self.cmd = {
            'protocol': 'ldap',
            'port': '2170'}
        self.otpt = {
            'status':'',
            'glue1.3': {
                'GlueServiceName':'',
                'GlueServiceType':'',
                'GlueSAStateUsedSpace':'',
                'GlueSAUsedOnlineSize':'',
                'GlueSAFreeOnlineSize':'',
                'GlueSAStateAvailableSpace':'',
                'GlueSATotalOnlineSize':'',
                'GlueSAReservedOnlineSize':'',
                'GlueSATotalNearlineSize':'',
                'GlueSALocalID':[]
            },
            'glue2.0': {
                'GLUE2EndpointInterfaceExtension':'',
                'GLUE2EndpointIssuerCA':'',
                'GLUE2EndpointTrustedCA':'',
                'GLUE2StorageShareAccessMode':'',
                'GLUE2StorageServiceCapacityFreeSize':'',
                'GLUE2StorageServiceCapacityUsedSize':'',
                'GLUE2StorageServiceCapacityTotalSize':'',
                'GLUE2StorageServiceCapacityReservedSize':''
            }
        }

    def get_command(self):
        #uri = self.cmd['uri'] + ' ' + self.cmd['protocol'] + '://' + self.endpoint + ':' + self.cmd['port']
        #opt = ' ' + self.cmd['sa'] + ' ' + self.cmd['pres'] + ' ' + uri + ' ' +  self.cmd['basedn'] + ' '
        #a=self.cmd['name'] + opt + self.filter + ' ' + self.attributes
        return 'BaseDN %s; Filter %s; Attrs %s' % (self.basedn , self.filter, self.attributes)

    def run_command(self):
        uri = self.cmd['protocol'] + '://' + self.endpoint + ':' + self.cmd['port']

        ldap_init = ldap.initialize(uri)

        search_scope = ldap.SCOPE_SUBTREE
        result_set = []

        try:
            ldap_result_id = ldap_init.search(self.basedn, search_scope, self.filter, self.attributes)
          
            while 1:
                result_type, result_data = ldap_init.result(ldap_result_id, 0)
                print 'data %s' % result_data

		if (result_data == []):
                    break
		else:
                    ## here you don't have to append to a list
		    ## you could do whatever you want with the individual entry
		    ## The appending to list is just for illustration. 
		    if result_type == ldap.RES_SEARCH_ENTRY:
                        result_set.append(result_data)
        except ldap.LDAPError, e:
	    print e

        return result_set

    def get_output(self):
        a=self.run_command()
        if len(a) > 0 :
            for x in self.otpt:
                if x == 'status':
                    self.otpt['status'] = 'PASS'
                else:
                   for y in a:
                       for z in y:
                           for element in z:
                               if type(element) is dict:
                                   for attr in element.keys():
                                      if attr in self.otpt['glue1.3'].keys():
                                          if attr == 'GlueSALocalID':
                                              self.otpt['glue1.3'][attr].append(element[attr])
                                          else:
                                              self.otpt['glue1.3'][attr] = element[attr][0]
                                      elif attr in self.otpt['glue2.0'].keys():
                                          self.otpt['glue2.0'][attr] = element[attr]
        else:
            self.otpt['status'] = 'FAILURE'

        print self.otpt

        return self.otpt


