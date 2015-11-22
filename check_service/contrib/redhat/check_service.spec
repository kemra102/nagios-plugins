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

Summary: A Nagios plugin to check the status of a Linux service.
Name: nagios-plugins-check-service
Version: %{?version}
Release: 1%{?dist}
License: BSD
Group: Applications/System
Source0: check_service
Source1: README.md
Source2: LICENSE
URL: https://github.com/kemra102/nagios-plugins

BuildArch: noarch
Requires: ruby

%description
A Nagios plugin to check the status of a Linux service.

%prep -q
cp -p %SOURCE0 .
cp -p %SOURCE1 .
cp -p %SOURCE2 .

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/nagios/plugins/
install -m 755 check_service %{buildroot}/%{_libdir}/nagios/plugins/

%files
%doc README.md
%license LICENSE
%attr(0755, root, root) %{_libdir}/nagios/plugins/check_service

%changelog
* Sun Nov 22 2015 Danny Roberts <danny@thefallenphoenix.net> 1.0
- Initial release.
