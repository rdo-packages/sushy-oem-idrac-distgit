%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order sphinx openstackdocstheme

%global sname sushy-oem-idrac
%global pname sushy_oem_idrac

%global common_desc \
Sushy OEM iDRAC is a Python extension module for the Sushy library \
to communicate with Redfish-enabled Dell/EMC servers (http://redfish.dmtf.org).

Name: python-%{sname}
Version: XXX
Release: XXX
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers
License: Apache-2.0
URL: https://opendev.org/x/%{sname}

Source0: https://files.pythonhosted.org/packages/source/s/%{sname}/%{sname}-%{upstream_version}.tar.gz

BuildArch: noarch

%description
%{common_desc}

%package -n python3-%{sname}
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers

BuildRequires: git-core
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary: An extension for the Sushy library to communicate with Redfish-enabled Dell/EMC servers - tests
Requires: python3-%{sname} = %{version}-%{release}

Requires: python3-mock
Requires: python3-oslotest
Requires: python3-testtools

%description -n python3-%{sname}-tests
%{common_desc}

This package contains unit tests.

%prep
%autosetup -n %{sname}-%{upstream_version} -S git


sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%check
%tox -e %{default_toxenv}

%install
%pyproject_install

%files -n python3-%{sname}
%license LICENSE
%{python3_sitelib}/%{pname}
%{python3_sitelib}/%{pname}-*.dist-info
%exclude %{python3_sitelib}/%{pname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{pname}/tests

%changelog
