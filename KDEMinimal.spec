Name:           KDEMinimal
Version:        0.0.1
Release:        0
Summary:        A Minimal KDE meta package
License:        MIT
Group:          Metapackages
URL:            https://github.com/anmazzotti/kde-minimal
Source0:        https://github.com/anmazzotti/kde-minimal/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  aaa_base
BuildRequires:  pkgconfig(systemd)

# Minimal KDE

## Greeter
# sddm still brings in x11 dependencies, see: https://bugzilla.opensuse.org/show_bug.cgi?id=1235041
#Requires:       sddm-qt6
#Requires:       sddm-kcm6
Requires:       tuigreet

## Plasma6 Workspace
Requires:       iso-codes
Requires:       iso-codes-lang
Requires:       accountsservice
Requires:       kf6-frameworkintegration-plugin
Requires:       kactivitymanagerd6
Requires:       kde-cli-tools6
Requires:       kf6-kded
Requires:       kf6-kquickcharts
Requires:       kglobalacceld6
Requires:       kirigami-addons6
Requires:       kscreen6
Requires:       kscreenlocker6
Requires:       kwin6
Requires:       libkscreen6-plugin
Requires:       qt6-positioning-imports
Requires:       qt6-tools-qdbus
Requires:       qt6-declarative-imports
Requires:       kf6-kconfig-imports
Requires:       milou6
Requires:       qt6-sql-sqlite
Requires:       kf6-knewstuff-imports
Requires:       ksystemstats6
Requires:       kf6-kuserfeedback-imports
Requires:       kio-extras
Requires:       knighttime6
Requires:       qt6-virtualkeyboard-imports
Requires:       kf6-krunner

## Plasma6 Session
Requires:       pipewire
Requires:       breeze6
Requires:       breeze6-decoration
Requires:       kf6-kwindowsystem
Requires:       polkit-kde-agent-6
Requires:       powerdevil6
Requires:       systemsettings6
Requires:       qt6-wayland
Requires:       xdg-user-dirs
Requires:       xorg-x11-server-wayland  

# Base Applications
Requires:       ark
Requires:       discover6
Requires:       dolphin
Requires:       gwenview
Requires:       kate
Requires:       kcalc
Requires:       konsole
Requires:       okular
Requires:       spectacle

# Flatpak
Requires:       flatpak
Requires:       discover6-backend-flatpak
Requires:       flatpak-kcm6

%install
install -D -p -m 644 %{buildroot}/greetd/config.toml %{_sysconfdir}/greetd/config.toml

%files
%dir %{_sysconfdir}/greetd/
%attr(644,greeter,greeter) %config(noreplace) %{_sysconfdir}/greetd/config.toml
