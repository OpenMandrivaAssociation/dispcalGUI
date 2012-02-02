%define	name		dispcalGUI
%define	version		0.8.5.2
%define release		1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A graphical user interface for the Argyll CMS display calibration utilities
Group: 		Graphics
License:	GPLv3
URL:		http://dispcalGUI.hoech.net
Source:		%{name}.tar.gz
Requires:	wxPythonGTK argyllcms
BuildRequires:	python-setuptools wxPythonGTK libpython-devel
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

%post
#!/bin/sh

if [ `whoami` = "root" ]; then
	prefix=/usr
else
	prefix="$HOME/.local"
fi

opts=`getopt --long prefix: -- "$0" "$@"`
eval set -- "$opts"
while true ; do
	case "$1" in
		--prefix)
			shift;
			prefix="$1";
			shift;;
		--)
			shift;
			break;;
		*)
			shift;;
	esac
done

if [ `whoami` = "root" ]; then
	XDG_DATA_DIRS="$prefix/share/:${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}"
fi

echo "Installing icon resources..."
for size in 16 22 24 32 48 256 ; do
	xdg-icon-resource install --noupdate --novendor --size $size "$prefix/share/dispcalGUI/theme/icons/${size}x${size}/dispcalGUI.png"
done
xdg-icon-resource forceupdate

echo "Installing desktop menu entry..."
xdg-desktop-menu install --novendor "$prefix/share/dispcalGUI/dispcalGUI.desktop"

echo "...done"


%postun
#!/bin/sh

if [ `whoami` = "root" ]; then
	prefix=/usr
else
	prefix="$HOME/.local"
fi

opts=`getopt --long prefix: -- "$0" "$@"`
eval set -- "$opts"
while true ; do
	case "$1" in
		--prefix)
			shift;
			prefix="$1";
			shift;;
		--)
			shift;
			break;;
		*)
			shift;;
	esac
done

if [ `whoami` = "root" ]; then
	XDG_DATA_DIRS="$prefix/share/:${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}"
fi

echo "Uninstalling desktop menu entry..."
xdg-desktop-menu uninstall "$prefix/share/applications/dispcalGUI.desktop"

echo "Uninstalling icon resources..."
for size in 16 22 24 32 48 256 ; do
	xdg-icon-resource uninstall --noupdate --size $size dispcalGUI
done
xdg-icon-resource forceupdate

echo "...done"


%files
%{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/udev/rules.d/92-Argyll.rules
%{_mandir}/man1/*.xz
%{_iconsdir}/hicolor/*/*
%{_docdir}/%{name}-%{version}

%{py_platsitedir}/%{name}
%{py_platsitedir}/*egg*

%{_datadir}/applications/dispcalGUI.desktop
%{_sysconfdir}/xdg/autostart/z-dispcalGUI-apply-profiles.desktop
