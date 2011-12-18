%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define age 1
%define release %{age}.sl5

Name:           tstorm
Version:        1.0.0
Release:        %{release}
Summary:        Python Module for Accessing and Modifying Configuration Data in INI files
Group:          Development/Libraries
License:        Apache License
URL:            http://code.google.com/p/iniparse/
Source0:        tstorm-%{version}-%{age}.tar.gz
BuildRoot:      %{_tmppath}/build-root-%{name}-%{version}-%{age}

BuildRequires: python-json

BuildArch: noarch

%description
iniparse is an INI parser for Python which is API compatible
with the standard library's ConfigParser, preserves structure of INI
files (order of sections & options, indentation, comments, and blank
lines are preserved when data is updated), and is more convenient to
use.

%prep
%setup -q -n %{name}-%{version}-%{age}


%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
#chmod 644 $RPM_BUILD_ROOT//usr/share/doc/emi-t-storm-%{version}/index.html
mv $RPM_BUILD_ROOT/usr/share/doc/tstorm-%{version}-%{age} $RPM_BUILD_ROOT/usr/share/doc/tstorm-%{version}
#mkdir -p $RPM_BUILD_ROOT/etc
mv $RPM_BUILD_ROOT/usr/etc $RPM_BUILD_ROOT/etc



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/tstorm-tp
%{_bindir}/tstorm-test-id
%doc  %{_docdir}/tstorm-%{version}/*
%dir %{_sysconfdir}/tstorm/*
%{python_sitelib}/tstorm


