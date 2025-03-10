Summary:	Abseil Python Common Libraries
Summary(pl.UTF-8):	Wspólne biblioteki Abseil dla Pythona
Name:		python3-absl
Version:	1.0.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/absl-py/
Source0:	https://files.pythonhosted.org/packages/source/a/absl-py/absl-py-%{version}.tar.gz
# Source0-md5:	89104cd7c82540a57c3ecb99ba4ab1e6
URL:		https://github.com/abseil/abseil-py
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abseil Python is a collection of Python library code for building
Python applications. The code is collected from Google's own Python
code base, and has been extensively tested and used in production.

%description -l pl.UTF-8
Abseil Python to biblioteka Pythona będąca zbiorem kodu do tworzenia
aplikacji pythonowych. Kod bibliotek został zebrany z własnego kodu
Google'a w Pythonie, obszernie przetestowany i jest używany
produkcyjnie.

%prep
%setup -q -n absl-py-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/absl
%{py3_sitescriptdir}/absl_py-%{version}-py*.egg-info
