Summary:	The best looking theme for Mozilla
Summary(pl):	Najlepszy temat dla Mozilli jaki kiedykolwiek powsta³
Name:		mozilla-theme-orbit
%define		_realname	morbit
Version:	0.0.4.2
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.alfordot.com/e/p/cdn/orbit3/%{_realname}-1_0-20020611.jar
Source1:	%{_realname}-installed-chrome.txt
URL:		http://morbit.cdn.gs/
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
The best looking theme for Mozilla.

%description -l pl
Najlepszy temat dla Mozilli jaki kiedykolwiek powsta³.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

mv -f $RPM_BUILD_ROOT%{_chromedir}/morbit-1_0-20020611.jar \
	$RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar

%post 
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
