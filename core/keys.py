from libqtile.config import Key
from libqtile.lazy import lazy
from settings import apps

mod = "mod4"
alt = "mod1"
ctrl = "control"
shift = "shift"

essentials = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, shift], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key(
        [mod, shift], "l", lazy.layout.shuffle_right(), desc="Move window to the right"
    ),
    Key([mod, shift], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, ctrl], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, ctrl], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, ctrl], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, ctrl], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, ctrl], "j", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, ctrl], "k", lazy.layout.grow(), desc="Grow window"),
    Key([mod, shift, ctrl], "h", lazy.layout.swap_column_left()),
    Key([mod, shift, ctrl], "l", lazy.layout.swap_column_right()),
    Key([mod, ctrl], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([alt], "tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, shift],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, ctrl], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, shift], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "Return", lazy.spawn(apps["terminal"]), desc="Launch terminal"),
]

media = [
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
]

screens = [
    Key([mod], "bracketright", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "bracketleft", lazy.prev_screen(), desc="Move focus to prev monitor"),
]

launch = [
    Key([mod], "b", lazy.spawn("firedragon"), desc="Launch firedragon"),
    Key([mod], "c", lazy.spawn(apps["visual"]), desc="Launch firedragon"),
]

utils = [
    Key([mod], "d", lazy.spawn(apps["dmenu"]), desc="Launch dmenu"),
    Key([mod], "e", lazy.spawn(apps["editor"]), desc="Launch neovide"),
    Key([mod], "Print", lazy.spawn(apps["editor"]), desc="Launch neovide"),
    Key(
        [mod],
        "v",
        lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard"),
        desc="Launch neovide",
    ),
]

keybinds = essentials
keybinds.extend(screens)
keybinds.extend(media)
keybinds.extend(launch)
keybinds.extend(utils)
