Name:		python-coverage
Version:	7.7.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/coverage/coverage-%{version}.tar.gz
Summary:	Code coverage measurement for Python
URL:		https://pypi.org/project/coverage/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python-devel
BuildSystem:	python
Obsoletes:	python2-coverage

%description
Code coverage measurement for Python

%prep
%autosetup -p1 -n coverage-%{version}

%files
%{_bindir}/coverage*
%{py_platsitedir}/coverage
%{py_platsitedir}/coverage-%{version}.dist-info
