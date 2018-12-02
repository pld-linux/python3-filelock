#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A platform independent file lock
Summary(pl.UTF-8):	Niezależne od platformy blokady plikowe
Name:		python-filelock
Version:	3.0.10
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/filelock/
Source0:	https://files.pythonhosted.org/packages/source/f/filelock/filelock-%{version}.tar.gz
# Source0-md5:	df0006d2b1ec96473bfc0927de123aa6
URL:		https://pypi.org/project/filelock/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a single module, which implements a platform
independent file lock in Python, which provides a simple way of
inter-process communication.

%description -l pl.UTF-8
Ten pakiet zawiera pojedynczny moduł implementujący niezależne od
platformy blokady plikowe w Pythonie. Zapewniają one prosty sposób
komunikacji międzyprocesowej.

%package -n python3-filelock
Summary:	A platform independent file lock
Summary(pl.UTF-8):	Niezależne od platformy blokady plikowe
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-filelock
This package contains a single module, which implements a platform
independent file lock in Python, which provides a simple way of
inter-process communication.

%description -n python3-filelock -l pl.UTF-8
Ten pakiet zawiera pojedynczny moduł implementujący niezależne od
platformy blokady plikowe w Pythonie. Zapewniają one prosty sposób
komunikacji międzyprocesowej.

%prep
%setup -q -n filelock-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst
%{py_sitescriptdir}/filelock.py[co]
%{py_sitescriptdir}/filelock-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-filelock
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst
%{py3_sitescriptdir}/filelock.py
%{py3_sitescriptdir}/__pycache__/filelock.cpython-*.py[co]
%{py3_sitescriptdir}/filelock-%{version}-py*.egg-info
%endif
