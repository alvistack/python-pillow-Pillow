# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pillow
Epoch: 100
Version: 9.1.1
Release: 1%{?dist}
Summary: Python Imaging Library (Fork)
License: HPND
URL: https://github.com/python-pillow/Pillow/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
BuildRequires: liblcms2-devel
%else
BuildRequires: lcms2-devel
%endif
BuildRequires: fdupes
BuildRequires: freetype-devel
BuildRequires: gcc
BuildRequires: libjpeg-devel
BuildRequires: libraqm-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: make
BuildRequires: openjpeg2-devel
BuildRequires: python-rpm-macros
BuildRequires: python3-cffi
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-olefile
BuildRequires: python3-setuptools
BuildRequires: zlib-devel

%description
The Python Imaging Library adds image processing capabilities to your
Python interpreter.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pillow
Summary: Python Imaging Library (Fork)
Requires: python3
Requires: python3-olefile
Provides: python3-pillow = %{epoch}:%{version}-%{release}
Provides: python3dist(pillow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pillow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pillow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pillow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pillow) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pillow
The Python Imaging Library adds image processing capabilities to your
Python interpreter.

%files -n python%{python3_version_nodots}-pillow
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pillow
Summary: Python Imaging Library (Fork)
Requires: python3
Requires: python3-olefile
Provides: python3-pillow = %{epoch}:%{version}-%{release}
Provides: python3dist(pillow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pillow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pillow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pillow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pillow) = %{epoch}:%{version}-%{release}

%description -n python3-pillow
The Python Imaging Library adds image processing capabilities to your
Python interpreter.

%files -n python3-pillow
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
