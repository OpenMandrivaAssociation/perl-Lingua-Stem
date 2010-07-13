%define upstream_name    Lingua-Stem
%define upstream_version 0.84

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Stemming of words
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This routine applies stemming algorithms to its parameters, returning the
stemmed words as appropriate to the selected locale.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
