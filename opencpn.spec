Name: opencpn
Summary: Chartplotter and GPS navigation software
Version: 4.8.0
Release: 1%{?dist}
License: GPLv2+

Source0: https://github.com/OpenCPN/OpenCPN/archive/v4.8.0.zip
Patch0: https://patch-diff.githubusercontent.com/raw/OpenCPN/OpenCPN/pull/885.patch
Patch1: https://patch-diff.githubusercontent.com/raw/OpenCPN/OpenCPN/pull/887.patch

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: elfutils-libelf-devel
BuildRequires: expat-devel
BuildRequires: gettext
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: portaudio-devel
BuildRequires: portaudio-devel
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: xz-devel
BuildRequires: xz-lzma-compat

%description
Chart Plotter and Navigational software program for use underway
or as a planning tool.

%package gshhs-min
Summary: Minimum GSHHG dataset
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description gshhs-min
Minimum GSHHG dataset

%package gshhs-crude
Summary: Crude GSHHS dataset
Requires: %{name}%{_isa} = %{version}-%{release}
Requires: %{name}-gshhs-min%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description gshhs-crude
Crude GSHHG dataset

%package gshhs-low
Summary: Low GSHHS dataset
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description gshhs-low
Low GSHHG dataset

%package gshhs-intermediate
Summary: Minimum GSHHS dataset
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description gshhs-intermediate
Intermediate GSHHG dataset

%package gshhs-high
Summary: High GSHHS dataset
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description gshhs-high
High GSHHG dataset

%package gshhs-full
Summary: Full GSHHS dataset
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description gshhs-full
Full GSHHG dataset

%package plugin-chartdldr
Summary: Chart downloading plugin for OpenCPN
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description plugin-chartdldr
Chart downloading plugin for OpenCPN

%package plugin-chartdldr-doc
Summary: Documentation for chart downloading plugin for OpenCPN
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description plugin-chartdldr-doc
Documentation for chart downloading plugin for OpenCPN

%package plugin-dashboard
Summary: Dashboard plugin for OpenCPN
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description plugin-dashboard
Dashboard plugin for OpenCPN

%package plugin-grib
Summary: Weather forecast download & display plugin for OpenCPN
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description plugin-grib
OpenCPN plugin to display Grib weather data files

%package plugin-wmm
Summary: World Magnetic Model plugin for OpenCPN
Requires: %{name}%{_isa} = %{version}-%{release}
Supplements: %{name}%{_isa} = %{version}-%{release}

%description plugin-wmm
World Magnetic Model plugin for OpenCPN

%prep
%setup0 -n OpenCPN-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake -DBUNDLE_GSHHS=FULL
make

%install
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang %{name}
%find_lang %{name}-chartdldr_pi
%find_lang %{name}-dashboard_pi
%find_lang %{name}-grib_pi
%find_lang %{name}-wmm_pi

%files -f %{name}.lang
/usr/bin/opencpn
%dir %{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/%{name}
%doc %{_datadir}/%{name}/license.txt
%dir %{_datadir}/%{name}/uidata
%config %{_datadir}/%{name}/uidata/*
%dir %{_datadir}/%{name}/s57data
%config %{_datadir}/%{name}/s57data/*.csv
%config %{_datadir}/%{name}/s57data/*.RLE
%config %{_datadir}/%{name}/s57data/*.xml
%{_datadir}/%{name}/s57data/*.png


#%dir %{_datadir}/%{name}/tcdata
#%{_datadir}/%{name}/tcdata/HARMONIC
#%{_datadir}/%{name}/tcdata/HARMONIC.IDX
#%doc %{_datadir}/%{name}/tcdata/README*

%dir %{_datadir}/%{name}/sounds
%{_datadir}/%{name}/sounds/*.wav

%doc %{_datadir}/%{name}/sounds/README*

%docdir %{_datadir}/%{name}/doc
%doc %{_datadir}/%{name}/doc/help_web.html
%doc %{_datadir}/%{name}/CoC-909_2013-InlandECDIS_20170308s.pdf
#%exclude %{_datadir}/%{name}/doc/readme*
#%doc %{_datadir}/%{name}/doc/help_en_US.html
#%doc %{_datadir}/%{name}/doc/images/*

%docdir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/copyright
%doc %{_datadir}/doc/%{name}/changelog

%dir %{_datadir}/%{name}/gshhs

%files gshhs-min
%{_datadir}/%{name}/gshhs/poly-c-1.dat

%files gshhs-crude
%{_datadir}/%{name}/gshhs/wdb_borders_c.b
%{_datadir}/%{name}/gshhs/wdb_rivers_c.b

%files gshhs-low
%{_datadir}/%{name}/gshhs/wdb_borders_l.b
%{_datadir}/%{name}/gshhs/wdb_rivers_l.b
#%{_datadir}/%{name}/gshhs/poly-l-1.dat

%files gshhs-intermediate
%{_datadir}/%{name}/gshhs/wdb_borders_i.b
%{_datadir}/%{name}/gshhs/wdb_rivers_i.b
%{_datadir}/%{name}/gshhs/poly-i-1.dat

%files gshhs-intermediate
%{_datadir}/%{name}/gshhs/wdb_borders_h.b
%{_datadir}/%{name}/gshhs/wdb_rivers_h.b
%{_datadir}/%{name}/gshhs/poly-h-1.dat

%files gshhs-full
%{_datadir}/%{name}/gshhs/wdb_borders_f.b
%{_datadir}/%{name}/gshhs/wdb_rivers_f.b
%{_datadir}/%{name}/gshhs/poly-f-1.dat

%files plugin-chartdldr -f %{name}-chartdldr_pi.lang
%{_libdir}/%{name}/libchartdldr_pi.so
%dir %{_datadir}/%{name}/plugins/chartdldr_pi/data
%config %{_datadir}/%{name}/plugins/chartdldr_pi/data/*.xml
%{_datadir}/%{name}/plugins/chartdldr_pi/data/*.png

%files plugin-chartdldr-doc
%docdir %{_datadir}/%{name}/plugins/chartdldr_pi/data/doc
%doc %{_datadir}/%{name}/plugins/chartdldr_pi/data/doc/*

%files plugin-dashboard -f %{name}-dashboard_pi.lang
%{_libdir}/%{name}/libdashboard_pi.so
%dir %{_datadir}/%{name}/plugins/dashboard_pi/data
%{_datadir}/%{name}/plugins/dashboard_pi/data/*.svg

%files plugin-grib -f %{name}-grib_pi.lang
%{_libdir}/%{name}/libgrib_pi.so
%dir %{_datadir}/%{name}/plugins/grib_pi/data
%{_datadir}/%{name}/plugins/grib_pi/data/*.svg

%files plugin-wmm -f %{name}-wmm_pi.lang
%{_libdir}/%{name}/libwmm_pi.so
%dir %{_datadir}/%{name}/plugins/wmm_pi/data
%config %{_datadir}/%{name}/plugins/wmm_pi/data/*.COF
%{_datadir}/%{name}/plugins/wmm_pi/data/*.svg
