%global debug_package %{nil}

Name: python-pillow
Epoch: 100
Version: 9.0.0
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
%fdupes -s %{buildroot}%{python3_sitearch}

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
