Summary:	The best looking theme for Mozilla
Summary(pl):	Najlepszy motyw dla Mozilli jaki kiedykolwiek powsta³
Name:		mozilla-theme-orbit
%define		_realname	morbit
%define	fver	1_5-MiK
Version:	0.0.7.1
Release:	2
Epoch:		5
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/morbit-1_5-MiK.jar 
# Source0-md5:	5d665b5ab68deca1a2f559c6a2ed0ee6
Source1:	%{_realname}-installed-chrome.txt
URL:		http://morbit.cdn.gs/
Requires(post,postun):	textutils
Requires:	mozilla = 5:1.5
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
