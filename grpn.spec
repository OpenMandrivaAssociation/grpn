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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.2-8mdv2010.0
+ Revision: 429323
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1.2-7mdv2009.0
+ Revision: 246643
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.1.2-5mdv2008.1
+ Revision: 131682
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import grpn


* Wed May 10 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1.2-5mdk
- Fix build on x86-64

* Tue Jan 10 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1.2-4mdk
- rebuild

* Mon Aug 16 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.1.2-3mdk
- Rebuild

* Fri Jul 18 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 1.1.2-2mdk
- Rebuild

* Mon Apr 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.2-1mdk
- 1.1.2

* Sat Jan 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.1-5mdk
- Fix menu entry

* Tue Jul 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-4mdk
- s/Copyright/License/g

* Mon Jun 18 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.1.1-3mdk
- New office menu structure

* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-2mdk
- rebuild

* Mon Sep 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-1mdk
- menus
- macros
- BM
- v1.1.1

* Thu Apr 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-2mdk
- fix group

* Thu Feb 24 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build 

* Mon Jun 21 1999 Tom Faska <tom@ubertas.com>
- Initial RPM for grpn-1.1.0
