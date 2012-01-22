%define upstream_name    HTTP-DAV
%define upstream_version 0.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 4

Summary:	A WebDAV client library for Perl5
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-libwww-perl
BuildRequires:	perl(XML::DOM)
BuildRequires:	perl(Crypt::SSLeay)
BuildRequires:	perl(MD5)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
PerlDAV is a Perl library for modifying content on webservers using the WebDAV
protocol. Now you can LOCK, DELETE and PUT files and much more on a DAV-enabled
webserver.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
	
%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

# requires a "test server"...
#make test TEST_VERBOSE=1

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README TODO doc/*
%{_bindir}/dave
%{_mandir}/*/*
%{perl_vendorlib}/HTTP
