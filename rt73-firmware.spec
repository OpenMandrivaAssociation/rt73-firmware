%define name rt73-firmware
%define rtname RT71W_Firmware
%define version 1.8
%define release %mkrel 3

Summary: Firmware for the RT73 chip
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ralinktech.com/ralink/data/%{rtname}_V%{version}.tar.bz2
License: Proprietary
Group: System/Kernel and hardware
Url: http://rt2x00.serialmonkey.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This package contains the firmware files for the RT73 chip, which is
used in WLAN USB sticks.

%prep
%setup -q -n %{rtname}_V%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
install -m644 rt73.bin $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/lib/firmware/rt73.bin

