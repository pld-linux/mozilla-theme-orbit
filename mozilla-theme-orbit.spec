Summary:	The best looking theme for Mozilla
Summary(pl):	Najlepszy motyw dla Mozilli jaki kiedykolwiek powsta³
Name:		mozilla-theme-orbit
%define		_realname	morbit
%define	fver	1_3-20030519
Version:	0.0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.uk1.mozdev.org/rsync/themes/themes/%{_realname}-%{fver}.jar
# Source0-md5:	da1c5879f4fb3b6e976d5f0094cb1de0
Source1:	%{_realname}-installed-chrome.txt
URL:		http://morbit.cdn.gs/
Requires(post,postun):	textutils
Requires:	mozilla >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
The best looking theme for Mozilla.

%description -l pl
Najlepszy motyw dla Mozilli jaki kiedykolwiek powsta³.

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
