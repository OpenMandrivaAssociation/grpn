Name: 		grpn
Version: 	1.1.2
Release: 	10
License: 	GPL
Summary: 	RPN calculator for X built using the GIMP Toolkit
URL: 		http://lashwhip.com/grpn.html
Group: 		Sciences/Mathematics
Source: 	%{name}-%{version}.tar.bz2
BuildRequires: gtk+-devel

%description 
GRPN Version 1.0, By Paul Wilkins

GRPN is a RPN calculator for the X Window system built using the GIMP
Toolkit (GTK).  GRPN works with real numbers, complex numbers,
matrices, and complex matrices.  Numbers can be displayed in 4
different radix modes, and complex numbers can be displayed in either
Cartesian or polar form.  


%prep

%setup -q

%build

%make

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 grpn %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/grpn
Name=Grpn
Comment=A RPN calculator
Icon=mathematics_section
Categories=Science;Math;
EOF


%files
%doc CHANGES LICENSE README
%{_bindir}/*
%{_datadir}/applications/mandriva-*.desktop



