%define pkgname HTTP-DAV

Summary:	A WebDAV client library for Perl5
Name:		perl-%{pkgname}
Version:	0.31
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	http://www.cpan.org/authors/id/P/PC/PCOLLINS/%{pkgname}-%{version}.tar.bz2
Patch0:		libhttp-dav-perl_0.31-3.diff
BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-XML-DOM
BuildRequires:	perl-Crypt-SSLeay
BuildRequires:	perl-MD5
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
PerlDAV is a Perl library for modifying content on webservers using the WebDAV
protocol. Now you can LOCK, DELETE and PUT files and much more on a DAV-enabled
webserver.

%prep

%setup -q -n %{pkgname}-%{version}
%patch0 -p1

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
	
# cleanup
for i in `find . -type d -name CVS`  `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

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
%doc Changes README TODO debian/changelog
%{_bindir}/dave
%{perl_vendorlib}/HTTP/DAV.pm
%dir %{perl_vendorlib}/HTTP/DAV
%{perl_vendorlib}/HTTP/DAV/*.pm
%{_mandir}/*/*


