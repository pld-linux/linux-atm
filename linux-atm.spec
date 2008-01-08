# $Revision: 1.43 $ $Date: 2008-01-08 19:08:48 $
#
# TODO:
#		- split to libatm-*, atm-init and atm-progs.
#
# Conditional build:
%bcond_without	oam	# without OAM (which needs ATM/OAM kernel patch)
%bcond_without	vbr	# without VBR (which needs ATM/VBR kernel patch)
#
Summary:	ATM on Linux
Summary(pl.UTF-8):	Obsługa sieci ATM w Linuksie
Name:		linux-atm
Version:	2.5.0
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/linux-atm/%{name}-%{version}.tar.gz
# Source0-md5:	0b45a0e801fac7093ce4b0cadf419965
Source1:	%{name}-2.4.0.1-pldrc.tar.gz
# Source1-md5:	c76c7dbac5797db883b2b22687243839
Patch0:		%{name}-syslog.patch
Patch1:		ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-%{name}-diffs
Patch2:		%{name}-llh-vbr.patch
URL:		http://linux-atm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.268
Obsoletes:	atm
Conflicts:	kernel-headers < 2.4
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

%description -l pl.UTF-8
Obsługa sieci ATM (Asynchronous Transfer Mode) w Linuksie, mimo iż
jest nadal rozwijana, działa już bardzo stabilnie i została już
włączona do jąder serii 2.4.x. W Linuksie PLD składa się ona z łat
(patches) do bieżącej wersji jądra zawierających sterowniki do kilku
popularnych kart (m.in Fore, Madge, IDT) i zapewniających zestawianie
połączeń PVC i SVC oraz zestawu programów i skryptów (ten pakiet)
realizujących najpopularniejsze usługi ATM, tj. Classical IP (IP over
ATM), klientów i serwery LAN Emulation (LANE), Multiprotocol Over ATM
(MPOA) i inne rozmaitości.

%package devel
Summary:	ATM on Linux - developer's package
Summary(pl.UTF-8):	Obsługa sieci ATM w Linuksie - biblioteki i pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	atm-devel

%description devel
Libraries and header files needed for development ATM applications for
Linux.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe niezbędne do opracowywania aplikacji ATM
dla Linuksa.

%package static
Summary:	ATM on Linux - static libraries
Summary(pl.UTF-8):	Obsługa sieci ATM w Linuksie - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	atm-static

%description static
Static libraries needed for development ATM applications for Linux.

%description static -l pl.UTF-8
Biblioteki statyczne niezbędne do opracowywania aplikacji ATM dla
Linuksa.

%package rc-scripts
Summary:	ATM on Linux - rc-scripts
Summary(pl.UTF-8):	Obsługa sieci ATM w Linuksie - skrypty startowe
Group:		Base
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts >= 0.2.9
Obsoletes:	atm-rc-scripts

%description rc-scripts
rc-scripts for ATM support.

%description rc-scripts -l pl.UTF-8
Skrypty startowe dla wsparcia obsługi ATM.

%prep
%setup -q -a1
%patch0 -p1
%if %{with vbr}
%patch1 -p1
%patch2 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--sysconfdir=%{_sysconfdir}/atm \
	--enable-cisco \
	--enable-mpoa_1_1 \
	--enable-multipoint

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{atm,sysconfig/{interfaces,network-scripts},rc.d/init.d} \
	$RPM_BUILD_ROOT/var/log/atm

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%service atm restart

%preun rc-scripts
if [ "$1" = "0" ]; then
	%service atm stop
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
