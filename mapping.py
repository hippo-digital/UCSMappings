# -*- coding: utf-8 -*-
#
# Univention AD Connector
#  this file defines the mapping beetween AD and UCS
#
# Copyright 2004-2016 Univention GmbH
#
# http://www.univention.de/
#
# All rights reserved.
#
# The source code of this program is made available
# under the terms of the GNU Affero General Public License version 3
# (GNU AGPL V3) as published by the Free Software Foundation.
#
# Binary versions of this program provided by Univention to you as
# well as other copyrighted, protected or trademarked materials like
# Logos, graphics, fonts, specific documentations and configurations,
# cryptographic keys etc. are subject to a license agreement between
# you and Univention and not subject to the GNU AGPL V3.
#
# In the case you use this program under the terms of the GNU AGPL V3,
# the program is provided in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License with the Debian GNU/Linux or Univention distribution in file
# /usr/share/common-licenses/AGPL-3; if not, see
# <http://www.gnu.org/licenses/>.

import univention.connector.ad
import univention.connector.ad.mapping
import univention.connector.ad.password

global_ignore_subtree=['cn=univention,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=policies,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=shares,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=printers,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=networks,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=kerberos,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=dhcp,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=dns,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=mail,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=samba,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=nagios,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=System,', 'ou=Grp Policy Users,', 'cn=Builtin,', 'cn=ForeignSecurityPrincipals,', 'ou=Domain Controllers,', 'cn=Program Data,', 'cn=Configuration,', 'cn=opsi,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk', 'cn=Microsoft Exchange System Objects,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','cn=CCN Apps,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Cisco,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','cn=Computers,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=CRM,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','cn=Deleted Objects,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=DFS Structure,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Disabled Computer Accounts,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Domain Controllers,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=EMC Celerra,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','CN=ForeignSecurityPrincipals,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=GP Test,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Inactive,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','CN=Infrastructure,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=IPT Static Phone Contacts,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','CN=LostAndFound,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','CN=Managed Service Accounts,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','CN=NTDS Quotas,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','CN=OpsMgrLatencyMonitors,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','CN=Program Data,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Service Accounts,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Sharepoint,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Single Sign On,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Suppliers,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','CN=System,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=UCCX_Users,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Websense,DC=sdhc,DC=xsdhis,DC=nhs','OU=GP Users,OU=Users,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Suspended Users,OU=Users,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Unmanaged Users,OU=Users,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Servers,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Suppliers,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','OU=Service Accounts,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Computers,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Groups,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=joiners,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=leavers,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=MFD,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Servers,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Testing,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Tombstoned,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk','ou=Users,OU=SDHIS,DC=sdhc,DC=xsdhis,DC=nhs,DC=uk']


