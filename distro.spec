#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : distro
Version  : 1.6.0
Release  : 29
URL      : https://github.com/python-distro/distro/archive/v1.6.0/distro-1.6.0.tar.gz
Source0  : https://github.com/python-distro/distro/archive/v1.6.0/distro-1.6.0.tar.gz
Summary  : Distro - an OS platform information API
Group    : Development/Tools
License  : Apache-2.0
Requires: distro-bin = %{version}-%{release}
Requires: distro-license = %{version}-%{release}
Requires: distro-python = %{version}-%{release}
Requires: distro-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-Check-for-empty-etc-os-release.patch

%description
Distro - an OS platform information API
=======================================
[![CI Status](https://github.com/python-distro/distro/workflows/CI/badge.svg)](https://github.com/python-distro/distro/actions/workflows/ci.yaml)
[![PyPI version](http://img.shields.io/pypi/v/distro.svg)](https://pypi.python.org/pypi/distro)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/distro.svg)](https://img.shields.io/pypi/pyversions/distro.svg)
[![Code Coverage](https://codecov.io/github/python-distro/distro/coverage.svg?branch=master)](https://codecov.io/github/python-distro/distro?branch=master)
[![Is Wheel](https://img.shields.io/pypi/wheel/distro.svg?style=flat)](https://pypi.python.org/pypi/distro)
[![Latest Github Release](https://readthedocs.org/projects/distro/badge/?version=stable)](http://distro.readthedocs.io/en/latest/)
[![Join the chat at https://gitter.im/python-distro/distro](https://badges.gitter.im/python-distro/distro.svg)](https://gitter.im/python-distro/distro?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package bin
Summary: bin components for the distro package.
Group: Binaries
Requires: distro-license = %{version}-%{release}

%description bin
bin components for the distro package.


%package license
Summary: license components for the distro package.
Group: Default

%description license
license components for the distro package.


%package python
Summary: python components for the distro package.
Group: Default
Requires: distro-python3 = %{version}-%{release}

%description python
python components for the distro package.


%package python3
Summary: python3 components for the distro package.
Group: Default
Requires: python3-core
Provides: pypi(distro)

%description python3
python3 components for the distro package.


%prep
%setup -q -n distro-1.6.0
cd %{_builddir}/distro-1.6.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629505845
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/distro
cp %{_builddir}/distro-1.6.0/LICENSE %{buildroot}/usr/share/package-licenses/distro/c700a8b9312d24bdc57570f7d6a131cf63d89016
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/distro

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/distro/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
