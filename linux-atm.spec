# $Revision: 1.1 $ $Date: 2001-10-28 01:43:47 $
Summary:	ATM on Linux
Summary(pl):	Obs³uga sieci ATM w Linuxie
Name:		linux-atm
Version:	2.4.0
Release:	1
License:	GPL
Group:		Networking
Group(de):	Netzwerkwesen
Group(pl):	Sieciowe
URL:		http://ica1www.epfl.ch/linux-atm/
Source0:	http://prdownloads.sourceforge.net/linux-atm/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-pldrc.tar.gz
Source2:	http://home.sch.bme.hu/~cell/br2684/dist/001212/pppbr-001212-br2684ctl.c
Patch0:		%{name}-syslog.patch
Patch1:		%{name}-br2684ctl-syslog.patch
Icon:		%{name}-logo.gif
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
Obs³uga sieci ATM (Asynchronous Transfer Mode) w Linuxie mimo i¿ jest
jeszcze w stadium alfa dzia³a ju¿ bardzo stabilnie i
najproawdopodobniej zostanie w³±czona do j±der serii 2.4.x. W Linuxie
PLD sk³ada siê ona z ³at (patches) do bie¿±cej wersji j±dra
zawieraj±cych sterowniki do kilku popularnych kart (m.in Fore, Madge,
IDT) i zapewniaj±cych zestawianie po³±czeñ PVC i SVC oraz zestawu
programów i skryptów (ten pakiet) realizuj±cych najpopularniejsze
us³ugi ATM, tj. Classical IP (IP over ATM), klientów i serwery LAN
Emulation (LANE), Multiprotocol Over ATM (MPOA) i inne rozmaito¶ci.

%package devel
Summary:	ATM on Linux - developer's package
Summary(pl):	Obs³uga sieci ATM w Linuxie - biblioteki i pliki nag³ówkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Obsoletes:	atm-devel
Requires:	%{name} = %{version}

%description devel
Libraries and header files needed for development ATM applications for
Linux.

%description -l pl devel
Biblioteki i pliki nag³ówkowe niezbêdne do opracowywania aplikacji ATM
dla Linuxa.

%package static
Summary:	ATM on Linux - static libraries
Summary(pl):	Obs³uga sieci ATM w Linuxie - biblioteki statyczne
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Obsoletes:	atm-static
Requires:	%{name}-devel = %{version}

%description static
Static libraries needed for development ATM applications for Linux.

%description -l pl static
Biblioteki statyczne niezbêdne do opracowywania aplikacji ATM
dla Linuxa.

%package rc-scripts
Summary:        ATM on Linux - rc-scripts
Summary(pl):    Obs³uga sieci ATM w Linuxie - skrypty startowe
Group:          Base
Requires:       %{name} = %{version}
Requires:	rc-scripts >= 0.2.9
Obsoletes:	atm-rc-scripts
Prereq:		/sbin/chkconfig

%description rc-scripts
rc-scripts for ATM support.

%description -l pl rc-scripts
Skrypty startowe dla wsparcia obs³ugi ATM.

%prep
%setup -q -a1
install -m644 %{SOURCE2} .
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure \
	--sysconfdir=/etc/atm \
	--enable-cisco \
	--enable-mpoa_1_1

%{__make}

gcc $RPM_OPT_FLAGS -I./lib pppbr-001212-br2684ctl.c -o br2684ctl -lresolv -L./lib -latm

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
