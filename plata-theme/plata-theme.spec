%define git_owner       tista500
%define git_url         https://gitlab.com/%{git_owner}/%{name}
Name:           plata-theme
Summary:        Plata Gtk Theme
License:        GPL 2.0
Release:        1%{?dist}
URL:            %{git_url}

Version:        0.5.93
Release:        5%{?dist}
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

%prep
%setup -qn %{name}-%{version}

%build
./autogen.sh --prefix=./usr
make

%install
%make_install
