Summary:	A graphical user interface for the Argyll CMS display calibration utilities
Name:		dispcalGUI
Version:	1.7.5.7
Release:	2
License:	GPLv3+
Group: 		Graphics
Url:		https://dispcalGUI.hoech.net
Source0:	http://sourceforge.net/projects/dispcalgui/files/release/%{version}/%{name}-%{version}.tar.gz
Patch0:		dispcalGUI-1.7.5.7-rpmbuild.patch
BuildRequires:	python-setuptools
BuildRequires:	wxPythonGTK
BuildRequires:	wxPythonGTK-wxversion
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xxf86vm)
Requires:	argyllcms
Requires:	python-setuptools
Requires:	wxPythonGTK
Requires:	wxPythonGTK-wxversion

%description
A graphical user interface for the Argyll CMS display calibration utilities.

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/dispcalGUI*.desktop
%{_mandir}/man1/*.xz
%{_iconsdir}/hicolor/*/*
%{py_platsitedir}/%{name}
%{py_platsitedir}/*egg*
%{_sysconfdir}/xdg/autostart/z-dispcalGUI-apply-profiles.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
python setup.py install --prefix=/usr --root=%{buildroot}


