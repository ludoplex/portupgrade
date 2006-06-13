#!/usr/bin/env ruby
#
# $Id: test_portsdb.rb 1028 2004-07-20 11:14:02Z knu $
$:.push("..")

require 'test/unit'

require 'pkgdb'
require 'portsdb'

class TestPortsDB < Test::Unit::TestCase
  def test_strip
    pkgdb = PkgDB.instance.setup('/var/db/pkg')
    portsdb = PortsDB.instance.setup(pkgdb.db_dir, '/usr/ports')

    assert_equal('foo/bar1', portsdb.strip('foo/bar1'))
    assert_equal('foo/bar2', portsdb.strip('foo/bar2/'))
    assert_equal('foo/bar3', portsdb.strip('/usr/ports/foo/bar3'))
    assert_equal('foo/bar4', portsdb.strip('/usr/ports/foo/bar4/'))
    assert_equal('foo/bar7', portsdb.strip('/usr/ports/foo//bar7/'))
    assert_equal(nil, portsdb.strip('/usr/ports/foo/../bar8/foo/'))
    assert_equal(nil, portsdb.strip('/usr/ports/foo/./bar9/'))
    assert_equal(nil, portsdb.strip('/usr/ports/foo/bar5/Makefile'))
    assert_equal(nil, portsdb.strip('/usr/ports/foo/bar6/files/'))
    assert_equal(nil, portsdb.strip('/foo'))
    assert_equal(nil, portsdb.strip('/foo/'))
    assert_equal(nil, portsdb.strip('/foo/bar'))
  end
end
