#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Statistics
%define		pnam	Shannon
Summary:	Statistics::Shannon - Shannon index
Summary(pl.UTF-8):	Statistics::Shannon - wskaźnik Shannona
Name:		perl-Statistics-Shannon
Version:	0.03
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b8f44ee0699a22296726982ef1e70ee5
URL:		http://search.cpan.org/dist/Statistics-Shannon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Statistics-Frequency >= 0.03
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Statistics::Shannon module can be used to compute the Shannon
index of data, which is a variability measure of data.

%description -l pl.UTF-8
Moduł Statistics::Shannon może być używany do liczenia wskaźnika
Shannona danych, który jest miarą zmienności danych.

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
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
