%define module HTTP-DAV

Name:		perl-%{module}
Version:	0.35
Release:	%mkrel 1
Summary:	A WebDAV client library for Perl5
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/HTTP/%{module}-%{version}.tar.gz
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
%setup -q -n %{module}-%{version}

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
