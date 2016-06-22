%global proton_datadir %{_datadir}/proton-%{version}

%if 0%{?fedora}
%global gem_name qpid_proton
%endif

# per https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Preventing_files.2Fdirectories_from_being_scanned_for_deps_.28pre-scan_filtering.29
%global __provides_exclude_from ^%{proton_datadir}/examples/.*$
%global __requires_exclude_from ^%{proton_datadir}/examples/.*$

#  for older rpm, like el6, https://fedoraproject.org/wiki/EPEL:Packaging_Autoprovides_and_Requires_Filtering#Perl
%{?filter_setup:
%filter_provides_in %{proton_datadir}/examples/
%filter_requires_in %{proton_datadir}/examples/
%filter_setup
}

Name:           qpid-proton
Version:        0.13.0
Release:        1%{?dist}
Group:          System Environment/Libraries
Summary:        A high performance, lightweight messaging library

License:        ASL 2.0
URL:            http://qpid.apache.org/proton/

Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  swig
BuildRequires:  pkgconfig
BuildRequires:  doxygen
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
%if 0%{?fedora} 
BuildRequires:  python2-devel
BuildRequires:  python3-devel
%endif
%if 0%{?rhel}
BuildRequires:  python-devel
%endif
BuildRequires:  epydoc
%if 0%{?fedora}
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
%endif
BuildRequires:  cyrus-sasl-devel

#Patch0:         proton.patch

%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.


%package c
Group:     System Environment/Libraries
Summary:   C libraries for Qpid Proton
Requires:  cyrus-sasl-lib
Obsoletes: qpid-proton

%description c
%{summary}.


%files c
%defattr(-,root,root,-)
%dir %{proton_datadir}
%doc %{proton_datadir}/LICENSE
%doc %{proton_datadir}/README*
%doc %{proton_datadir}/TODO
%{_libdir}/libqpid-proton.so.*

%post c -p /sbin/ldconfig

%postun c -p /sbin/ldconfig

%if 0%{?rhel}
%package   cpp
Group:     System Environment/Libraries
Summary:   C++ libraries for Qpid Proton
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release} 

%description cpp
%{summary}.

%files cpp
%defattr(-,root,root,-)
%dir %{proton_datadir}
%doc %{proton_datadir}/LICENSE
%doc %{proton_datadir}/README*
%doc %{proton_datadir}/TODO
%{_libdir}/libqpid-proton-cpp.so.*

%post cpp -p /sbin/ldconfig

%postun cpp -p /sbin/ldconfig
%endif

%package c-devel
Group:     Development/System
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton
Obsoletes: qpid-proton-devel

%description c-devel
%{summary}.

