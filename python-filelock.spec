#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tests	# unit tests (250+ processes created, max processes ulimit must allow it)

Summary:	A platform independent file lock
Summary(pl.UTF-8):	Niezależne od platformy blokady plikowe
Name:		python-filelock
Version:	3.0.12
Release:	2
License:	Public Domain
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/filelock/
Source0:	https://files.pythonhosted.org/packages/source/f/filelock/filelock-%{version}.tar.gz
# Source0-md5:	c1fe6d9a7433a7ca6ce4f36e273317d1
URL:		https://pypi.org/project/filelock/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.4

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

%if %{with tests}
%{__python} test.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} test.py
%endif
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
%doc LICENSE README.md
%{py_sitescriptdir}/filelock.py[co]
%{py_sitescriptdir}/filelock-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-filelock
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/filelock.py
%{py3_sitescriptdir}/__pycache__/filelock.cpython-*.py[co]
%{py3_sitescriptdir}/filelock-%{version}-py*.egg-info
%endif
