%define module	coverage
%define name	python-%{module}
%define version 3.4
%define release %mkrel 1

Summary:	Code coverage measurement for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://nedbatchelder.com/code/coverage/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-setuptools
%py_requires -d

%description
Coverage measures code coverage, typically during test execution. It
uses the code analysis tools and tracing hooks provided in the Python
standard library to determine which lines are executable, and which
have been executed.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
chmod 644 *.txt coverage/htmlfiles/* coverage.egg-info/*
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt


