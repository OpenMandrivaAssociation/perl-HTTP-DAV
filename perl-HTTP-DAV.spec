%define upstream_name    HTTP-DAV
%define upstream_version 0.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A WebDAV client library for Perl5
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-libwww-perl
BuildRequires:	perl(XML::DOM)
BuildRequires:	perl(Crypt::SSLeay)
BuildRequires:	perl(MD5)
BuildRequires:	perl-devel

BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

# requires a "test server"...
#make test TEST_VERBOSE=1

%install
%makeinstall_std

%files
%doc Changes README TODO doc/*
%{_bindir}/dave
%{_mandir}/*/*
%{perl_vendorlib}/HTTP


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.410.0-4mdv2012.0
+ Revision: 765363
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.410.0-2
+ Revision: 667202
- mass rebuild

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2011.0
+ Revision: 561577
- update to 0.41

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 497001
- update to 0.40

* Sun Dec 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-1mdv2010.1
+ Revision: 478057
- update to 0.39

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.0
+ Revision: 395166
- update to 0.38
- using %%perl_convert_version
- fixed license field

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2009.1
+ Revision: 318256
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.31-5mdv2009.0
+ Revision: 223793
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.31-4mdv2008.1
+ Revision: 180410
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary


* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 09:33:28 (63277)
- rebuild

* Sat Oct 07 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-06 07:09:09 (62898)
- Import perl-HTTP-DAV

* Thu Jul 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.31-2mdv2007.0
- use %%mkrel
- added fixes from debian (P0)

* Wed Oct 05 2005 Oden Eriksson <oeriksson@mandriva.com> 0.31-1mdk
- initial Mandriva package

