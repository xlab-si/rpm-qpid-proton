%global proton_datadir %{_datadir}/proton-%{version}

Name:           qpid-proton
Version:        0.4
Release:        1%{?dist}
Summary:        A high performance, lightweight messaging library

License:        ASL 2.0
URL:            http://qpid.apache.org/proton/
Source0:        http://www.apache.org/dist/qpid/proton/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake28
BuildRequires:  swig
BuildRequires:  pkgconfig
BuildRequires:  doxygen
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  python-devel
BuildRequires:  epydoc


%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.


%package -n qpid-proton-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary:  Development libraries for writing messaging apps with Qpid Proton


%description -n qpid-proton-devel
%{summary}.


%files -n qpid-proton-devel
%defattr(-,root,root,-)
%{_includedir}/proton
%{_libdir}/libqpid-proton.so
%{_libdir}/pkgconfig/libqpid-proton.pc
%{proton_datadir}/docs/api-c


%package -n python-qpid-proton
Summary:  Python language bindings for the Qpid Proton messaging framework

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python



%description -n python-qpid-proton
%{summary}.


%files -n python-qpid-proton
%defattr(-,root,root,-)
%{python_sitearch}/_cproton.so
%{python_sitearch}/cproton.*
%{python_sitearch}/proton.*


%package -n python-qpid-proton-doc
Summary: Documentation for the Python language bindings for Qpid Proton


%description -n python-qpid-proton-doc
%{summary}.


%files -n python-qpid-proton-doc
%defattr(-,root,root,-)
%{proton_datadir}/docs


%prep
%setup -q -n %{name}-%{version}


%build
%cmake28 -DPROTON_DISABLE_RPATH=true .
make all docs %{?_smp_mflags}


%install
%make_install

chmod +x %{buildroot}%{python_sitearch}/_cproton.so

# clean up files that are not shipped
rm -rf %{buildroot}%{_libdir}/php
rm -rf %{buildroot}%{_libdir}/java
rm -rf %{buildroot}%{_libdir}/libproton-jni.so
rm -rf %{buildroot}%{_datarootdir}/php
rm -rf %{buildroot}%{_datarootdir}/java
rm -rf %{buildroot}%{_sysconfdir}/php.d

%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%dir %{proton_datadir}
%doc %{proton_datadir}/LICENSE
%doc %{proton_datadir}/README
%doc %{proton_datadir}/TODO
%{_mandir}/man1/*
%{_bindir}/proton
%{_bindir}/proton-dump
%{_libdir}/libqpid-proton.so.*


%changelog
* Wed Mar 13 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-1
- Rebased on Proton 0.4.
- On EL6 BR pulls in Cmake 2.8 on PPC/PPC64.

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
