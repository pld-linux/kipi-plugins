#
%define	_beta	beta3

Summary:	Library KIPI plugins
Summary(pl.UTF-8):	Wtyczki dla biblioteki KIPI
Name:		kipi-plugins
Version:	0.2.0
Release:	0.%{_beta}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	c9d6daa55c55966b93347311e87804dd
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	automoc4
BuildRequires:	exiv2-devel >= 0.12
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	imlib2-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libkdcraw-devel >= 0.2.0
BuildRequires:	libkexiv2-devel >= 0.2.0
BuildRequires:	libkipi-devel >= 0.2.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.4.3
BuildRequires:	qt4-qmake >= 4.4.3
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

install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/xx

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/kde4/*.so
%attr(755,root,root) %{_libdir}/libkipiplugins.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkipiplugins.so.1
%{_datadir}/apps/kipiplugin_galleryexport
%{_datadir}/apps/kipiplugin_htmlexport
%{_datadir}/apps/kipiplugin_imageviewer
%{_datadir}/apps/kipiplugin_metadataedit
%{_datadir}/apps/kipiplugin_simpleviewerexport
%{_datadir}/apps/kipiplugin_slideshow
%{_datadir}/kde4/services/kipiplugin_*.desktop
%{_iconsdir}/hicolor/*/*
