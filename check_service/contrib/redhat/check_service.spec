%if 0%{?rhel} == 5
  %define dist .el5
%if 0%{?rhel} == 6
  %define dist .el6
%if 0%{?rhel} == 7
  %define dist .el7
%endif
%define version 1.0

Summary: A Nagios plugin to check the status of a Linux service.
Name: nagios-plugins-check-service
Version: %{?version}
Release: %{?dist}
Copyright: BSD
Group: Applications/System
Source0: check_service
Source1: README.md
Source2: LICENSE
URL: https://github.com/kemra102/nagios-plugins

Requires: ruby

%description
A Nagios plugin to check the status of a Linux service.

%prep
rm -rf $RPM_BUILD_DIR/nagios-plugins-check-service-%{?version}

%configure
cp %{SOURCE1} ./README
cp %{SOURCE2} ./LICENSE

%install
install -m 0755 check_service %{buildroot}/%{_libdir}/nagios/plugins

%files
%doc README LICENSE
%{_libdir}/nagios/plugins/check_service

%changelog
* Sat Nov 22 2015 Danny Roberts <danny@thefallenphoenix.net> 1.0
- Initial release.
