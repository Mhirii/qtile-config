from libqtile.config import Match

browsers = [
    Match(wm_class="firefox"),
    Match(wm_class="firedragon"),
    Match(wm_class="chromium"),
]

terminals = [
    Match(wm_class="alacritty"),
    Match(wm_class="kitty"),
]

editors = [
    Match(wm_class="code"),
    Match(wm_class="neovide"),
]

music_players = [
    Match(wm_class="Spotify"),
    Match(title="spotify-tui"),
    Match(title="cava"),
]
password_managers = [
    Match(wm_class="Bitwarden"),
]
communication = [
    Match(wm_class="discord"),
    Match(wm_class="telegram-desktop"),
]
