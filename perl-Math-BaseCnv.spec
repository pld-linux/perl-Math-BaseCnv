#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	BaseCnv
%include	/usr/lib/rpm/macros.perl
Summary:	Math::BaseCnv - quickly convert between any number bases
Summary(pl.UTF-8):	Math::BaseCnv - szybkie przeliczanie między dowolnymi podstawami liczb
Name:		perl-Math-BaseCnv
Version:	1.4.75O6Pbr
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	60d5fb31db63e3d7a9807b0df37c4a80
URL:		http://search.cpan.org/dist/Math-BaseCnv/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BaseCnv provides a few simple functions for converting between
arbitrary number bases. It is as fast as the author currently knows
how to make it (of course relying only on the lovely Perl). If you
would rather utilize an object syntax for number-base conversion,
please see Ken Williams' fine Math::BaseCalc module.

%description -l pl.UTF-8
BaseCnv udostępnia kilka prostych funkcji do przeliczania między
dowolnymi podstawami liczb. Działa tak szybko, jak tylko autor umiał
zrobić (oczywiście polegając tylko na ulubionym Perlu). W przypadku
chęci przeliczania między podstawami z użyciem składni obiektowej
zamiast tego można użyć modułu Math::BaseCalc Kena Williamsa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/BaseCnv.pm
%{_mandir}/man3/*
