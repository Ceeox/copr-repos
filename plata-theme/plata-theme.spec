%define git_owner       tista500
%define git_url         https://gitlab.com/%{git_owner}/%{name}
Name:           plata-theme
Summary:        Plata Gtk Theme
License:        GPL 2.0
URL:            %{git_url}

Version:        0.5.93
Release:        1%{?dist}
Source0:        %{git_url}/-/archive/%{version}/%{name}-%{version}.tar.gz       

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gdkpixbuf2-devel
BuildRequires:  sassc
BuildRequires:  parallel
BuildRequires:  inkscape
BuildRequires:  pkgconfig
BuildRequires:  libxml2
BuildRequires:  glib2-devel


%description
Plata-theme
A Gtk+ theme based on Material Design Refresh.

%prep
%setup -qn %{name}-%{version}

%build
./autogen.sh \
--prefix=%{_prefix} \
--enable-parallel \
--enable-plank \
--enable-telegram \
--enable-tweetdeck \
--enable-gtk_next
%make_build

%install
%make_install

%files
%{_datadir}/themes/*
