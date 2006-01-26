# $Revision: 1.35 $ $Date: 2006-01-26 13:26:25 $
#
# TODO:
#		- split to libatm-*, atm-init and atm-progs.
#		- fix:
#i686-pld-linux-gcc -I../.. -DHAVE_CONFIG_H -I../.. -I../../src/include -O2 -march=i686
#-mtune=pentium4  -pipe -Wall -Wshadow -Wpointer-arith -Wwrite-strings -Wstrict-prototypes -c qd.dump.c
#i686-pld-linux-gcc -E -I../.. -DHAVE_CONFIG_H - <msg.fmt | ./qgen
#<stdin>:93:1: error: pasting "}" and "fw_pcr_0" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "bw_pcr_0" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "fw_pcr_01" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "bw_pcr_01" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "fw_scr_0" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "bw_scr_0" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "fw_scr_01" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "bw_scr_01" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "fw_mbs_0" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "bw_mbs_0" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "fw_mbs_01" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "bw_mbs_01" does not give a valid preprocessing token
#<stdin>:93:1: error: pasting "}" and "best_effort" does not give a valid preprocessing token
#<stdin>:138:3: error: invalid preprocessing directive #Note
#<stdin>:139:9: error: invalid preprocessing directive #to
#  229 groups, 213 fields (26 var-len), construction area is 1069 bytes,
#    3490 words in constructor, 3244 words in parser.
#
# Conditional build:
%bcond_without	vbr	# without VBR (which needs ATM/VBR kernel patch)
#
Summary:	ATM on Linux
Summary(pl):	Obs³uga sieci ATM w Linuksie
Name:		linux-atm
Version:	2.4.1
Release:	3
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/linux-atm/%{name}-%{version}.tar.gz
# Source0-md5:	84fef49cc39ff2605204246666f65864
Source1:	%{name}-2.4.0.1-pldrc.tar.gz
# Source1-md5:	c76c7dbac5797db883b2b22687243839
Source2:	http://home.sch.bme.hu/~cell/br2684/dist/001212/pppbr-001212-br2684ctl.c
Patch0:		%{name}-syslog.patch
Patch1:		%{name}-br2684ctl-syslog.patch
Patch2:		%{name}-include.patch
Patch3:		ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-%{name}-diffs
Patch4:		%{name}-llh-vbr.patch
Patch5:		%{name}-gcc4.patch
URL:		http://linux-atm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
Conflicts:	kernel-headers < 2.4
Obsoletes:	atm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ATM (Asynchronous Transfer Mode) networking for Linux is still under
development now but it works quite stable now and has been already
included in 2.4.x series kernels. In PLD Linux it consists of some
patches for current kernel version containing drivers for a few
popular ATM cards (ex. Fore, Madge, IDT) and PVC and SVC support. It
also includes programs and scripts providing the most popular ATM
services, i.e. Classical IP (IP over ATM), LAN Emulation clients and
servers, Multiprotocol Over ATM (MPOA) and some other goodies.

%description -l pl
Obs³uga sieci ATM (Asynchronous Transfer Mode) w Linuksie, mimo i¿
jest nadal rozwijana, dzia³a ju¿ bardzo stabilnie i zosta³a ju¿
w³±czona do j±der serii 2.4.x. W Linuksie PLD sk³ada siê ona z ³at
(patches) do bie¿±cej wersji j±dra zawieraj±cych sterowniki do kilku
popularnych kart (m.in Fore, Madge, IDT) i zapewniaj±cych zestawianie
po³±czeñ PVC i SVC oraz zestawu programów i skryptów (ten pakiet)
realizuj±cych najpopularniejsze us³ugi ATM, tj. Classical IP (IP over
ATM), klientów i serwery LAN Emulation (LANE), Multiprotocol Over ATM
(MPOA) i inne rozmaito¶ci.

%package devel
Summary:	ATM on Linux - developer's package
Summary(pl):	Obs³uga sieci ATM w Linuksie - biblioteki i pliki nag³ówkowe
Group:		Development/Libraries
Obsoletes:	atm-devel
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and header files needed for development ATM applications for
Linux.

%description devel -l pl
Biblioteki i pliki nag³ówkowe niezbêdne do opracowywania aplikacji ATM
dla Linuksa.

%package static
Summary:	ATM on Linux - static libraries
Summary(pl):	Obs³uga sieci ATM w Linuksie - biblioteki statyczne
Group:		Development/Libraries
Obsoletes:	atm-static
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries needed for development ATM applications for Linux.

%description static -l pl
Biblioteki statyczne niezbêdne do opracowywania aplikacji ATM dla
Linuksa.

%package rc-scripts
Summary:	ATM on Linux - rc-scripts
Summary(pl):	Obs³uga sieci ATM w Linuksie - skrypty startowe
Group:		Base
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts >= 0.2.9
Obsoletes:	atm-rc-scripts

%description rc-scripts
rc-scripts for ATM support.

%description rc-scripts -l pl
Skrypty startowe dla wsparcia obs³ugi ATM.

%prep
%setup -q -a1
install -m644 %{SOURCE2} .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if %{with vbr}
%patch3 -p1
%patch4 -p1
%endif
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--sysconfdir=%{_sysconfdir}/atm \
	--enable-cisco \
	--enable-mpoa_1_1

%{__make}

pwd
%{__cc} %{rpmcflags} %{rpmldflags} -Isrc/include pppbr-001212-br2684ctl.c \
	-o br2684ctl -lresolv -Lsrc/lib/.libs -latm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{atm,sysconfig/{interfaces,network-scripts},rc.d/init.d} \
	$RPM_BUILD_ROOT/var/log/atm

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install br2684ctl $RPM_BUILD_ROOT%{_sbindir}

install src/config/hosts.atm $RPM_BUILD_ROOT%{_sysconfdir}
install src/extra/ANS/e164_cc $RPM_BUILD_ROOT%{_sysconfdir}

install pld/atm/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/atm
install pld/init.d/atm $RPM_BUILD_ROOT/etc/rc.d/init.d
install pld/sysconfig/atm $RPM_BUILD_ROOT/etc/sysconfig
install pld/network-scripts/{ifup-*,ifdown-*} \
		$RPM_BUILD_ROOT/etc/sysconfig/network-scripts

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
%doc doc/README.* doc/atm-linux-howto.txt AUTHORS BUGS ChangeLog README THANKS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hosts.atm
%attr(750,root,root) %dir %{_sysconfdir}/atm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/atm/*
%config %{_sysconfdir}/e164_cc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(751,root,root) /var/log/atm
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files rc-scripts
%defattr(644,root,root,755)
%doc pld/README.PLD pld/interfaces/ifcfg-*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/atm
%attr(755,root,root) /etc/sysconfig/network-scripts/*
%attr(754,root,root) /etc/rc.d/init.d/atm
