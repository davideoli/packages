%global gittag 0.0.2

Name:		xfce4-hotcorner-plugin	
Version:	0.0.2
Release:	1%{?dist}
Summary:	XFCE4 HotCorner Panel Plugin

License:	GPLv2+
URL:		https://github.com/brianhsu/xfce4-hotcorner-plugin
Source0:	https://github.com/brianhsu/%{name}/archive/%{gittag}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	cmake libwnck3-devel xfce4-panel-devel gcc 
Requires:	xfce4-panel

%description
This plugin aims to provide an easy to use xfce4 panel plugin that lets users set hot corner actions.

%prep
%setup -q
sed -i -e 's|lib/xfce4/panel/plugins/|%{_libdir}/xfce4/panel/plugins|g' CMakeLists.txt

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .


%install
%make_install




%files
%{_libdir}/xfce4/panel/plugins/libhotcorner.so
%{_prefix}/share/xfce4/panel/plugins/hotcorner.desktop
%{_prefix}/share/locale/zh_TW/LC_MESSAGES/xfce4-hotcorner-plugin.mo


%doc AUTHORS README.md



%changelog
* Tue May 31 2016 Davide Olivieri <olivieri.dav@gmail.com> - 0.0.2
- Initial Packaging

