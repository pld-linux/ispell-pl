Summary:	Polish dictionary for ispell
Summary(pl):	Polski s³ownik dla ispell
Name:		ispell-pl
Version:	20021127
Release:	1
License:	GPL, but source URL and version must be specified
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/ispell-pl/%{name}-%{version}.tar.gz
URL:		http://ispell-pl.sourceforge.net/
BuildRequires:	ispell
Requires:	ispell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ispell-polish

%description
Polish dictionary for ispell, built from tarball taken from
http://dl.sourceforge.net/ispell-pl/.

%description -l pl
Polski s³ownik dla programu ispell, zbudowany z paczki ¶ci±gniêtej z
http://dl.sourceforge.net/ispell-pl/.

W tym pakiecie znajduje siê s³ownik skompilowany wg nastêpuj±cej
konfiguracji (slownik.cfg):

X A
X B
X C
X imiona-A
X imiona-B
X skroty

S£OWNIKI FACHOWE:
	biologia
	chemia
	druk
	ekonomia
	filozofia
	fizyka
	fizyka.ciala.stalego
	geografia
	historia
X	informatyka
	literatura
	matematyka
	medycyna
	muzyka
X	obce
	polityka
	prawo
	religia
	sport
	sztuka
X	technika
	wulgarne
	zeglarstwo

%prep
%setup -q

%build
cat > slowniki.cfg << EOF
X	A
X	B
X	C
X	imiona-A
X	imiona-B
X	skroty

S£OWNIKI FACHOWE:
	biologia
	chemia
	druk
	ekonomia
	filozofia
	fizyka
	fizyka.ciala.stalego
	geografia
	historia
X	informatyka
	literatura
	matematyka
	medycyna
	muzyka
X	obce
	polityka
	prawo
	religia
	sport
	sztuka
X	technika
	wulgarne
	zeglarstwo
EOF

./zbuduj.slownik.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ispell
install polish.aff $RPM_BUILD_ROOT%{_libdir}/ispell/
install polish.hash $RPM_BUILD_ROOT%{_libdir}/ispell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CZYTAJ.TO Changelog slowniki.cfg
%{_libdir}/ispell/*
