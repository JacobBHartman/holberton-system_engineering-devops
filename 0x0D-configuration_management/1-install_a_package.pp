# this package make sure puppet-lint is correct version
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
