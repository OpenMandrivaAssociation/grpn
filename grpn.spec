%define name grpn
%define version 1.1.2
%define release  %mkrel 8

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Summary: 	RPN calculator for X built using the GIMP Toolkit
URL: 		http://lashwhip.com/grpn.html
Group: 		Sciences/Mathematics
Source: 	%{name}-%{version}.tar.bz2
BuildRequires: gtk+-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description 
GRPN Version 1.0, By Paul Wilkins

GRPN is a RPN calculator for the X Window system built using the GIMP
Toolkit (GTK).  GRPN works with real numbers, complex numbers,
matrices, and complex matrices.  Numbers can be displayed in 4
different radix modes, and complex numbers can be displayed in either
Cartesian or polar form.  


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%make

%install
install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 grpn $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application <<EOF
Exec=%{_bindir}/grpn
Name=Grpn
Comment=A RPN calculator
Icon=mathematics_section
Categories=Science;Math;
EOF


%clean
rm -rf $RPM_BUILD_ROOT 

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr (-,root,root)
%doc CHANGES LICENSE README
%{_bindir}/*
%{_datadir}/applications/mandriva-*.desktop

