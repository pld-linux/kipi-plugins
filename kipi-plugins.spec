
%define _beta	beta1

Summary:	Library KIPI plugins
Summary(pl):	Wtyczki dla biblioteki KIPI
Name:		kipi-plugins
Version:	0.1
Release:	0.%{_beta}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/digikam/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	024785a86202f45116a0439232933545
URL:		http://digikam.sourceforge.net/
BuildRequires:	libkipi-devel >= 0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library KIPI plugins.

%description -l pl
Wtyczki dla biblioteki KIPI.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

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
