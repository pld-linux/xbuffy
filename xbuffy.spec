Summary:	XBiff-type program. With XBuffy you can watch multiple mailboxes
Summary(pl):	Program typu xbiff. Potrafi monitorowaæ jednocze¶nie kilka skrzynek pocztowych
Name:		xbuffy
Version:	3.3.bl.3
Release:	2
License:	Free
Group:		X11/Amusements
Source0:	http://www.fiction.net/blong/programs/xbuffy/%{name}-%{version}.tar.gz
# Source0-md5:	f4de2adc9d0b2327040e700e2fd25a42
Source1:	http://www.fiction.net/blong/programs/xbuffy/%{name}-%{version}.readme
# Source1-md5:	ab3857614cb235aeb8937ca46f3417ea
Patch0:	%{name}-rfc2047.patch
URL:		http://www.fiction.net/blong/programs/#xbuffy
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix		/usr/X11R6
%define	_bindir		%{_prefix}/bin
%define	_mandir		%{_prefix}/man

%description
This is xbuffy, an X program designed to watch multiple mail folders 
for new mail. This version supports mbox/mh/maildir and was patched to 
properly handle rfc2047 compliant email headers. 

This is a modified version of xbuffy 3.3 by Bill Pemberton (wfp5p@virginia.edu).

%description -l pl
Xbuffy jest programem typu xbiff dzia³ajacym w ¶rodowisku X Window,
przeznaczonym do jednoczesnego monitorowania wielu skrzynek pocztowych.
Ta wersja rozpoznaje skrzynki typu mbox, MH, mailDir oraz zosta³a 
po³atana by prawid³owo obs³ugiwaæ nag³ówki zgodne z rfc2047.

Jest to zmodyfikowana wersja programu xbuffy 3.3 
napisanego przez Billa Pembertona (wfp5p@virginia.edu).

%prep
%setup -q
%patch0 -p1
cp %{SOURCE1} .
head -n 30 xbuffy.c >LICENCE

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D xbuffy $RPM_BUILD_ROOT%{_bindir}/xbuffy
install -D xbuffy.man $RPM_BUILD_ROOT%{_mandir}/man1/xbuffy.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}.readme LICENCE 
%{_mandir}/man1/xbuffy.1*
%attr(755,root,root) %{_bindir}/xbuffy