ad_mapping = {
	'user': univention.connector.property (
			ucs_default_dn='cn=users,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk',
			con_default_dn='cn=users,',

			ucs_module='users/user',

			# read, write, sync, none
			sync_mode='sync',

			scope='sub',

			con_search_filter='(&(objectClass=user)(!objectClass=computer))',
			match_filter='(|(&(objectClass=posixAccount)(objectClass=sambaSamAccount))(objectClass=user))',
			ignore_filter='(|(userAccountControl=2080)(uid=Administrator)(CN=Administrator)(uid=krbtgt)(CN=krbtgt)(uid=root)(CN=root)(uid=pcpatch)(CN=pcpatch))',


			ignore_subtree = global_ignore_subtree,
			
			con_create_objectclass=['top', 'user', 'person', 'organizationalPerson'],

			dn_mapping_function=[ univention.connector.ad.user_dn_mapping ],

			# from UCS Modul
			attributes= {
					'samAccountName': univention.connector.attribute (
							ucs_attribute='username',
							ldap_attribute='uid',
							con_attribute='sAMAccountName',
							required=1,
							compare_function=univention.connector.compare_lowercase,
						),
					'givenName' : univention.connector.attribute (
							ucs_attribute='firstname',
							ldap_attribute='givenName',
							con_attribute='givenName',
						),
					'sn': univention.connector.attribute (
							ucs_attribute='lastname',
							ldap_attribute='sn',
							con_attribute='sn',
						),
				},

			ucs_create_functions = [ univention.connector.set_ucs_passwd_user,
						 univention.connector.check_ucs_lastname_user,
						 univention.connector.set_primary_group_user
						 ],

			post_con_modify_functions=[ univention.connector.ad.set_userPrincipalName_from_ucr,
						    univention.connector.ad.password.password_sync_ucs,

						    univention.connector.ad.primary_group_sync_from_ucs,
						    univention.connector.ad.object_memberships_sync_from_ucs,
						    univention.connector.ad.disable_user_from_ucs,
						    ],

			post_ucs_modify_functions=[ 						univention.connector.ad.password.password_sync,

						    univention.connector.ad.set_univentionObjectFlag_to_synced,
						    univention.connector.ad.primary_group_sync_to_ucs,
						    univention.connector.ad.object_memberships_sync_to_ucs,
						    univention.connector.ad.disable_user_to_ucs,
						    ],

			post_attributes={
					'organisation': univention.connector.attribute (
							ucs_attribute='organisation',
							ldap_attribute='o',
							con_attribute='company',

						),
						
					'description': univention.connector.attribute (
						ucs_attribute='description',
						ldap_attribute='description',
						con_attribute='description',
					),
					'street': univention.connector.attribute (
							ucs_attribute='street',
							ldap_attribute='street',
							con_attribute='streetAddress',
						),
					'city': univention.connector.attribute (
							ucs_attribute='city',
							ldap_attribute='l',
							con_attribute='l',
						),
					'postcode': univention.connector.attribute (
							ucs_attribute='postcode',
							ldap_attribute='postalCode',
							con_attribute='postalCode',
						),
					'sambaWorkstations': univention.connector.attribute (
							ucs_attribute='sambaUserWorkstations',
							ldap_attribute='sambaUserWorkstations',
							con_attribute='userWorkstations',
						),
					#'sambaLogonHours': univention.connector.attribute (
					#		ucs_attribute='sambaLogonHours',
					#		ldap_attribute='sambaLogonHours',
					#		con_attribute='logonHours',
					#	),
					'profilepath': univention.connector.attribute (
							ucs_attribute='profilepath',
							ldap_attribute='sambaProfilePath',
							con_attribute='profilePath',
						),
					'scriptpath': univention.connector.attribute (
							ucs_attribute='scriptpath',
							ldap_attribute='sambaLogonScript',
							con_attribute='scriptPath',
						),
					'telephoneNumber': univention.connector.attribute (
							ucs_attribute='phone',
							ldap_attribute='telephoneNumber',
							con_attribute='telephoneNumber',
							con_other_attribute='otherTelephone',
						),
					'homePhone': univention.connector.attribute (
							ucs_attribute='homeTelephoneNumber',
							ldap_attribute='homePhone',
							con_attribute='homePhone',
							con_other_attribute='otherHomePhone',
						),
					'mobilePhone': univention.connector.attribute (
							ucs_attribute='mobileTelephoneNumber',
							ldap_attribute='mobile',
							con_attribute='mobile',
							con_other_attribute='otherMobile',
						),
					'pager': univention.connector.attribute (
							ucs_attribute='pagerTelephoneNumber',
							ldap_attribute='pager',
							con_attribute='pager',
							con_other_attribute='otherPager',
						),
					'displayName': univention.connector.attribute (
							ucs_attribute='displayName',
							ldap_attribute='displayName',
							con_attribute='displayName',
						),
			},

		),

	'group': univention.connector.property (
			ucs_default_dn='cn=groups,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk',
			con_default_dn='cn=Users,',

			ucs_module='groups/group',

			sync_mode='sync',

			scope='sub',

			ignore_filter='(|(groupType=-2147483643)(groupType=4)(univentionGroupType=-2147483643)(univentionGroupType=4)(cn=Windows Hosts)(cn=DC Slave Hosts)(cn=DC Backup Hosts)(cn=Authenticated Users)(cn=World Authority)(cn=Everyone)(cn=Null Authority)(cn=Nobody)(cn=Enterprise Domain Controllers)(cn=Computers)(cn=Remote Interactive Logon)(cn=SChannel Authentication)(cn=Digest Authentication)(cn=Terminal Server User)(cn=NTLM Authentication)(cn=Other Organization)(cn=This Organization)(cn=Anonymous Logon)(cn=Network Service)(cn=Creator Group)(cn=Creator Owner)(cn=Local Service)(cn=Owner Rights)(cn=Interactive)(cn=Restricted)(cn=Network)(cn=Service)(cn=Dialup)(cn=System)(cn=Batch)(cn=Proxy)(cn=IUSR)(cn=Self))',


			ignore_subtree = global_ignore_subtree,
			
			con_search_filter='objectClass=group',

			con_create_objectclass=['top', 'group'],

			post_con_modify_functions=[ univention.connector.ad.group_members_sync_from_ucs, univention.connector.ad.object_memberships_sync_from_ucs ],

			post_ucs_modify_functions=[ 
						    univention.connector.ad.set_univentionObjectFlag_to_synced,
							univention.connector.ad.group_members_sync_to_ucs,
							univention.connector.ad.object_memberships_sync_to_ucs
						],

			dn_mapping_function=[ univention.connector.ad.group_dn_mapping ],

			attributes= {
					'cn': univention.connector.attribute (
							ucs_attribute='name',
							ldap_attribute='cn',
							con_attribute='sAMAccountName',
							required=1,
							compare_function=univention.connector.compare_lowercase,
						),
					'groupType': univention.connector.attribute (
							ucs_attribute='adGroupType',
							ldap_attribute='univentionGroupType',
							con_attribute='groupType',
					),

					'description': univention.connector.attribute (
							ucs_attribute='description',
							ldap_attribute='description',
							con_attribute='description',
						),
						
				},

			mapping_table = {
						
				'cn': [( u'Domain Users' , u'Domänen-Benutzer'), ( u'Domain Users' , u'Domain Users'),
						(u'Domain Admins', u'Domänen-Admins'), (u'Domain Admins', u'Domain Admins'),
						(u'Windows Hosts', u'Domänencomputer'), (u'Windows Hosts', u'Windows Hosts'),
						(u'Domain Guests', u'Domänen-Gäste'), (u'Domain Guests', u'Domain Guests')]
					

			},

		),

	'windowscomputer': univention.connector.property (
			ucs_default_dn='cn=computers,dc=sdhc,dc=xsdhis,dc=nhs,dc=uk',
			con_default_dn='cn=computers,',
			ucs_module='computers/windows',
			ucs_module_others=['computers/memberserver', 'computers/ucc', 'computers/linux', 'computers/ubuntu', 'computers/macos' ],

			sync_mode='sync',


			post_ucs_modify_functions=[ 
						    univention.connector.ad.set_univentionObjectFlag_to_synced,
						],

			scope='sub',

			dn_mapping_function=[ univention.connector.ad.windowscomputer_dn_mapping ],

			con_search_filter='(&(objectClass=computer)(userAccountControl:1.2.840.113556.1.4.803:=4096))',

			# ignore_filter='userAccountControl=4096',
			match_filter='(|(&(objectClass=univentionWindows)(!(univentionServerRole=windows_domaincontroller)))(objectClass=computer)(objectClass=univentionMemberServer)(objectClass=univentionUbuntuClient)(objectClass=univentionLinuxClient)(objectClass=univentionMacOSClient)(objectClass=univentionCorporateClient))',

			ignore_subtree = global_ignore_subtree,


			con_create_objectclass=['top', 'computer' ],

			con_create_attributes=[('userAccountControl', ['4096'])],

			attributes= {
					'cn': univention.connector.attribute (
							ucs_attribute='name',
							ldap_attribute='cn',
							con_attribute='cn',
							required=1,
							compare_function=univention.connector.compare_lowercase,
						),
					'samAccountName': univention.connector.attribute (
							ldap_attribute='uid',
							con_attribute='sAMAccountName',
							compare_function=univention.connector.compare_lowercase,
						),
					'description': univention.connector.attribute (
							ucs_attribute='description',
							ldap_attribute='description',
							con_attribute='description'
						),
					'operatingSystem': univention.connector.attribute (
							ucs_attribute='operatingSystem',
							ldap_attribute='univentionOperatingSystem',
							con_attribute='operatingSystem'
						),
					'operatingSystemVersion': univention.connector.attribute (
							ucs_attribute='operatingSystemVersion',
							ldap_attribute='univentionOperatingSystemVersion',
							con_attribute='operatingSystemVersion'
						),
				},

		),
	'container': univention.connector.property (
			ucs_module='container/cn',

			sync_mode='sync',


			scope='sub',

			con_search_filter='(|(objectClass=container)(objectClass=builtinDomain))', # builtinDomain is cn=builtin (with group cn=Administrators)

			ignore_filter='(|(cn=mail)(cn=kerberos))',


			ignore_subtree = global_ignore_subtree,
			
			post_ucs_modify_functions=[ 
						    univention.connector.ad.set_univentionObjectFlag_to_synced,
						],

			con_create_objectclass=['top', 'container' ],

			attributes= {
					'cn': univention.connector.attribute (
							ucs_attribute='name',
							ldap_attribute='cn',
							con_attribute='cn',
							required=1,
							compare_function=univention.connector.compare_lowercase,
						),
					'description': univention.connector.attribute (
							ucs_attribute='description',
							ldap_attribute='description',
							con_attribute='description'
						),
				},

		),

	'ou': univention.connector.property (
			ucs_module='container/ou',

			sync_mode='sync',


			scope='sub',

			con_search_filter='objectClass=organizationalUnit',



			ignore_subtree = global_ignore_subtree,

			post_ucs_modify_functions=[ 
						    univention.connector.ad.set_univentionObjectFlag_to_synced,
						],

			con_create_objectclass=[ 'top', 'organizationalUnit' ],

			attributes= {
					'ou': univention.connector.attribute (
							ucs_attribute='name',
							ldap_attribute='ou',
							con_attribute='ou',
							required=1,
							compare_function=univention.connector.compare_lowercase,
						),
					'description': univention.connector.attribute (
							ucs_attribute='description',
							ldap_attribute='description',
							con_attribute='description'
						),
				},
		),
}



