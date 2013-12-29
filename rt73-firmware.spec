%define	rtname	RT71W_Firmware

Summary:	Firmware for the RT73 chip
Name:		rt73-firmware
Version:	1.8
Release:	8
Source0:	http://www.ralinktech.com/ralink/data/%{rtname}_V%{version}.tar.bz2
Source1:	rt73.pm-utils
License:	Proprietary
Group:		System/Kernel and hardware
Url:		http://rt2x00.serialmonkey.com/
BuildArch:	noarch

%description
This package contains the firmware files for the RT73 chip, which is
used in WLAN USB sticks.

%prep
%setup -q -n %{rtname}_V%{version}

%build

%install
install -m644 rt73.bin -D %{buildroot}/lib/firmware/rt73.bin
install -m755 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/pm/config.d/rt73

%files
/lib/firmware/rt73.bin
%{_sysconfdir}/pm/config.d/rt73
