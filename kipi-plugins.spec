#
%define		qtver	4.4.3

Summary:	Library KIPI plugins
Summary(pl.UTF-8):	Wtyczki dla biblioteki KIPI
Name:		kipi-plugins
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
# Source0-md5:	2049c37dd1bff8f818e379d3c7676389
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	exiv2-devel >= 0.12
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdegraphics-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libgpod-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	libxslt-devel
BuildRequires:	opencv-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sane-backends-devel
# because of current K_PATH_X definition
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library KIPI plugins.

%description -l pl.UTF-8
Wtyczki dla biblioteki KIPI.

%prep
%setup -q

%build
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

%find_lang kipiplugin --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kipiplugin.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/dngconverter
%attr(755,root,root) %{_bindir}/scangui
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_acquireimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_advancedslideshow.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_batchprocessimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_calendar.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_dngconverter.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_facebook.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_flashexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_flickrexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_galleryexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_gpssync.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_htmlexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_imageviewer.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_ipodexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_jpeglossless.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_kioexportimport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_metadataedit.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_picasawebexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_printimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_rawconverter.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_removeredeyes.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_sendimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_smug.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_timeadjust.so
%attr(755,root,root) %{_libdir}/libkipiplugins.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkipiplugins.so.1
#%{_datadir}/apps/kipiplugin_advancedslideshow
%{_datadir}/apps/kipiplugin_facebook
%{_datadir}/apps/kipiplugin_flashexport
%{_datadir}/apps/kipiplugin_flickrexport
%{_datadir}/apps/kipiplugin_galleryexport
%{_datadir}/apps/kipiplugin_htmlexport
%{_datadir}/apps/kipiplugin_imageviewer
%{_datadir}/apps/kipiplugin_metadataedit
%{_datadir}/apps/kipiplugin_picasawebexport
%{_datadir}/apps/kipiplugin_printimages
%{_datadir}/apps/kipiplugin_removeredeyes
%{_datadir}/apps/kipiplugin_smug
%{_datadir}/kde4/services/kipiplugin_*.desktop
%{_desktopdir}/kde4/dngconverter.desktop
%{_desktopdir}/kde4/kipiplugins.desktop
%{_desktopdir}/kde4/scangui.desktop
%{_iconsdir}/hicolor/*/actions/*
%{_iconsdir}/oxygen/*/apps/*
