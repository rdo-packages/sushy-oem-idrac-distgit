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
%global pname sushy_oem_idrac

%global common_desc \
Sushy OEM iDRAC is a Python extension module for the Sushy library \
to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org).

Name: python-%{sname}
Version: XXX
Release: XXX
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers
License: ASL 2.0
URL: https://opendev.org/x/%{sname}

Source0: https://files.pythonhosted.org/packages/source/s/%{sname}/%{sname}-%{upstream_version}.tar.gz

BuildArch: noarch

%description
%{common_desc}

%package -n python%{pyver}-%{sname}
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers
%{?python_provide:%python_provide python%{pyver}-%{sname}}

BuildRequires: git
BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-pbr
BuildRequires: python%{pyver}-setuptools
# For running unit tests during check phase
BuildRequires: python%{pyver}-dateutil
BuildRequires: python%{pyver}-six
BuildRequires: python%{pyver}-stestr
BuildRequires: python%{pyver}-sushy

Requires: python%{pyver}-pbr >= 2.0.0
Requires: python%{pyver}-six >= 1.10.0
Requires: python%{pyver}-dateutil >= 2.7.0
Requires: python%{pyver}-sushy >= 2.0.0


%description -n python%{pyver}-%{sname}
%{common_desc}

%package -n python%{pyver}-%{sname}-tests
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers - tests
Requires: python%{pyver}-%{sname} = %{version}-%{release}

BuildRequires: python%{pyver}-mock
BuildRequires: python%{pyver}-oslotest
BuildRequires: python%{pyver}-testtools

Requires: python%{pyver}-mock
Requires: python%{pyver}-oslotest
Requires: python%{pyver}-testtools

%description -n python%{pyver}-%{sname}-tests
%{common_desc}

This package contains unit tests.

%prep
%autosetup -n %{sname}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{pyver_build}

%check
stestr-%{pyver} run --slowest

%install
%{pyver_install}

%files -n python%{pyver}-%{sname}
%license LICENSE
%{pyver_sitelib}/%{pname}
%{pyver_sitelib}/%{pname}-*.egg-info
%exclude %{pyver_sitelib}/%{pname}/tests

%files -n python%{pyver}-%{sname}-tests
%license LICENSE
%{pyver_sitelib}/%{pname}/tests

%changelog
# REMOVEME: error caused by commit https://opendev.org/x/sushy-oem-idrac71050eaca6e2daaeca318db40e9c6f0b3dff67ba
