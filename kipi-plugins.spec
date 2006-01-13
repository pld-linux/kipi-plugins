
%define _beta	beta2

Summary:	Library KIPI plugins
Summary(pl):	Wtyczki dla biblioteki KIPI
Name:		kipi-plugins
Version:	0.1.0
Release:	0.%{_beta}.5
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/digikam/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	1dd0cb05e0c7da43861d2bf0affaa4b3
URL:		http://digikam.sourceforge.net/
BuildRequires:	X11-devel
BuildRequires:	gettext-devel
BuildRequires:	imlib2-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libexif-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libkexif-devel
BuildRequires:	libkipi-devel >= 0.1
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library KIPI plugins.

%description -l pl
Wtyczki dla biblioteki KIPI.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
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

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang 
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/*
%{_datadir}/services/*
%{_mandir}/man1/*
