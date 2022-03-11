# installs puppet-lint version 2.5.0

package {'Installs package':
  ensure => '2.5.0'
  provider => 'gem',
}
