from themes import current_theme

theme = current_theme

FONT = "JetbrainsMono Nerd Font"
FONT_SIZE = 14
FONT_BOLD = "JetbrainsMono Nerd Font Bold"
FONT_SIZE_BIG = 18
FOREGROUND = theme["light_1"]

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
    "telegram": "telegram-desktop",
    "screenshot": "flameshot full -p /home/mhiri/Pictures/Screenshots",
    "dmenu": f"dmenu_run -i -nb {theme['dark_1']} -nf {theme['accent']} -sb {theme['accent']} -sf {theme['dark_1']} -fn 'JetbrainsMono Nerd Font:bold:pixelsize:24'",
}
