%define	name		dispcalGUI
%define	version		1.1.2.9
%define release		1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A graphical user interface for the Argyll CMS display calibration utilities
Group: 		Graphics
License:	GPLv3
URL:		http://dispcalGUI.hoech.net
Source0:	%{name}.tar.gz
Requires:	wxPythonGTK argyllcms
BuildRequires:	python-setuptools wxPythonGTK python-devel
BuildRequires:	wxPythonGTK-wxversion
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
Requires:	python-setuptools
Requires:	wxPythonGTK-wxversion

%description
A graphical user interface for the Argyll CMS display calibration utilities

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build 

%install
python setup.py install --prefix=/usr  --root=%{buildroot}

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/udev/rules.d/55-Argyll.rules
%{_mandir}/man1/*.xz
%{_iconsdir}/hicolor/*/*
#% {_docdir}/%{name}-%{version}/screenshots/
#% {_docdir}/%{name}-%{version}/theme
%{_docdir}/%{name}-%{version}/

%{py_platsitedir}/%{name}
%{py_platsitedir}/*egg*

%{_datadir}/applications/dispcalGUI.desktop
%{_sysconfdir}/xdg/autostart/z-dispcalGUI-apply-profiles.desktop
