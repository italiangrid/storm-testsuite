__author__ = 'Elisabetta Ronchieri'

import commands
import os
import ldap
from tstorm.utils import utils

class LdapSearch:
    def __init__(self, endpoint, filter, attributes, basedn):
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
                'GLUE2EndpointInterfaceExtension':[],
                'GLUE2EndpointIssuerCA':[],
                'GLUE2EndpointCapability':[],
                'GLUE2EndpointTrustedCA':[],
                'GLUE2EndpointSupportedProfile':[],
                'GLUE2StorageShareAccessMode':[],
                'GLUE2StorageServiceCapacityFreeSize':'',
                'GLUE2StorageServiceCapacityUsedSize':'',
                'GLUE2StorageServiceCapacityTotalSize':'',
                'GLUE2StorageServiceCapacityReservedSize':''
            }
        }

    def run_command(self):
        uri = self.cmd['protocol'] + '://' + self.endpoint + ':' + self.cmd['port']

        ldap_init = ldap.initialize(uri)

        search_scope = ldap.SCOPE_SUBTREE
        result_set = []

        try:
            ldap_result_id = ldap_init.search(self.basedn, search_scope, self.filter, self.attributes)
            #print self.filter, self.attributes  
            while 1:
                result_type, result_data = ldap_init.result(ldap_result_id, 0)
                #print 'data %s' % result_data

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
            self.otpt['status'] = 'PASS'
            for y in a:
                for z in y:
                    for element in z:
                        if type(element) is dict:
                            for attr in element.keys():
                                #print '0 ', attr, element.keys()
                                if attr in self.otpt['glue1.3'].keys():
                                    if attr == 'GlueSALocalID':
                                        #print '1 ', attr
                                        self.otpt['glue1.3'][attr].append(element[attr][0])
                                        #print '1 ', attr, self.otpt['glue1.3'][attr], a
                                    else:
                                        #print '1 ', attr
                                        self.otpt['glue1.3'][attr] = element[attr][0]
                                elif attr in self.otpt['glue2.0'].keys():
                                    if attr in ('GLUE2EndpointCapability', 'GLUE2EndpointInterfaceExtension',
                                        'GLUE2EndpointIssuerCA', 'GLUE2EndpointTrustedCA', 
                                        'GLUE2EndpointSupportedProfile', 'GLUE2StorageShareAccessMode'):
                                        #print element[attr], attr
                                        for x in element[attr]:
                                            self.otpt['glue2.0'][attr].append(x)
                                    else:
                                        self.otpt['glue2.0'][attr] = element[attr][0]
        else:
            for value in self.attributes:
                if value in ('GLUE2EndpointCapability', 'GLUE2EndpointInterfaceExtension',
                    'GLUE2EndpointIssuerCA', 'GLUE2EndpointTrustedCA',
                    'GLUE2EndpointSupportedProfile', 'GLUE2StorageShareAccessMode'):
                    self.otpt['status'] = 'PASS'
                else:
                    self.otpt['status'] = 'FAILURE'

        #print self.otpt

        return self.otpt


