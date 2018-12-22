#! /bin/bash

soft=(cryptsetup-libs dbus dbus-libs device-mapper device-mapper-libs
dracut-config-generic dracut-config-rescue dracut-network freetype glib2
kmod libgudev1 nspr nss nss-softokn nss-softokn-freebl nss-sysinit nss-tools
nss-util systemd systemd-libs systemd-sysv libdrm)

for i in ${soft[@]}
do
 yumdownloader --resolve --destdir /var/cache/yum/x86_64/7/base/packages $i
done
