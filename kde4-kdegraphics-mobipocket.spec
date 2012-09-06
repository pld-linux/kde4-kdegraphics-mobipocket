%define		_state		stable
%define		orgname		kdegraphics-mobipocket
%define		qtver		4.8.1

Summary:	K Desktop Environment - Mobipocket support for Okular
Summary(pl.UTF-8):	K Desktop Environment - Wsparcie formatu mobipocket dla Okulara
Name:		kde4-kdegraphics-mobipocket
Version:	4.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d6034168af396566d1cdc8c2cec9275e
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-okular-devel >= %{version}
BuildRequires:	strigi-devel
Obsoletes:	mobipocket <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mobipocket support for Okular.

%description -l pl.UTF-8
Wsparcie formatu mobipocket dla Okulara.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/mobithumbnail.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_mobi.so
%attr(755,root,root) %{_libdir}/strigi/strigila_mobi.so
%{_desktopdir}/kde4/okularApplication_mobi.desktop
%{_datadir}/kde4/services/libokularGenerator_mobi.desktop
%{_datadir}/kde4/services/mobithumbnail.desktop
%{_datadir}/kde4/services/okularMobi.desktop
