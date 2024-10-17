%define upstream_name    Lingua-Stem
%define upstream_version 0.84

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Stemming of words
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Lingua::PT::Stemmer)
BuildRequires:	perl(Lingua::Stem::It)
BuildRequires:	perl(Lingua::Stem::Fr)
BuildRequires:	perl(Lingua::Stem::Snowball::Da)
BuildRequires:	perl(Lingua::Stem::Snowball::No)
BuildRequires:	perl(Lingua::Stem::Snowball::Se)
BuildRequires:	perl(Text::German)
BuildArch:	noarch

%description
This routine applies stemming algorithms to its parameters, returning the
stemmed words as appropriate to the selected locale.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*


%changelog
* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.840.0-1mdv2011.0
+ Revision: 552407
- update to 0.84

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.830.0-1mdv2010.0
+ Revision: 402572
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.83-4mdv2009.0
+ Revision: 257585
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.83-3mdv2009.0
+ Revision: 245626
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.83-1mdv2008.1
+ Revision: 136280
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.83-1mdv2008.0
+ Revision: 56095
- new version


* Mon Jul 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.82-1mdv2007.0
- New version 0.82
- spec cleanup
- fix directory ownership
- better summary

* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdv2007.0
- Rebuild

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.81-mdk
- 0.81
- Fix Url
- Fix Requires
- Make rpmbuildupdate Happy

* Thu Jun 03 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.70-1mdk
- 0.70
- fix buildrequires
- drop PREFIX
- use %%makeinstall_std macro
- cosmetics
- drop test for now

