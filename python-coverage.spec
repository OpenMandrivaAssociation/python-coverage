%define module	coverage

Summary:	Code coverage measurement for Python
Name:		python-%{module}
Version:	3.5.3
Release:	1
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://nedbatchelder.com/code/coverage/
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
chmod 644 *.txt coverage/htmlfiles/* coverage.egg-info/*
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt




%changelog
* Wed Oct 05 2011 Lev Givon <lev@mandriva.org> 3.5.1-1mdv2012.0
+ Revision: 703186
- Update to 3.5.1.

* Fri Jul 01 2011 Lev Givon <lev@mandriva.org> 3.5-1
+ Revision: 688522
- Update to 3.5.

* Wed Nov 03 2010 Michael Scherer <misc@mandriva.org> 3.4-2mdv2011.0
+ Revision: 592699
- rebuild for python 2.7

* Wed Oct 20 2010 Lev Givon <lev@mandriva.org> 3.4-1mdv2011.0
+ Revision: 586853
- import python-coverage

