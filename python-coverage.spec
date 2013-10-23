%define module	coverage

Summary:	Code coverage measurement for Python
Name:		python-%{module}
Version:	3.7
Release:	2
Source0:	http://pypi.python.org/packages/source/c/coverage/coverage-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://nedbatchelder.com/code/coverage/
BuildRequires:	python-setuptools
BuildRequires:  python-devel
BuildRequires:  python3-devel
BuildRequires:  python3egg(setuptools)

%description
Coverage measures code coverage, typically during test execution. It
uses the code analysis tools and tracing hooks provided in the Python
standard library to determine which lines are executable, and which
have been executed.

%package -n python3-coverage
Summary:        Code coverage measurement for Python
Group:          Development/Python
Requires:       python3
 
%description -n python3-coverage
Coverage measures code coverage, typically during test execution. It
uses the code analysis tools and tracing hooks provided in the Python
standard library to determine which lines are executable, and which
have been executed.

%prep
%setup -q -c

mv %{module}-%{version} python2
cp -r python2 python3

%build
pushd python2
%{__python} setup.py build
popd

pushd python3
%{__python3} setup.py build
popd

%install
pushd python2
%{__python} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python3} setup.py install --root=%{buildroot}
popd

%files -n python-coverage 
%doc python2/*.txt
%{python_sitearch}/coverage
%{python_sitearch}/coverage-%{version}-py%{py_ver}.egg-info
/usr/bin/coverage
/usr/bin/coverage2
/usr/bin/coverage-%{py_ver}

%files -n python3-coverage
%doc python3/*.txt
%{python3_sitearch}/coverage
%{python3_sitearch}/coverage-%{version}-py%{py3_ver}.egg-info
/usr/bin/coverage3
/usr/bin/coverage-%{py3_ver}
