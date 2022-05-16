include ntp
include epel
include umd4
include testca
include sdds_users

include voms::dteam
include voms::testvo
include voms::testvo2

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
  'voms-clients',
  'voms-clients-java',
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

Class['ntp']
-> Class['epel']
-> Class['umd4']
-> Class['python']
-> Class['java']
-> Class['sdds_users']
-> Class['voms::dteam']
-> Class['voms::testvo']
-> Class['voms::testvo2']
-> Class['testca']
-> Class['storm::repo']
-> Yumrepo['voms-0621-01']
-> Package[$packages]
-> Package['robotframework']
-> User['tester']
