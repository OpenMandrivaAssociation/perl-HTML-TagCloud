%define upstream_name    HTML-TagCloud
%define upstream_version 0.38

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.38
Release:	2

Summary:	Generate An HTML Tag Cloud
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-TagCloud-0.38.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.370.0-1mdv2011.0
+ Revision: 686638
- update to new version 0.37

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.360.0-2
+ Revision: 657338
- rebuild for updated spec-helper

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.360.0-1
+ Revision: 639639
- update to new version 0.36

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 471077
- import perl-HTML-TagCloud


* Sun Nov 29 2009 cpan2dist 0.34-1mdv
- initial mdv release, generated with cpan2dist

