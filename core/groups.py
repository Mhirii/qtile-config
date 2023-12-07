from libqtile.config import Group, Key
from libqtile.lazy import lazy
from core.keys import keybinds, mod

from settings.matches import (
    browsers,
    terminals,
    editors,
    music_players,
    communication,
)

groups_list = [
    Group("1", label="1", layout="monadtall", matches=terminals),
    Group("2", label="2", layout="monadtall", matches=browsers),
    Group("3", label="3", layout="monadtall", matches=editors),
    Group("4", label="4", layout="monadtall"),
    Group("5", label="5", layout="monadtall", matches=communication),
    Group("6", label="6", layout="monadtall", matches=music_players),
    Group("7", label="7", layout="monadtall"),
    Group("8", label="8", layout="monadtall"),
    Group("9", label="9", layout="monadtall"),
]

for index, i in enumerate(groups_list):
    keybinds.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Key(
            #     [mod, "alt"],
            #     i.name,
            #     lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name),
            # ),
        ]
    )
