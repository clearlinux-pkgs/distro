#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : distro
Version  : 1.4.0
Release  : 13
URL      : https://github.com/nir0s/distro/archive/v1.4.0.tar.gz
Source0  : https://github.com/nir0s/distro/archive/v1.4.0.tar.gz
Summary  : No detailed summary available
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
Patch1: os-release.patch

%description
Distro - an OS platform information API
=======================================
[![Build Status](https://travis-ci.org/nir0s/distro.svg?branch=master)](https://travis-ci.org/nir0s/distro)
[![Build status](https://ci.appveyor.com/api/projects/status/e812qjk1gf0f74r5/branch/master?svg=true)](https://ci.appveyor.com/project/nir0s/distro/branch/master)
[![PyPI version](http://img.shields.io/pypi/v/distro.svg)](https://pypi.python.org/pypi/distro)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/distro.svg)](https://img.shields.io/pypi/pyversions/distro.svg)
[![Requirements Status](https://requires.io/github/nir0s/distro/requirements.svg?branch=master)](https://requires.io/github/nir0s/distro/requirements/?branch=master)
[![Code Coverage](https://codecov.io/github/nir0s/distro/coverage.svg?branch=master)](https://codecov.io/github/nir0s/distro?branch=master)
[![Code Quality](https://landscape.io/github/nir0s/distro/master/landscape.svg?style=flat)](https://landscape.io/github/nir0s/distro)
[![Is Wheel](https://img.shields.io/pypi/wheel/distro.svg?style=flat)](https://pypi.python.org/pypi/distro)
[![Latest Github Release](https://readthedocs.org/projects/distro/badge/?version=stable)](http://distro.readthedocs.io/en/latest/)
[![Join the chat at https://gitter.im/nir0s/distro](https://badges.gitter.im/nir0s/distro.svg)](https://gitter.im/nir0s/distro?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

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

%description python3
python3 components for the distro package.


%prep
%setup -q -n distro-1.4.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550191835
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/distro
cp LICENSE %{buildroot}/usr/share/package-licenses/distro/LICENSE
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
/usr/share/package-licenses/distro/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
