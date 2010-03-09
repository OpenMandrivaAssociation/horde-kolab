%define prj Kolab

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-kolab
Version:       0.0.6
Release:       %mkrel 1
Summary:       Horde Mime Library
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): %{_bindir}/pear
Requires:      horde-nls
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The Horde_MIME:: class provides methods for dealing with MIME standards.

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



