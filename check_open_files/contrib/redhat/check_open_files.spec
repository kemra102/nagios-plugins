%if 0%{?rhel} == 5
  %define dist .el5
%endif
%if 0%{?rhel} == 6
  %define dist .el6
%endif
%if 0%{?rhel} == 7
  %define dist .el7
%endif
%define version 1.0

Summary: A Nagios plugin to check the number of files a user has open.
Name: nagios-plugins-check-open-files
Version: %{?version}
Release: 1.20160719e752f09%{?dist}
License: BSD
Group: Applications/System
Source0: check_open_files
Source1: README.md
Source2: LICENSE
URL: https://github.com/kemra102/nagios-plugins

BuildArch: noarch
Requires: ruby
Requires: sudo
Requires: bash

%description
A Nagios plugin to check the number of files a user has open..

%prep
cp -p %SOURCE0 .
cp -p %SOURCE1 .
cp -p %SOURCE2 .

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/nagios/plugins/
install -m 755 check_open_files %{buildroot}/%{_libdir}/nagios/plugins/

%files
%if 0%{?rhel} == 7
  %doc README.md
  %license LICENSE
%else
  %doc README.md LICENSE
%endif
%attr(0755, root, root) %{_libdir}/nagios/plugins/check_open_files

%changelog
* Tue Jul 19 2016 Danny Roberts <danny.roberts@skybettingandgaming.com> 1.0
- Initial release.
