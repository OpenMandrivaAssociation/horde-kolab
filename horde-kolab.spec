%define prj Kolab

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-kolab
Version:       0.0.6
Release:       4
Summary:       Horde Mime Library
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-nls
Requires:      php-pear
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
This package contains a number of helper functions that make communication
between a Horde client and a Kolab server smoother.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%{peardir}/Horde/Kolab.php





%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.6-3mdv2011.0
+ Revision: 564029
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.6-2mdv2010.1
+ Revision: 524851
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear

* Tue Mar 09 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.6-1mdv2010.1
+ Revision: 516847
- Updated Description Line
- really removed BuilRequires: horde-framework
- added Requires: php-pear
  removed BuildRequires: horde-framework
- import horde-kolab


