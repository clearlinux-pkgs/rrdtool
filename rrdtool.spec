#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rrdtool
Version  : 1.7.1
Release  : 2
URL      : https://oss.oetiker.ch/rrdtool/pub/rrdtool-1.7.1.tar.gz
Source0  : https://oss.oetiker.ch/rrdtool/pub/rrdtool-1.7.1.tar.gz
Summary  : Round Robin Database Tool to store and display time-series data
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: rrdtool-bin = %{version}-%{release}
Requires: rrdtool-data = %{version}-%{release}
Requires: rrdtool-lib = %{version}-%{release}
Requires: rrdtool-license = %{version}-%{release}
Requires: rrdtool-locales = %{version}-%{release}
Requires: rrdtool-man = %{version}-%{release}
Requires: rrdtool-services = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : gettext-bin
BuildRequires : groff
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxml2-dev
BuildRequires : lua-dev
BuildRequires : m4
BuildRequires : pcre-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(systemd)
BuildRequires : python3-dev
BuildRequires : ruby
BuildRequires : systemd-dev
Patch1: 0001-Proper-path-for-rrdcached-service-files.patch

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

%package bin
Summary: bin components for the rrdtool package.
Group: Binaries
Requires: rrdtool-data = %{version}-%{release}
Requires: rrdtool-license = %{version}-%{release}
Requires: rrdtool-man = %{version}-%{release}
Requires: rrdtool-services = %{version}-%{release}

%description bin
bin components for the rrdtool package.


%package data
Summary: data components for the rrdtool package.
Group: Data

%description data
data components for the rrdtool package.


%package dev
Summary: dev components for the rrdtool package.
Group: Development
Requires: rrdtool-lib = %{version}-%{release}
Requires: rrdtool-bin = %{version}-%{release}
Requires: rrdtool-data = %{version}-%{release}
Provides: rrdtool-devel = %{version}-%{release}

%description dev
dev components for the rrdtool package.


%package doc
Summary: doc components for the rrdtool package.
Group: Documentation
Requires: rrdtool-man = %{version}-%{release}

%description doc
doc components for the rrdtool package.


%package lib
Summary: lib components for the rrdtool package.
Group: Libraries
Requires: rrdtool-data = %{version}-%{release}
Requires: rrdtool-license = %{version}-%{release}

%description lib
lib components for the rrdtool package.


%package license
Summary: license components for the rrdtool package.
Group: Default

%description license
license components for the rrdtool package.


%package locales
Summary: locales components for the rrdtool package.
Group: Default

%description locales
locales components for the rrdtool package.


%package man
Summary: man components for the rrdtool package.
Group: Default

%description man
man components for the rrdtool package.


%package services
Summary: services components for the rrdtool package.
Group: Systemd services

%description services
services components for the rrdtool package.


%prep
%setup -q -n rrdtool-1.7.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551203119
export LDFLAGS="${LDFLAGS} -fno-lto"
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1551203119
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rrdtool
cp LICENSE %{buildroot}/usr/share/package-licenses/rrdtool/LICENSE
cp bindings/python/COPYING %{buildroot}/usr/share/package-licenses/rrdtool/bindings_python_COPYING
%make_install
%find_lang rrdtool

%files
%defattr(-,root,root,-)
/usr/lib/perl/5.28.1/RRDp.pm
/usr/lib/perl/5.28.1/x86_64-linux-thread-multi/RRDs.pm
/usr/lib/perl/5.28.1/x86_64-linux-thread-multi/auto/RRDp/.packlist
/usr/lib/perl/5.28.1/x86_64-linux-thread-multi/auto/RRDs/.packlist
/usr/lib/perl/5.28.1/x86_64-linux-thread-multi/perllocal.pod

%files bin
%defattr(-,root,root,-)
/usr/bin/rrdcached
/usr/bin/rrdcgi
/usr/bin/rrdcreate
/usr/bin/rrdinfo
/usr/bin/rrdtool
/usr/bin/rrdupdate

%files data
%defattr(-,root,root,-)
/usr/share/rrdtool/examples/4charts.pl
/usr/share/rrdtool/examples/bigtops.pl
/usr/share/rrdtool/examples/cgi-demo.cgi
/usr/share/rrdtool/examples/minmax.pl
/usr/share/rrdtool/examples/perftest.pl
/usr/share/rrdtool/examples/piped-demo.pl
/usr/share/rrdtool/examples/rrdcached/RRDCached.pm
/usr/share/rrdtool/examples/rrdcached/rrdcached-size.pl
/usr/share/rrdtool/examples/shared-demo.pl
/usr/share/rrdtool/examples/stripes.pl
/usr/share/rrdtool/examples/stripes.py

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/librrd.so
/usr/lib64/pkgconfig/librrd.pc
/usr/share/man/man3/RRDp.3
/usr/share/man/man3/RRDs.3
/usr/share/man/man3/librrd.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/rrdtool/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl/5.28.1/x86_64-linux-thread-multi/auto/RRDs/RRDs.so
/usr/lib64/librrd.so.8
/usr/lib64/librrd.so.8.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rrdtool/LICENSE
/usr/share/package-licenses/rrdtool/bindings_python_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bin_dec_hex.1
/usr/share/man/man1/cdeftutorial.1
/usr/share/man/man1/rpntutorial.1
/usr/share/man/man1/rrd-beginners.1
/usr/share/man/man1/rrd_pdpcalc.1
/usr/share/man/man1/rrdbuild.1
/usr/share/man/man1/rrdcached.1
/usr/share/man/man1/rrdcgi.1
/usr/share/man/man1/rrdcreate.1
/usr/share/man/man1/rrddump.1
/usr/share/man/man1/rrdfetch.1
/usr/share/man/man1/rrdfirst.1
/usr/share/man/man1/rrdflushcached.1
/usr/share/man/man1/rrdgraph.1
/usr/share/man/man1/rrdgraph_data.1
/usr/share/man/man1/rrdgraph_examples.1
/usr/share/man/man1/rrdgraph_graph.1
/usr/share/man/man1/rrdgraph_rpn.1
/usr/share/man/man1/rrdinfo.1
/usr/share/man/man1/rrdlast.1
/usr/share/man/man1/rrdlastupdate.1
/usr/share/man/man1/rrdlist.1
/usr/share/man/man1/rrdresize.1
/usr/share/man/man1/rrdrestore.1
/usr/share/man/man1/rrdthreads.1
/usr/share/man/man1/rrdtool.1
/usr/share/man/man1/rrdtune.1
/usr/share/man/man1/rrdtutorial.1
/usr/share/man/man1/rrdupdate.1
/usr/share/man/man1/rrdxport.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rrdcached.service
/usr/lib/systemd/system/rrdcached.socket

%files locales -f rrdtool.lang
%defattr(-,root,root,-)

