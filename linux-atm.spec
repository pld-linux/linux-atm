# $Revision: 1.10 $ $Date: 2002-02-19 12:55:01 $
Summary:	ATM on Linux
Summary(pl):	Obs≥uga sieci ATM w Linuxie
Name:		linux-atm
Version:	2.4.0
Release:	1
License:	GPL
Group:		Networking
Group(cs):	SÌªovÈ
Group(da):	NetvÊrks
Group(de):	Netzwerkwesen
Group(es):	Red
Group(fr):	RÈseau
Group(is):	Net
Group(it):	Rete
Group(no):	Nettverks
Group(pl):	Sieciowe
Group(pt_BR):	Rede
Group(pt):	Rede
Group(ru):	Û≈‘ÿ
Group(sl):	Omreæni
Group(sv):	N‰tverk
Group(uk):	Ì≈“≈÷¡
Source0:	http://prdownloads.sourceforge.net/linux-atm/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}.1-pldrc.tar.gz
Source2:	http://home.sch.bme.hu/~cell/br2684/dist/001212/pppbr-001212-br2684ctl.c
Patch0:		%{name}-syslog.patch
Patch1:		%{name}-br2684ctl-syslog.patch
Icon:		linux-atm-logo.gif
URL:		http://linux-atm.sourceforge.net/
BuildRequires:	autoconf
Conflicts:	kernel-headers < 2.4
Obsoletes:	atm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ATM (Asynchronous Transfer Mode) networking for Linux is still under
development now but it works quite stable now and will most probably
be included in 2.4.x series kernels. In PLD Linux it consists of some
patches for current kernel version containing drivers for a few
popular ATM cards (ex. Fore, Madge, IDT) and PVC and SVC support. It
also includes programs and scripts providing the most popular ATM
services, i.e. Classical IP (IP over ATM), LAN Emulation clients and
servers, Multiprotocol Over ATM (MPOA) and some other goodies.

%description -l pl
Obs≥uga sieci ATM (Asynchronous Transfer Mode) w Linuxie mimo iø jest
jeszcze w stadium alfa dzia≥a juø bardzo stabilnie i
najproawdopodobniej zostanie w≥±czona do j±der serii 2.4.x. W Linuxie
PLD sk≥ada siÍ ona z ≥at (patches) do bieø±cej wersji j±dra
zawieraj±cych sterowniki do kilku popularnych kart (m.in Fore, Madge,
IDT) i zapewniaj±cych zestawianie po≥±czeÒ PVC i SVC oraz zestawu
programÛw i skryptÛw (ten pakiet) realizuj±cych najpopularniejsze
us≥ugi ATM, tj. Classical IP (IP over ATM), klientÛw i serwery LAN
Emulation (LANE), Multiprotocol Over ATM (MPOA) i inne rozmaito∂ci.

%package devel
Summary:	ATM on Linux - developer's package
Summary(pl):	Obs≥uga sieci ATM w Linuxie - biblioteki i pliki nag≥Ûwkowe
Group:		Development/Libraries
Group(cs):	V˝vojovÈ prost¯edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	ﬁrÛunartÛl/Agerasˆfn
Group(it):	Sviluppo/Librerie
Group(ja):	≥´»Ø/•È•§•÷•È•Í
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(sl):	Razvoj/Knjiænice
Group(sv):	Utveckling/Bibliotek
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Obsoletes:	atm-devel
Requires:	%{name} = %{version}

%description devel
Libraries and header files needed for development ATM applications for
Linux.

%description devel -l pl
Biblioteki i pliki nag≥Ûwkowe niezbÍdne do opracowywania aplikacji ATM
dla Linuxa.

