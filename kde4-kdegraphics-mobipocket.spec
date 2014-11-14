%define		_state		stable
%define		orgname		kdegraphics-mobipocket
%define		qtver		4.8.1

Summary:	K Desktop Environment - Mobipocket support for Okular
Summary(pl.UTF-8):	K Desktop Environment - Wsparcie formatu mobipocket dla Okulara
Name:		kde4-kdegraphics-mobipocket
Version:	4.14.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	1b89a50b355293a9dd7ce654709e7d09
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	strigi-devel
Obsoletes:	mobipocket <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mobipocket support for Okular.

%description -l pl.UTF-8
Wsparcie formatu mobipocket dla Okulara.

%package devel
Summary:	Development files for kdegraphics-mobipocket
Summary(pl.UTF-8):	Pliki przydatne twórcom gier dla kdegraphics-mobipocket
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
Development files for kde4-kdegraphics-mobipocket.

%description devel -l pl.UTF-8
kde4-kdegraphics-mobipocket - pliki dla programistów.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/mobithumbnail.so
%attr(755,root,root) %ghost %{_libdir}/libqmobipocket.so.?
%attr(755,root,root) %{_libdir}/libqmobipocket.so.*.*.*
%attr(755,root,root) %{_libdir}/strigi/strigila_mobi.so
%{_datadir}/kde4/services/mobithumbnail.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/qmobipocket
%{_libdir}/cmake/QMobipocket
%attr(755,root,root) %{_libdir}/libqmobipocket.so
