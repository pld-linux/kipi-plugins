#
%define		_beta	rc2
%define		qtver	4.4.3

Summary:	Library KIPI plugins
Summary(pl.UTF-8):	Wtyczki dla biblioteki KIPI
Name:		kipi-plugins
Version:	0.2.0
Release:	0.%{_beta}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	e853a7929749e69f59e5c7bc9cdd8598
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	exiv2-devel >= 0.12
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdegraphics-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
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

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/dngconverter
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_acquireimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_advancedslideshow.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_calendar.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_dngconverter.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_fb.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_flickrexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_galleryexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_gpssync.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_htmlexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_imageviewer.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_ipodexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_jpeglossless.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_metadataedit.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_picasawebexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_printwizard.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_rawconverter.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_sendimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_simpleviewer.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_smug.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_timeadjust.so
%attr(755,root,root) %{_libdir}/libkipiplugins.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkipiplugins.so.1
%{_datadir}/apps/kipiplugin_advancedslideshow
%{_datadir}/apps/kipiplugin_galleryexport
%{_datadir}/apps/kipiplugin_htmlexport
%{_datadir}/apps/kipiplugin_imageviewer
%{_datadir}/apps/kipiplugin_metadataedit
%{_datadir}/apps/kipiplugin_simpleviewerexport
%{_datadir}/kde4/services/kipiplugin_*.desktop
%{_desktopdir}/kde4/dngconverter.desktop
%{_iconsdir}/hicolor/*/*
