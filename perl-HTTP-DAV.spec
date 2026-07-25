%define modname	HTTP-DAV
%define modver 0.50

Summary:	A WebDAV client library for Perl5
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTTP-DAV
Source0:	https://cpan.metacpan.org/authors/id/C/CO/COSIMO/HTTP-DAV-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(XML::DOM)
BuildRequires:	perl(Crypt::SSLeay)
BuildRequires:	perl(MD5)
BuildRequires:	perl-devel

%description
PerlDAV is a Perl library for modifying content on webservers using the WebDAV
protocol. Now you can LOCK, DELETE and PUT files and much more on a DAV-enabled
webserver.

%prep
%setup -qn %{modname}-%{modver}

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
	
%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# requires a "test server"...
#make test TEST_VERBOSE=1

%install
%makeinstall_std

%files
%doc Changes README TODO doc/*
%{_bindir}/dave
%{perl_vendorlib}/HTTP
%{_mandir}/man1/*
%{_mandir}/man3/*


