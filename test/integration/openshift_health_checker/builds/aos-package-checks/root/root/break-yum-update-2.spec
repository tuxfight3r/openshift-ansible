Name:           break-yum-update
Version:        1.0
Release:        2
Summary:        Package for breaking updates by requiring things that don't exist

License:        NA

Requires:	package-that-does-not-exist
Source0:	http://example.com/foo.tgz
BuildArch:	noarch

%description
Package for breaking updates by requiring things that don't exist


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT


%files
%doc



%changelog
