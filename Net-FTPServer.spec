# Automatically generated by Net-FTPServer.spec.PL

%define perlsitelib %(perl -e 'use Config; print $Config{installsitelib}')
%define perlman1dir %(perl -e 'use Config; print $Config{installman1dir}')
%define perlman3dir %(perl -e 'use Config; print $Config{installman3dir}')
%define perlversion %(perl -e 'use Config; print $Config{version}')

Summary: Net::FTPServer - an extensible, secure FTP server
Name: perl-Net-FTPServer
Version: 1.122
Release: 1
Copyright: GPL
Group: Applications/Internet
Source: Net-FTPServer-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-root
BuildRequires: perl-Authen-PAM >= 0.12
BuildRequires: perl-BSD-Resource >= 1.08
BuildRequires: perl-File-Sync >= 0.09
BuildRequires: perl-IO-stringy >= 1.220
BuildRequires: perl >= %{perlversion}
Requires: perl-Authen-PAM >= 0.12
Requires: perl-BSD-Resource >= 1.08
Requires: perl-File-Sync >= 0.09
Requires: perl-IO-stringy >= 1.220
Requires: perl >= %{perlversion}


%description
Biblio@Tech Net::FTPServer - A full-featured, secure, extensible
and configurable Perl FTP server.


%prep
%setup -q -n Net-FTPServer-%{version}


%build
NET_FTPSERVER_NO_SLEEP=1 perl Makefile.PL `perl -MExtUtils::MakeMaker -e 'print q|PREFIX=%{buildroot}/usr| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '`
make
make test


%install
rm -rf $RPM_BUILD_ROOT
make install sysconfdir=%{buildroot}/etc `perl -MExtUtils::MakeMaker -e 'print \$ExtUtils::MakeMaker::VERSION <= 6.05 ? q|PREFIX=%{buildroot}/usr| : q|DESTDIR=%{buildroot}| '`
# MakeMaker ignores perlman3dir setting.
find %{buildroot} -name man3 | perl -p -e 's@%{buildroot}(.*)@$1/*.3*@' > %{name}-man


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}-man
%defattr(-,root,root)
%doc AUTHORS COPYING FAQ INSTALL README TODO doc/*
%{perlsitelib}/Net/FTPServer.pm
%{perlsitelib}/Net/FTPServer/
/usr/sbin/*.pl
%config(noreplace) /etc/ftpd.conf


%changelog
* Thu May 01 2003 Rob Brown <bbb@cpan.org>
- Compatibilty fixes (perl 5.005/5.8.0/5.8.1/5.9.0).
* Fri Jan 17 2003 Rob Brown <bbb@cpan.org>
- No more XS code.
* Fri Dec 28 2001 Richard Jones <rich@annexia.org>
- Better handling of different Perl versions. RPM contains documentation,
- config file and start-up scripts.
* Tue Feb 15 2001 Rob Brown <bbb@cpan.org>
- Generalized files - works with Perl 5.6 as well as with Perl 5.005
* Tue Feb 08 2001 Richard Jones <rich@annexia.org>
- initial creation