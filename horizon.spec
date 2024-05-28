Name: horizon-eda
Version: 2.6.0
Release: 1

Summary: Horizon is a free EDA package
License: GPL-3.0-or-later
Group: Engineering
Url: https://github.com/horizon-eda/horizon

Source: https://github.com/horizon-eda/horizon/archive/refs/tags/v%version.tar.gz

BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cppzmq-devel
BuildRequires: cairomm-devel
BuildRequires: boost-devel
BuildRequires: glm-devel
BuildRequires: gtkmm30-devel
BuildRequires: libarchive-devel
BuildRequires: libcurl-devel
BuildRequires: libgit2-devel
BuildRequires: librsvg2-devel
BuildRequires: libspnav-devel
BuildRequires: libuuid-devel
BuildRequires: opencascade-devel
BuildRequires: podofo-devel
BuildRequires: sqlite-devel

%description
%summary.

%prep
%autosetup -v -n %{name}-%{version}

%build
%meson
%meson_build


%install
%meson_install

%files
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*
%doc *.md

%changelog
