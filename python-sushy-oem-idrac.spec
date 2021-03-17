%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname sushy-oem-idrac
%global pname sushy_oem_idrac

%global common_desc \
Sushy OEM iDRAC is a Python extension module for the Sushy library \
to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org).

Name: python-%{sname}
Version: 0.0.2
Release: 1%{?dist}
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers
License: ASL 2.0
URL: https://opendev.org/x/%{sname}

Source0: https://files.pythonhosted.org/packages/source/s/%{sname}/%{sname}-%{upstream_version}.tar.gz

BuildArch: noarch

%description
%{common_desc}

%package -n python3-%{sname}
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: git
BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools
# For running unit tests during check phase
BuildRequires: python3-dateutil
BuildRequires: python3-six
BuildRequires: python3-stestr
BuildRequires: python3-sushy

Requires: python3-pbr >= 2.0.0
Requires: python3-six >= 1.10.0
Requires: python3-dateutil >= 2.7.0
Requires: python3-sushy >= 2.0.0


%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers - tests
Requires: python3-%{sname} = %{version}-%{release}

BuildRequires: python3-mock
BuildRequires: python3-oslotest
BuildRequires: python3-testtools

Requires: python3-mock
Requires: python3-oslotest
Requires: python3-testtools

%description -n python3-%{sname}-tests
%{common_desc}

This package contains unit tests.

%prep
%autosetup -n %{sname}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{py3_build}

%check
stestr-3 run --slowest

%install
%{py3_install}

%files -n python3-%{sname}
%license LICENSE
%{python3_sitelib}/%{pname}
%{python3_sitelib}/%{pname}-*.egg-info
%exclude %{python3_sitelib}/%{pname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{pname}/tests

%changelog
* Thu May 07 2020 RDO <dev@lists.rdoproject.org> 0.0.2-1
- Update to 0.0.2

# REMOVEME: error caused by commit https://opendev.org/x/sushy-oem-idrac/commit/1020e805d368684080660f10a5ee207d119c2b07
