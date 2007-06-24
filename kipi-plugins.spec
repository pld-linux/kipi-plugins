
%define		_beta	beta2

Summary:	Library KIPI plugins
Summary(pl.UTF-8):	Wtyczki dla biblioteki KIPI
Name:		kipi-plugins
Version:	0.1.4
Release:	0.%{_beta}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	073484de3cf98083c4b2da6eb0602cb7
Patch0:		kde-ac260-lt.patch
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	exiv2-devel >= 0.14
BuildRequires:	gettext-devel
BuildRequires:	imlib2-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libexif-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libkexif-devel >= 0.2.5
BuildRequires:	libkipi-devel >= 0.1.5
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
# because of current K_PATH_X definition
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library KIPI plugins.

%description -l pl.UTF-8
Wtyczki dla biblioteki KIPI.

%prep
%setup -q -n %{name}-%{version}-%{_beta}
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/xx
rm $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde3/*.so
%attr(755,root,root) %{_libdir}/libkipiplugins.so.*.*.*
%{_datadir}/apps/*
%{_datadir}/services/*
%{_datadir}/config.kcfg/htmlexportconfig.kcfg
%{_mandir}/man1/*
