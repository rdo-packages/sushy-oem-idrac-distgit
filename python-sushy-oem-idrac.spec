# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1
%global sname sushy-oem-idrac

%global common_desc \
Sushy OEM iDRAC is a Python extension module for Sushy library to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org)

%global common_desc_tests Tests for Sushy OEM iDRAC

Name: python-%{sname}
Version: XXX
Release: XXX
Summary: Sushy OEM iDRAC is a Python extension module for Sushy library to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org)
License: ASL 2.0
URL: http://launchpad.net/%{sname}/

Source0: http://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz

BuildArch: noarch

%description
%{common_desc}

%package -n python%{pyver}-%{sname}
Summary: Sushy OEM iDRAC is a Python extension module for Sushy library to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org)
%{?python_provide:%python_provide python%{pyver}-%{sname}}

BuildRequires: git
BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-pbr
BuildRequires: python%{pyver}-setuptools
# For running unit tests during check phase
BuildRequires: python%{pyver}-requests
BuildRequires: python%{pyver}-six
BuildRequires: python%{pyver}-dateutil
BuildRequires: python%{pyver}-stevedore

Requires: python%{pyver}-pbr >= 2.0.0
Requires: python%{pyver}-six >= 1.10.0
Requires: python%{pyver}-requests >= 2.14.2
Requires: python%{pyver}-dateutil
Requires: python-sushy


%description -n python%{pyver}-%{sname}
%{common_desc}

%package -n python%{pyver}-%{sname}-tests
Summary: Sushy OEM iDRAC tests
Requires: python%{pyver}-%{sname} = %{version}-%{release}

BuildRequires: python%{pyver}-oslotest
BuildRequires: python%{pyver}-testrepository
BuildRequires: python%{pyver}-testscenarios
BuildRequires: python%{pyver}-testtools

Requires: python%{pyver}-oslotest
Requires: python%{pyver}-testrepository
Requires: python%{pyver}-testscenarios
Requires: python%{pyver}-testtools

%description -n python%{pyver}-%{sname}-tests
%{common_desc_tests}

%prep
%autosetup -n %{sname}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{pyver_build}

%check
%{pyver_bin} setup.py test

%install
%{pyver_install}

%files -n python%{pyver}-%{sname}
%license LICENSE
%{pyver_sitelib}/%{sname}
%{pyver_sitelib}/%{sname}-*.egg-info
%exclude %{pyver_sitelib}/%{sname}/tests

%files -n python%{pyver}-%{sname}-tests
%license LICENSE
%{pyver_sitelib}/%{sname}/tests

%changelog
* Thu Dec  5 2019  Ilya Etingof <etingof@gmail.com> 0.2.0-2
- Initial package.
