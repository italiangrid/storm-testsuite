include epel
include umd4
include testvos
include testca
include sdds_users

class { 'storm::repo':
  enabled     => ['stable'],
}

$packages = [
  'openldap-clients',
  'globus-gass-copy-progs',
  'gfal2-util',
  'gfal2-all',
  'dcache-srmclient',
  'storm-srm-client',
  'davix',
  'myproxy',
]

package { $packages:
  ensure => 'latest',
}

yumrepo { 'voms-0621-01':
  ensure   => present,
  descr    => 'voms unreleased rpms',
  baseurl  => 'https://ci.cloud.cnaf.infn.it/view/voms/job/pkg.voms/job/v0621.01/lastSuccessfulBuild/artifact/artifacts/stage-area/centos7',
  enabled  => 1,
  protect  => 1,
  priority => 1,
  gpgcheck => 0,
}

package { 'voms-clients':
  ensure => 'installed',
}

class { 'python':
  pip => 'present',
}

package { 'robotframework':
  ensure   => installed,
  require  => Class['python'],
  provider => 'pip',
}
package { 'robotframework-httplibrary':
  ensure   => installed,
  require  => [Class['python'], Package['robotframework']],
  provider => 'pip',
}

class { 'java' :
  package => 'java-1.8.0-openjdk-devel',
}

user { 'tester':
  ensure     => present,
  name       => $title,
  password   => Sensitive('password'),
  managehome => true,
  groups     => ['wheel'],
}

Class['epel']
-> Class['umd4']
-> Class['python']
-> Class['java']
-> Class['sdds_users']
-> Class['testvos']
-> Class['testca']
-> Class['storm::repo']
-> Package[$packages]
-> Package['voms-clients']
-> Package['robotframework']
-> User['tester']
