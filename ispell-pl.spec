Summary:	Polish dictionary for GNU ispell
Summary(pl):	Polski s�ownik dla GNU ispell
Name:		ispell-pl
Version:	20011004
Release:	1
License:	LGPL
Group:		Applications/Text
Source0:	ftp://ftp.icm.edu.pl/pub/unix/polish-ispell/ispell-pl-%{version}.tar.gz
Requires:	ispell
BuildRequires:	ispell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ispell-polish

%description
Polish dictionary for ispell.

%description -l pl
Polski s�ownik dla programu ispell, pochodz�cy z programu s�ownikowego
(patrz URL) W tym pakiecie znajdziesz s�ownik skompilowany wg
nast�puj�cej konfiguracji (slownik.cfg):

X A
X B
X C
X imiona-A
X imiona-B
X skroty

S�OWNIKI FACHOWE:
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
%setup -q -n %{version}

%build
cat > slowniki.cfg << EOF
X	A
X	B
X	C
X	imiona-A
X	imiona-B
X	skroty

S�OWNIKI FACHOWE:
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

cp polish.dic.proto polish.dic
./slowniki.pl
%{_bindir}/buildhash polish.dic polish.aff polish.hash \
 && rm -f polish.dic polish.dic.cnt polish.dic.stat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ispell
install polish.aff $RPM_BUILD_ROOT%{_libdir}/ispell/
install polish.hash $RPM_BUILD_ROOT%{_libdir}/ispell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/ispell/*
