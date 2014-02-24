%global proton_datadir %{_datadir}/proton-%{version}

Name:           qpid-proton
Version:        0.6
Release:        2%{?dist}
Summary:        A high performance, lightweight messaging library

License:        ASL 2.0
URL:            http://qpid.apache.org/proton/

Source0:        http://www.apache.org/dist/qpid/proton/%{version}/%{name}-%{version}.tar.gz
Patch1: 01-PROTON-445-Dynamic-languages-honor-CMAKE_INSTALL_PRE.patch

%if (0%{?fedora} || 0%{?rhel} == 7)
BuildRequires:  cmake >= 2.6
%global cmake_exe %{cmake}
%endif

%if 0%{?rhel} == 6
BuildRequires: cmake28
%global cmake_exe %{cmake28}
%endif

BuildRequires:  swig
BuildRequires:  pkgconfig
BuildRequires:  doxygen
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  epydoc



%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

# === qpid-proton-c

%package c
Summary:   C libraries for Qpid Proton
Obsoletes: qpid-proton < %{version}-%{release}
Provides:  qpid-proton = %{version}-%{release}


%description c
%{summary}.


%files c
%defattr(-,root,root,-)
%dir %{proton_datadir}
%doc %{proton_datadir}/LICENSE
%doc %{proton_datadir}/README
%doc %{proton_datadir}/TODO
%{_mandir}/man1/*
%{_bindir}/proton
%{_bindir}/proton-dump
%{_libdir}/libqpid-proton.so.*


%post c -p /sbin/ldconfig


%postun c -p /sbin/ldconfig

# === qpid-proton-c-devel

%package c-devel
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton
Obsoletes: qpid-proton-devel < %{version}-%{release}
Provides:  qpid-proton-devel = %{version}-%{release}


%description c-devel
%{summary}.


%files c-devel
%defattr(-,root,root,-)
%{_includedir}/proton
%{_libdir}/libqpid-proton.so
%{_libdir}/pkgconfig/libqpid-proton.pc
%{_datadir}/proton/examples

# === qpid-proton-c-devel-doc

%package c-devel-doc
Summary:   Documentation for the C development libraries for Qpid Proton
BuildArch: noarch

%description c-devel-doc
%{summary}.

%files c-devel-doc
%defattr(-,root,root,-)
%doc %{proton_datadir}/docs/api-c

# === python-qpid-proton

%package -n python-qpid-proton
Summary:  Python language bindings for the Qpid Proton messaging framework

Requires: qpid-proton-c%{?_isa} = %{version}-%{release}
Requires: python


%description -n python-qpid-proton
%{summary}.


%files -n python-qpid-proton
%defattr(-,root,root,-)
%{python_sitearch}/_cproton.so
%{python_sitearch}/cproton.*
%{python_sitearch}/proton.*

# === python-qpid-proton-doc



%package -n python-qpid-proton-doc
Summary:   Documentation for the Python language bindings for Qpid Proton
BuildArch: noarch


%description -n python-qpid-proton-doc
%{summary}.


%files -n python-qpid-proton-doc
%defattr(-,root,root,-)
%doc %{proton_datadir}/docs/api-py

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1


%build

%cmake_exe \
    -DPROTON_DISABLE_RPATH=true \
    -DPYTHON_ARCHLIB_DIR=%{python_sitearch} \
    .
make all docs %{?_smp_mflags}


%install
%make_install

chmod +x %{buildroot}%{python_sitearch}/_cproton.so

# clean up files that are not shipped
rm -rf %{buildroot}%{_exec_prefix}/bindings
rm -rf %{buildroot}%{_libdir}/java
rm -rf %{buildroot}%{_libdir}/libproton-jni.so
rm -rf %{buildroot}%{_datarootdir}/java
rm -rf %{buildroot}%{_libdir}/proton.cmake

%changelog
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
