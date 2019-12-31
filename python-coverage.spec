%define module	coverage

Summary:	Code coverage measurement for Python
Name:		python-%{module}
Version:	5.0.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/06/5d/241de8854b6353a17d168223e7a16544ba560954bdfe25ef7337ba14cc28/coverage-5.0.1.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://nedbatchelder.com/code/coverage/
BuildRequires:	python2-setuptools
BuildRequires:	python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-distribute
#%%rename		python-coverage

%description
Coverage measures code coverage, typically during test execution. It
uses the code analysis tools and tracing hooks provided in the Python
standard library to determine which lines are executable, and which
have been executed.

%package -n python2-coverage
Summary:        Code coverage measurement for Python
Group:          Development/Python
Requires:       python2
 
%description -n python2-coverage
Coverage measures code coverage, typically during test execution. It
uses the code analysis tools and tracing hooks provided in the Python
standard library to determine which lines are executable, and which
have been executed.

%prep
%setup -q -c

mv %{module}-%{version} python2
cp -r python2 python

%build
pushd python2
%{__python2} setup.py build
popd

pushd python
%{__python} setup.py build
popd

%install
pushd python2
%{__python2} setup.py install --root=%{buildroot}
popd

pushd python
%{__python} setup.py install --root=%{buildroot}
popd

%files -n python-coverage 
%doc python/*.txt
%{python_sitearch}/coverage
%{python_sitearch}/coverage-%{version}-py%{py3_ver}.egg-info
/usr/bin/coverage
/usr/bin/coverage3
/usr/bin/coverage-%{py3_ver}

%files -n python2-coverage
%doc python2/*.txt
%{python2_sitearch}/coverage
%{python2_sitearch}/coverage-%{version}-py%{py2_ver}.egg-info
/usr/bin/coverage2
/usr/bin/coverage-%{py2_ver}
