#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-resource-classes
Version  : 1.0.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/2f/7b/44983d7f190406204869c5689fe085a618f356ea9a44d62962b39423ed5d/os-resource-classes-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2f/7b/44983d7f190406204869c5689fe085a618f356ea9a44d62962b39423ed5d/os-resource-classes-1.0.0.tar.gz
Summary  : Resource Classes for OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: os-resource-classes-license = %{version}-%{release}
Requires: os-resource-classes-python = %{version}-%{release}
Requires: os-resource-classes-python3 = %{version}-%{release}
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
===================
os-resource-classes
===================
A list of standardized resource classes for OpenStack.

%package license
Summary: license components for the os-resource-classes package.
Group: Default

%description license
license components for the os-resource-classes package.


%package python
Summary: python components for the os-resource-classes package.
Group: Default
Requires: os-resource-classes-python3 = %{version}-%{release}

%description python
python components for the os-resource-classes package.


%package python3
Summary: python3 components for the os-resource-classes package.
Group: Default
Requires: python3-core
Provides: pypi(os_resource_classes)
Requires: pypi(pbr)

%description python3
python3 components for the os-resource-classes package.


%prep
%setup -q -n os-resource-classes-1.0.0
cd %{_builddir}/os-resource-classes-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585686066
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-resource-classes
cp %{_builddir}/os-resource-classes-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/os-resource-classes/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-resource-classes/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
