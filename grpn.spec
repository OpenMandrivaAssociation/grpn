%define name grpn
%define version 1.1.2
%define release 5mdk

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

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/grpn"\
title="Grpn"\
longtitle="A RPN calculator"\
needs="x11"\
icon="mathematics_section.png"\
section="Applications/Sciences/Mathematics"
EOF


%clean
rm -rf $RPM_BUILD_ROOT 

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr (-,root,root)
%doc CHANGES LICENSE README
%{_bindir}/*
%{_menudir}/*

