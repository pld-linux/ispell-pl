Summary:	Polish dictionary for ispell
Summary(pl.UTF-8):   Polski słownik dla ispella
Name:		ispell-pl
Version:	20021127
Release:	4
License:	GPL, but source URL and version must be specified
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/ispell-pl/%{name}-%{version}.tar.gz
# Source0-md5:	91418bdae4b7a4eb6a8cc69be8e5787d
Patch0:		%{name}-posix.patch
URL:		http://ispell-pl.sourceforge.net/
BuildRequires:	ispell >= 3.2.06
Requires:	ispell >= 3.2.06
Obsoletes:	ispell-polish
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish dictionary for ispell, built from tarball taken from
http://dl.sourceforge.net/ispell-pl/.

Build configuration (list of included subdictionaries) can be viewed
in slowniki.cfg file in package documentation.

%description -l pl.UTF-8
Polski słownik dla programu ispell, zbudowany z paczki ściągniętej z
http://dl.sourceforge.net/ispell-pl/.

Konfigurację (lista dołączonych słowników) można obejrzeć w pliku
slowniki.cfg z dokumentacji pakietu.

%prep
%setup -q
%patch0 -p1

%build
./zbuduj.slownik.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ispell

install polish.aff $RPM_BUILD_ROOT%{_libdir}/ispell
install polish.hash $RPM_BUILD_ROOT%{_libdir}/ispell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CZYTAJ.TO Changelog slowniki.cfg
%{_libdir}/ispell/*
