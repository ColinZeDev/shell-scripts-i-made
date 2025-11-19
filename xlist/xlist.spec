Name:           xlist
Version:        0.0.1
Release:        1%{?dist}
Summary:        An enhanced ls command

License:        MIT
URL:            https://github.com/ColinZeDev/xlist
Source0:        xlist.sh

BuildArch:      noarch
Requires:       bash

%description
xlist is a custom shell script that improves upon the standard 'ls' command
with additional features and formatting.

%prep
# No preparation needed for a single script

%install
mkdir -p %{buildroot}/usr/local/bin

install -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/xlist

%files
/usr/local/bin/xlist

%changelog
* Tue Nov 19 2025 ColinZeDev - 0.0.1
- Initial package for xlist
