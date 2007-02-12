# TODO: make rc-inetd config file (based on included sercd.xinetd)
Summary:	RFC 2217 Serial Communications Daemon
Summary(pl.UTF-8):	Demon do komunikacji szeregowej zgodny z RFC 2217
Name:		sercd
Version:	2.3.2
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.lysator.liu.se/~astrand/projects/sercd/%{name}-%{version}.tar.gz
# Source0-md5:	092487939c22fc4c6c42a41cda25658f
URL:		http://www.lysator.liu.se/~astrand/projects/sercd/
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_sbindir}/sercd
%{_mandir}/man8/sercd.8*
