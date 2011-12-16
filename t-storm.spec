%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           emi-t-storm
Version:        1.0.0
Release:        1%{?dist}
Summary:        Python Module for Accessing and Modifying Configuration Data in INI files
Group:          Development/Libraries
License:        Apache
URL:            http://code.google.com/p/iniparse/
Source0:        emi-t-storm-%{version}-1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-1-%{release}-root-%(%{__id_u} -n)

BuildRequires: python-json

BuildArch: noarch

%description
iniparse is an INI parser for Python which is API compatible
with the standard library's ConfigParser, preserves structure of INI
files (order of sections & options, indentation, comments, and blank
lines are preserved when data is updated), and is more convenient to
use.

%prep
%setup -q -n -%{version}


%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# fixes
#chmod 644 $RPM_BUILD_ROOT//usr/share/doc/emi-t-storm-%{version}/index.html
#mv $RPM_BUILD_ROOT/usr/share/doc/emi-t-storm-%{version} $RPM_BUILD_ROOT/usr/share/doc/emi-tstorm-%{version}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc  %{_docdir}/emi-t-storm-%{version}/*
%{python_sitelib}/tstorm
%{python_sitelib}/tstorm-%{version}-py*.egg-info


