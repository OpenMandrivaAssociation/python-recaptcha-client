Name:           python-recaptcha-client
Version:        1.0.6
Release:        2
Summary:        Python module for reCAPTCHA and reCAPTCHA Mailhide

Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/recaptcha-client
Source0:        http://pypi.python.org/packages/source/r/recaptcha-client/recaptcha-client-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-pycrypto

%description
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not require
any imaging libraries because the CAPTCHA is served directly from reCAPTCHA.
Also allows you to securely obfuscate emails with Mailhide. This functionality
requires python-crypto. This library requires two types of API keys. If you'd
like to use the CAPTCHA, you'll need a key from
http://recaptcha.net/api/getkey. For Mailhide, you'll need a key from
http://mailhide.recaptcha.net/apikey.

%prep
%setup -q -n recaptcha-client-%{version}
sed -i 's/^from ez_setup/#from ez_setup/' setup.py
sed -i 's/^use_setuptools()/#use_setuptools()/' setup.py


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc PKG-INFO
%{python_sitelib}/recaptcha/
%{python_sitelib}/recaptcha_client*-nspkg.pth
%{python_sitelib}/recaptcha_client*.egg-info/



%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 662539
- update to new version 1.0.6

* Sun Nov 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.5-1mdv2011.0
+ Revision: 594396
- import python-recaptcha-client

