Summary:	RFC 2217 Serial Communications Daemon
Summary(pl.UTF-8):	Demon do komunikacji szeregowej zgodny z RFC 2217
Name:		sercd
Version:	3.0.0
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/sercd/%{name}-%{version}.tar.gz
# Source0-md5:	3ad41d9e8fa28e12f96652fdd4db30b0
Source1:	%{name}.inetd
URL:		http://sercd.sourceforge.net/
Requires:	rc-inetd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sercd is a serial port redirector that is compliant with the RFC 2217
"Telnet Com Port Control Option" protocol. This protocol lets you
share a serial port through the network.

%description -l pl.UTF-8
sercd to narzędzie do przekierowywania portów szeregowych zgodne z
protokołem RFC 2217 "Telnet Com Port Control Option". Protokół ten
pozwala na współdzielenie portu szeregowego przez sieć.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q rc-inetd reload

%postun
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_sbindir}/sercd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/%{name}
%{_mandir}/man8/sercd.8*
