Summary:	The best looking theme for Mozilla
Summary(pl.UTF-8):	Najlepszy motyw dla Mozilli jaki kiedykolwiek powstał
Name:		mozilla-theme-orbit
%define		_realname	orbit
Version:	1.7
%define	fver	1_7-MiK
Release:	1
Epoch:		5
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/1_7/%{_realname}-%{fver}.jar 
# Source0-md5:	9becd58f71da9c501c252dd705f7f58a
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www.miksworld.de/
Requires(post,postun):	textutils
Requires:	mozilla >= 5:1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
The best looking theme for Mozilla.

%description -l pl.UTF-8
Najlepszy motyw dla Mozilli jaki kiedykolwiek powstał.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
