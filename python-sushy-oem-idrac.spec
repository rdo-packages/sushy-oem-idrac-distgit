%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname sushy-oem-idrac

%if 0%{?fedora}
%global with_python3 1
%endif

Name: python-%{sname}
Version: XXX
Release: XXX
Summary: Sushy OEM iDRAC is a Python extension module for Sushy library to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org)
License: ASL 2.0
URL: http://launchpad.net/sushy/

Source0: http://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz

BuildArch: noarch

%description
Sushy is a Python library to communicate with Redfish based systems (http://redfish.dmtf.org)

%package -n python2-%{sname}
Summary: Sushy OEM iDRAC is a Python extension module for Sushy library to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org)
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires: python2-devel
BuildRequires: python2-pbr
BuildRequires: python-setuptools

Requires: python2-pbr >= 2.0.0
Requires: python-six >= 1.10.0
Requires: python-requests >= 2.14.2

%description -n python2-%{sname}
Sushy OEM iDRAC is a Python extension module for Sushy library to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org)

%package -n python2-%{sname}-tests
Summary: Sushy OEM iDRAC tests
Requires: python2-%{sname} = %{version}-%{release}

%description -n python2-%{sname}-tests
Tests for Sushy OEM iDRAC

%if 0%{?with_python3}

%package -n python3-%{sname}
Summary: Sushy OEM iDRAC is a Python extension module for Sushy library to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org)

%{?python_provide:%python_provide python3-%{sname}}
BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools

Requires: python3-pbr >= 2.0.0
Requires: python3-six >= 1.10.0
Requires: python3-requests >= 2.14.2

%description -n python3-%{sname}
Sushy OEM iDRAC is a Python extension module for Sushy library to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org)

%package -n python3-%{sname}-tests
Summary: Sushy OEM iDRAC tests
Requires: python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
Tests for Sushy OEM iDRAC

%endif # with_python3

%package -n python-%{sname}-doc
Summary: Sushy OEM iDRAC documentation

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx

%description -n python-%{sname}-doc
Documentation for Sushy OEM iDRAC

%prep
%autosetup -n %{sname}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # with_python3

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif # with_python3

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/%{sname}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{sname}
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{sname}

%files -n python2-%{sname}
%license LICENSE
%{python2_sitelib}/%{sname}
%{python2_sitelib}/%{sname}-*.egg-info
%exclude %{python2_sitelib}/%{sname}/tests

%files -n python2-%{sname}-tests
%license LICENSE
%{python2_sitelib}/%{sname}/tests

%if 0%{?with_python3}

%files -n python3-%{sname}
%license LICENSE
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%endif # with_python3

%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
* Thu Dec  5 12:12:03 UTC 2019  Ilya Etingof <etingof@gmail.com> 0.2.0-2
- Initial package.
