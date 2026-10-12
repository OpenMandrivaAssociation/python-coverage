%define module coverage

Name:		python-coverage
Version:	7.15.2
Release:	2
Summary:	Code coverage measurement for Python
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/coverage/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Obsoletes:	python2-coverage

%description
Code coverage measurement for Python.

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%{_bindir}/%{module}*
%{py_platsitedir}/a1_coverage.pth
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-%{version}.dist-info
