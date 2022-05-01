#!/usr/bin/env bash
#nitrogen --set-zoom --save ~/.config/qtile/wallpaper.jpg

# Graphical authentication agent (for gparted and others)
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &	

# Volume applet
volumeicon &

nm-applet &

setxkbmap us

picom -f &
