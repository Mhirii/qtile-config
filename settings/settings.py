from themes import current_theme

FONT = "JetbrainsMono Nerd Font"
FONT_SIZE = 14
FONT_BOLD = "JetbrainsMono Nerd Font Bold"
FONT_SIZE_BIG = 18
FOREGROUND = current_theme["light_1"]

FONT_PARAMS = {
    "font": FONT,
    "fontsize": FONT_SIZE,
    "foreground": FOREGROUND,
}

apps = {
    "terminal": "alacritty",
    "browser": "firedragon",
    "editor": "neovide",
    "visual": "code --password-store=gnome",
    "screenshot": "flameshot full -p /home/mhiri/Pictures/Screenshots",
    "dmenu": "dmenu_run -i -nb '#16161e' -nf '#7aa2f7' -sb '#7aa2f7' -sf '#16161e' -fn 'SpaceMono Nerd Font:bold:pixelsize:24'",
}
