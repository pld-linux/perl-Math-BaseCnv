#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	BaseCnv
Summary:	Math::BaseCnv - quickly convert between any number bases
Summary(pl):	Math::BaseCnv - szybkie przeliczanie mi�dzy dowolnymi podstawami liczb
Name:		perl-Math-BaseCnv
Version:	1.0.446EIbS
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	a2791d8ea6ddb547d5ebeab484d8e3d1
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

%description -l pl
BaseCnv udost�pnia kilka prostych funkcji do przeliczania mi�dzy
dowolnymi podstawami liczb. Dzia�a tak szybko, jak tylko autor umia�
zrobi� (oczywi�cie polegaj�c tylko na ulubionym Perlu). W przypadku
ch�ci przeliczania mi�dzy podstawami z u�yciem sk�adni obiektowej
zamiast tego mo�na u�y� modu�u Math::BaseCalc Kena Williamsa.

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
%attr(755,root,root) %{_bindir}/bin/cnv
%{perl_vendorlib}/Math/BaseCnv.pm
%{_mandir}/man3/*