%package static
Summary:	ATM on Linux - static libraries
Summary(pl):	Obs≥uga sieci ATM w Linuxie - biblioteki statyczne
Group:		Development/Libraries
Group(cs):	V˝vojovÈ prost¯edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	ﬁrÛunartÛl/Agerasˆfn
Group(it):	Sviluppo/Librerie
Group(ja):	≥´»Ø/•È•§•÷•È•Í
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(sl):	Razvoj/Knjiænice
Group(sv):	Utveckling/Bibliotek
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Obsoletes:	atm-static
Requires:	%{name}-devel = %{version}

%description static
Static libraries needed for development ATM applications for Linux.

%description static -l pl
Biblioteki statyczne niezbÍdne do opracowywania aplikacji ATM dla
Linuxa.

%package rc-scripts
Summary:	ATM on Linux - rc-scripts
Summary(pl):	Obs≥uga sieci ATM w Linuxie - skrypty startowe
Group:		Base
Group(cs):	Z·klad
Group(da):	Basal
Group(de):	Basis
Group(es):	Base
Group(fr):	Base
Group(is):	Grunnforrit
Group(it):	Base
Group(ja):	•Ÿ°º•π
Group(no):	Basis
Group(pl):	Podstawowe
Group(pt):	Base
Group(pt_BR):	Base
Group(ru):	‚¡⁄¡
Group(sl):	Osnova
Group(sv):	Bas
Group(uk):	‚¡⁄¡
Requires:	%{name} = %{version}
Requires:	rc-scripts >= 0.2.9
Obsoletes:	atm-rc-scripts
Prereq:		/sbin/chkconfig

%description rc-scripts
rc-scripts for ATM support.

%description rc-scripts -l pl
Skrypty startowe dla wsparcia obs≥ugi ATM.

%prep
%setup -q -a1
install -m644 %{SOURCE2} .
%patch0 -p1
#%patch1 -p1

%build
autoconf
%configure \
	--sysconfdir=%{_sysconfdir}/atm \
	--enable-cisco \
	--enable-mpoa_1_1

%{__make}

pwd
gcc $RPM_OPT_FLAGS -I./src/include pppbr-001212-br2684ctl.c \
	-o br2684ctl -lresolv -L./src/lib/.libs -latm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{atm,sysconfig/{interfaces,network-scripts},rc.d/init.d} \
	$RPM_BUILD_ROOT/var/log/atm

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install br2684ctl $RPM_BUILD_ROOT%{_sbindir}

install src/config/hosts.atm $RPM_BUILD_ROOT%{_sysconfdir}
install src/extra/ANS/e164_cc $RPM_BUILD_ROOT%{_sysconfdir}

install pld/atm/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/atm/
install pld/init.d/atm $RPM_BUILD_ROOT/etc/rc.d/init.d/
install pld/sysconfig/atm $RPM_BUILD_ROOT/etc/sysconfig/
install pld/network-scripts/{ifup-*,ifdown-*} \
		$RPM_BUILD_ROOT/etc/sysconfig/network-scripts
 
gzip -9nf doc/README.* doc/atm-linux-howto.txt \
	BUGS AUTHORS ChangeLog README THANKS \
	pld/README.PLD pld/interfaces/ifcfg-*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post rc-scripts
/sbin/chkconfig --add atm
if [ -f /var/lock/subsys/atm ]; then
	/etc/rc.d/init.d/atm restart 1>&2
fi

%preun rc-scripts
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/atm ]; then
		/etc/rc.d/init.d/atm stop 1>&2
	fi
	/sbin/chkconfig --del atm
fi

%files
%defattr(644,root,root,755)
%doc doc/*.gz *.gz
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/hosts.atm
%attr(750,root,root) %dir %{_sysconfdir}/atm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/atm/*
%config %{_sysconfdir}/e164_cc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(751,root,root) /var/log/atm
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files rc-scripts
%defattr(644,root,root,755)
%doc pld/README.PLD.gz pld/interfaces/ifcfg-*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sysconfig/atm
%attr(755,root,root) %{_sysconfdir}/sysconfig/network-scripts/*
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/atm
