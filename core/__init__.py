from core.keys import keybinds
from core.groups import groups_list
from core.window import floating_layout
from core.screens import init_screens
from core.info import home, conf_dir, scripts_dir, number_of_screens
from core.layouts import init_layouts

__all__ = [
    # ────────────────────────────────── configs ───────────────────────────────── #
    "keybinds",
    "groups_list",
    "floating_layout",
    "init_screens",
    "init_layouts",
    # ─────────────────────────────────── paths ────────────────────────────────── #
    "home",
    "conf_dir",
    "scripts_dir",
    "number_of_screens",
]
