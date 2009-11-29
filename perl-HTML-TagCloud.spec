%define upstream_name    HTML-TagCloud
%define upstream_version 0.34

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Generate An HTML Tag Cloud
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The the HTML::TagCloud manpage module enables you to generate "tag clouds"
in HTML. Tag clouds serve as a textual way to visualize terms and topics
that are used most frequently. The tags are sorted alphabetically and a
larger font is used to indicate more frequent term usage.

Example sites with tag clouds: the http://www.43things.com/ manpage, the
http://www.astray.com/recipes/ manpage and the
http://www.flickr.com/photos/tags/ manpage.

This module provides a simple interface to generating a CSS-based HTML tag
cloud. You simply pass in a set of tags, their URL and their count. This
module outputs stylesheet-based HTML. You may use the included CSS or use
your own.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/man3/*
%perl_vendorlib/*