%files c-devel
%defattr(-,root,root,-)
%{_includedir}/proton
%if 0%{?rhel} 
%exclude %{_includedir}/proton/*.hpp
%endif
%{_libdir}/libqpid-proton.so
%{_libdir}/pkgconfig/libqpid-proton.pc
%{_libdir}/cmake/Proton


%if 0%{?rhel}
%package cpp-devel
Group:     Development/System
Requires:  qpid-proton-cpp%{?_isa} = %{version}-%{release}
Requires:  qpid-proton-c-devel%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton

%description cpp-devel
%{summary}.

%files cpp-devel
%defattr(-,root,root,-)
%{_includedir}/proton/*.hpp
%{_libdir}/pkgconfig/libqpid-proton-cpp.pc
%{_libdir}/libqpid-proton-cpp.so
%{_libdir}/cmake/ProtonCpp
%endif


%package c-devel-docs
Summary:   Documentation for the C development libraries for Qpid Proton
BuildArch: noarch
Obsoletes:  qpid-proton-c-devel-doc
%description c-devel-docs
%{summary}.

%files c-devel-docs
%defattr(-,root,root,-)
%doc %{proton_datadir}/docs/api-c
%doc %{proton_datadir}/examples
%exclude %{proton_datadir}/examples/cpp
%exclude %{proton_datadir}/examples/go
%exclude %{proton_datadir}/examples/java
%exclude %{proton_datadir}/examples/javascript
%exclude %{proton_datadir}/examples/php
%exclude %{proton_datadir}/examples/python
%exclude %{proton_datadir}/examples/ruby
%exclude %{proton_datadir}/examples/perl
%exclude %{proton_datadir}/examples/c/messenger/recv
%exclude %{proton_datadir}/examples/c/messenger/recv-async
%exclude %{proton_datadir}/examples/c/messenger/send
%exclude %{proton_datadir}/examples/c/messenger/send-async
%exclude %{proton_datadir}/examples/c/messenger/CMakeFiles
%exclude %{proton_datadir}/examples/c/messenger/Makefile
%exclude %{proton_datadir}/examples/c/messenger/cmake_install.cmake
%exclude %{proton_datadir}/examples/c/messenger/CTestTestfile.cmake
%exclude %{proton_datadir}/examples/engine/java
%exclude %{proton_datadir}/examples/c/reactor/receiver
%exclude %{proton_datadir}/examples/c/reactor/sender
%exclude %{proton_datadir}/examples/c/reactor/CMakeFiles
%exclude %{proton_datadir}/examples/c/reactor/Makefile
%exclude %{proton_datadir}/examples/c/reactor/cmake_install.cmake
%exclude %{proton_datadir}/examples/c/reactor/CTestTestfile.cmake
%exclude %{proton_datadir}/examples/CMakeFiles
%exclude %{proton_datadir}/examples/cmake_install.cmake
%exclude %{proton_datadir}/examples/CTestTestfile.cmake
%exclude %{proton_datadir}/examples/Makefile
%exclude %{proton_datadir}/examples/c/CMakeFiles
%exclude %{proton_datadir}/examples/c/cmake_install.cmake
%exclude %{proton_datadir}/examples/c/CTestTestfile.cmake
%exclude %{proton_datadir}/examples/c/Makefile

%if 0%{?rhel}
%package   cpp-devel-docs
Summary:   Documentation for the C++ development libraries for Qpid Proton
BuildArch: noarch
Obsoletes:  qpid-proton-cpp-devel-doc

%description cpp-devel-docs
%{summary}.

%files cpp-devel-docs
%defattr(-,root,root,-)
%{proton_datadir}/docs/api-cpp
%doc %{proton_datadir}/examples
%exclude %{proton_datadir}/examples/c
%exclude %{proton_datadir}/examples/go
%exclude %{proton_datadir}/examples/java
%exclude %{proton_datadir}/examples/javascript
%exclude %{proton_datadir}/examples/php
%exclude %{proton_datadir}/examples/python
%exclude %{proton_datadir}/examples/ruby
%exclude %{proton_datadir}/examples/perl
%exclude %{proton_datadir}/examples/engine
%endif


%package -n python-qpid-proton
Group:    System Environment/Libraries
Summary:  Python language bindings for the Qpid Proton messaging framework

Requires: qpid-proton-c%{?_isa} = %{version}-%{release}
Requires: python

%description -n python-qpid-proton
%{summary}.

%files -n python-qpid-proton
%defattr(-,root,root,-)
%{python_sitearch}/_cproton.so
%{python_sitearch}/cproton.*
%{python_sitearch}/proton/*


%if 0%{?fedora}
%package -n python3-qpid-proton
Group:    System Environment/Libraries
Summary:  Python language bindings for the Qpid Proton messaging framework
%{?python_provide:%python_provide python3-qpid-proton}

Requires: qpid-proton-c%{?_isa} = %{version}-%{release}

%description -n python3-qpid-proton
%{summary}.

%files -n python-qpid-proton
%defattr(-,root,root,-)
%{python2_sitearch}/*

%files -n python3-qpid-proton
%defattr(-,root,root,-)
%{python3_sitearch}/*
%endif

%package -n python-qpid-proton-docs
Group:     Documentation
Summary:   Documentation for the Python language bindings for Qpid Proton
BuildArch: noarch
Obsoletes:  python-qpid-proton-doc

%description -n python-qpid-proton-docs
%{summary}.

%files -n python-qpid-proton-docs
%defattr(-,root,root,-)
%doc %{proton_datadir}/docs/api-py
%doc %{proton_datadir}/examples/python


%if 0%{?fedora}
%package -n perl-qpid-proton
Summary: Perl language bindings for Qpid Proton messaging framework

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:  qpid-proton-c = %{version}-%{release}

%description -n perl-qpid-proton
%{summary}.

%files -n perl-qpid-proton
%doc LICENSE TODO README*
%{perl_vendorarch}/*
%endif


%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1

%build

%if 0%{?fedora}
%cmake \
    -DPROTON_DISABLE_RPATH=true \
    -DBUILD_RUBY=OFF \
    -DBUILD_PHP=OFF \
    -DSYSINSTALL_PYTHON=1 \
    -DSYSINSTALL_PERL=1 \
    .
%endif
%if 0%{?rhel}
%cmake -DPROTON_DISABLE_RPATH=true \
       -DCMAKE_EXE_LINKER_FLAGS="-Wl,-z,relro,-z,now" \
       -DCMAKE_SHARED_LINKER_FLAGS="-Wl,-z,relro" \
       -DCMAKE_MODULE_LINKER_FLAGS="-Wl,-z,relro" \
       -DSYSINSTALL_BINDINGS=ON \
       -DBUILD_RUBY=OFF \
       -DBUILD_PERL=OFF \
       .
%endif

make all docs %{?_smp_mflags}
%if 0%{?fedora}
(cd proton-c/bindings/python; %py3_build)
%endif

%install
%make_install
%if 0%{?fedora}
(cd proton-c/bindings/python; %py3_install)
%endif

CPROTON_BUILD=$PWD . ./config.sh

chmod +x %{buildroot}%{python_sitearch}/_cproton.so
find %{buildroot}%{proton_datadir}/examples/ -type f | xargs chmod -x 

# clean up files that are not shipped
rm -rf %{buildroot}%{_exec_prefix}/bindings
rm -rf %{buildroot}%{_libdir}/java
rm -rf %{buildroot}%{_libdir}/libproton-jni.so
rm -rf %{buildroot}%{_datarootdir}/java
rm -rf %{buildroot}%{_libdir}/proton.cmake
%if 0%{?fedora}
rm -rf %{buildroot}%{_libdir}/cmake/ProtonCpp
rm -rf %{buildroot}%{_libdir}/*cpp*
rm -rf %{buildroot}%{_libdir}/pkgconfig/libqpid-proton-cpp.pc
rm -rf %{buildroot}%{proton_datadir}/docs/api-cpp
%endif
%if 0%{?rhel}
rm -rf %{buildroot}%{_libdir}/perl5
rm -rf %{buildroot}%{_libdir}/php
rm -rf %{buildroot}%{_libdir}/ruby
rm -rf %{buildroot}%{_datarootdir}/php
rm -rf %{buildroot}%{_datarootdir}/perl5
rm -rf %{buildroot}%{_datarootdir}/ruby
rm -rf %{buildroot}%{_sysconfdir}/php.d
%endif

%check
%if 0%{?fedora} 
# check perl bindings
pushd proton-c/bindings/perl
make test
popd
%endif

%changelog
* Wed Jun 22 2016 Irina Boverman <iboverma@redhat.com> - 0.13.0-1
- Rebased to 0.13.0
- Changed *doc to *docs, moved examples to *docs

* Wed Mar 23 2016 Irina Boverman <iboverma@redhat.com> - 0.12.1-1
- Rebased to 0.12.1
- Added python3 installation

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  8 2015 Irina Boverman <iboverma@redhat.com> - 0.10-2
- Added dependency on cyrus-sasl-devel and cyrus-sasl-lib
- Added 0001-PROTON-974-Accept-a-single-symbol-in-SASL-mechs-fram.patch
 
* Wed Sep  2 2015 Irina Boverman <iboverma@redhat.com> - 0.10-1
- Rebased to 0.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.9-4
- Perl 5.22 rebuild

* Wed Apr  8 2015 Darryl L. Pierce <dpierce@redhat.com> - 0.9-3
- Added a global excludes macro to fix EL6 issues with example Perl modules.

* Wed Apr  8 2015 Darryl L. Pierce <dpierce@redhat.com> - 0.9-2
- Marked the examples in -c-devel as doc.
- Turned off the executable flag on all files under examples.

* Mon Apr  6 2015 Darryl L. Pierce <dpierce@redhat.com> - 0.9-1
- Rebased on Proton 0.9.
- Removed the proton binary from qpid-proton-c.
- Added the perl-qpid-proton subpackage.

* Tue Nov 18 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.8-1
- Rebased on Proton 0.8.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.7-3
- Removed intra-package comments which cause error messages on package uninstall.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.7-1
- Rebased on Proton 0.7
- Added new CMake modules for Proton to qpid-proton-c-devel.

* Mon Feb 24 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.6-2
- Reorganized the subpackages.
- Merged up branches to get things back into sync.

* Thu Jan 16 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.6-1
- Rebased on Proton 0.6.
- Update spec to delete ruby and perl5 directories if Cmake creates them.
- Removed Java sub-packages - those will be packaged separate in future.

* Fri Sep  6 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.5-2
- Made python-qpid-proton-doc a noarch package.
- Resolves: BZ#1005058

* Wed Aug 28 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.5-1
- Rebased on Proton 0.5.
- Resolves: BZ#1000620

* Mon Aug 26 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-4
- Created the qpid-proton-c-devel-doc subpackage.
- Resolves: BZ#1000615

* Wed Jul 24 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-3
- Provide examples for qpid-proton-c
- Resolves: BZ#975723

* Fri Apr  5 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2.2
- Added Obsoletes and Provides for packages whose names changed.
- Resolves: BZ#948784

* Mon Apr  1 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2.1
- Fixed the dependencies for qpid-proton-devel and python-qpid-proton.

* Thu Mar 28 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2
- Moved all C libraries to the new qpid-proton-c subpackage.

* Tue Feb 26 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-1
- Rebased on Proton 0.4.

* Thu Feb 21 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-4
- Fixes copying nested data.
- PROTON-246, PROTON-230

* Mon Jan 28 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-3
- Fixes build failure on non-x86 platforms.
- Resolves: BZ#901526

* Fri Jan 25 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-2
- Fixes build failure on non-x86 platforms.
- Resolves: BZ#901526

* Wed Jan 16 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-1
- Rebased on Proton 0.3.

* Fri Dec 28 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2.4
- Moved ownership of the docs dir to the docs package.

* Wed Dec 19 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2.3
- Fixed package dependencies, adding the release macro.

* Mon Dec 17 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2.2
- Fixed subpackage dependencies on main package.
- Removed accidental ownership of /usr/include.

* Thu Dec 13 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2.1
- Remove BR for ruby-devel.
- Removed redundant package name from summary.
- Removed debugging artifacts from specfile.
- Moved unversioned library to the -devel package.
- Added dependency on main package to -devel. 
- Fixed directory ownerships.

* Fri Nov 30 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2
- Removed BR on help2man.
- Added patch for generated manpage.

* Mon Nov  5 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-1
- Initial packaging of the Qpid Proton.
