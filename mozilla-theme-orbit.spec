Summary:        The best looking theme for mozilla
Summary(pl):    Najlepszy temat dla mozilli jaki kiedykolwiek powsta³.
Name:           mozilla-theme-orbit
Version:        0.0.4.2
Release:        1
License:        GPL
Group:          X11/Applications/Networking
Source0:	http://www.alfordot.com/e/p/cdn/orbit3/morbit-1_0-20020611.jar
Source1:        morbit-installed-chrome.txt
URL:            http://morbit.cdn.gs/
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	morbit

%description
%description -l pl
Najlepszy temat dla mozilli jaki kiedykolwiek powsta³.

%prep
%setup -q -c -T
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}
mv $RPM_BUILD_ROOT%{_chromedir}/morbit-1_0-20020611.jar $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "%{_realname}.jar" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
