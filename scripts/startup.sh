#!/bin/bash

sh ~/.screenlayout/reddragon.sh
nm-applet --indicator &
blueman-applet &
dunst &
feh --bg-fill --randomize ~/.config/qtile/wallpapers/ &
alacritty &
xclip &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
disown
sleep 1
picom --config ~/.config/qtile/conf/picom.conf &
greenclip daemon &
flameshot &

# megasync &
# telegram-desktop &
