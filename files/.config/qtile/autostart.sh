#!/usr/bin/env bash


# Restore Wallpaper
nitrogen --restore &

# Graphical authentication agent (for gparted and others)
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &	

# Volume applet
killall volumeicon # kill applest during reload
volumeicon &

killall nm-applet
nm-applet &

setxkbmap us
picom -f &
