# TODO: finish doc
#
# Conditional build:
%bcond_without	tests	# unit tests (250+ processes created, max processes ulimit must allow it)
%bcond_with	doc	# Sphinx documentation

Summary:	A platform independent file lock
Summary(pl.UTF-8):	Niezależne od platformy blokady plikowe
Name:		python3-filelock
Version:	3.6.0
Release:	2
License:	Public Domain
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/filelock/
Source0:	https://files.pythonhosted.org/packages/source/f/filelock/filelock-%{version}.tar.gz
# Source0-md5:	b1032075ddada92874377426337c38a6
URL:		https://pypi.org/project/filelock/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 4
BuildRequires:	python3-pytest-timeout >= 1.4.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-furo >= 2021.8.17b43
BuildRequires:	python3-sphinx-autodoc-typehints >= 1.12
BuildRequires:	sphinx-pdg >= 4.1
%endif
Requires:	python3-modules >= 1:3.7
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

%prep
%setup -q -n filelock-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_timeout \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%if %{with doc}
sphinx-build -b html -d docs/_build/doctree docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/filelock
%{py3_sitescriptdir}/filelock-%{version}-py*.egg-info
