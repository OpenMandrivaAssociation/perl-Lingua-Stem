%define module  Lingua-Stem
%define name    perl-%{module}
%define version 0.83
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Stemming of words
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Lingua/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Lingua::PT::Stemmer)
BuildRequires:  perl(Lingua::Stem::It)
BuildRequires:  perl(Lingua::Stem::Fr)
BuildRequires:  perl(Lingua::Stem::Snowball::Da)
BuildRequires:  perl(Lingua::Stem::Snowball::No)
BuildRequires:  perl(Lingua::Stem::Snowball::Se)
BuildRequires:  perl(Text::German)
BuildArch:      noarch

%description
This routine applies stemming algorithms to its parameters, returning the
stemmed words as appropriate to the selected locale.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*

