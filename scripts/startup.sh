#!/bin/bash

nm-applet --indicator &
blueman-applet &
dunst &
feh --bg-fill --randomize ~/.config/qtile/wallpapers/ &
alacritty &
xclip &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown
sleep 1;
picom --config ~/.config/qtile/conf/picom.conf &

# megasync &
# telegram-desktop &