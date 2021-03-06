Name:          adb-utils
Version:       1.2
Release:       1%{?dist}
Summary:       Installs the necessary utils/service files to support ADB/CDK

License:       GPLV2
BuildArch:     noarch

URL:           https://github.com/projectatomic/%{name}
Source0:       https://github.com/projectatomic/%{name}/archive/v%{version}.tar.gz

BuildRequires: systemd

%description
Includes the utils files and service files that are required for the running
specific service and directly including it to kickstart file.

%prep
%setup -q -n %{name}-%{version}

%install
%{__mkdir_p} %{buildroot}/opt/adb/openshift
%{__mkdir_p} %{buildroot}%{_sysconfdir}/sysconfig/
%{__mkdir_p} %{buildroot}%{_unitdir}
%{__mkdir_p} %{buildroot}%{_bindir}

%{__install} -pm644 services/openshift/openshift.service \
%{buildroot}%{_unitdir}/openshift.service
%{__cp} services/openshift/openshift_option \
%{buildroot}%{_sysconfdir}/sysconfig/openshift_option
%{__cp} services/openshift/scripts/* %{buildroot}/opt/adb/openshift/
%{__cp} utils/* %{buildroot}/opt/adb/
ln -s /opt/adb/sccli.sh %{buildroot}%{_bindir}/sccli

%files
%{_sysconfdir}/sysconfig/openshift_option
%{_unitdir}/openshift.service
%{_bindir}/sccli
/opt/adb/
%doc LICENSE  README.rst

%changelog
* Wed Mar 09 2016 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.2-1
- Update to 1.2 with couple of bugfix

* Thu Mar 03 2016 Lalatendu Mohanty <lmohanty@redhat.com> 1.1-1
- Updating to 1.1 and couple of specfile fixes
- Removing dependancy on commit0

* Tue Mar 01 2016 Brian Exelbierd <bex@pobox.com> 1-4
- Architecture change: openshift image/version info passed from the
  Vagrantfile to the box
- docker pull is now done in sccli
- Uses IMAGE_* variables so that sccli can use same for other svcs
- DOCKER_REGISTRY var removed from openshift_options now in image name
- `docker tag` removed from the unit file
- when using openshift, enable the service for future reboots
- CLI binaries now copied with `docker cp` for efficiency

* Tue Feb 09 2016 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1-3
- Add sccli changes

* Fri Feb 05 2016 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1-2
- Update to latest source 

* Mon Feb 01 2016 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1-1
- Initial attemp to create a rpm
