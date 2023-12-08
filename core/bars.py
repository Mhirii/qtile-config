from libqtile import widget, qtile

from settings import FONT_PARAMS
from settings.settings import FONT_BOLD, FONT_SIZE, FONT_SIZE_BIG, apps
from themes import current_theme
from core.widgets import (
    cpu_widget,
    date,
    default_spacer,
    memory_widget,
    separator_pipe_reverse,
    slash,
    separator_arrow,
    separator_arrow_reverse,
    slash_reverse,
    spacer,
    separator_pipe,
    time,
)

theme = current_theme

GROUP_BLOCK = (
    spacer(theme["accent"], 8),
    widget.TextBox(
        text="󰊠 ",
        background=theme["accent"],
        foreground=theme["dark_0"],
        font=FONT_BOLD,
        fontsize=FONT_SIZE,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(apps["dmenu"])},
    ),
    separator_pipe(theme["dark_2"], theme["accent"]),
    widget.GroupBox(
        font=FONT_BOLD,
        fontsize=FONT_SIZE,
        borderwidth=2,
        padding=2,
        highlight_method="block",
        background=theme["dark_2"],
        inactive=theme["dark_3"],
        active=theme["gray_0"],
        block_highlight_text_color=theme["accent"],
        highlight_color="#4B427E",
        this_current_screen_border=theme["dark_2"],
        this_screen_border=theme["dark_2"],
        other_current_screen_border=theme["dark_3"],
        other_screen_border=theme["dark_2"],
        urgent_alert_method="text",
        # urgent_border="#181c21",
        urgent_text="#af5555",
        rounded=True,
        # hide_unused=True,
        disable_drag=True,
    ),
    separator_arrow(theme["dark_1"], theme["dark_2"]),
)

LAYOUT_BLOCK = (
    widget.Spacer(
        length=8,
        background=theme["dark_1"],
    ),
    widget.CurrentLayout(
        background=theme["dark_1"],
        **FONT_PARAMS,
        fmt="󰙀 {}",
    ),
    widget.Chord(
        chords_colors={
            " launch": ("#7aa0ff", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.Prompt(
        background=theme["dark_1"],
        font=FONT_BOLD,
        fontsize=FONT_SIZE,
        foreground=theme["accent"],
        prompt=" › ",
    ),
    separator_arrow(theme["dark_0"], theme["dark_1"]),
    default_spacer(theme["dark_0"]),
)

STATS_BLOCK = (
    separator_arrow_reverse(theme["dark_0"], theme["dark_1"]),
    spacer(theme["dark_1"], 8),
    cpu_widget(),
    slash_reverse(theme["dark_1"], theme["dark_2"]),
    memory_widget(),
    slash_reverse(theme["dark_1"], theme["dark_2"]),
    widget.Volume(
        background=theme["dark_1"],
        **FONT_PARAMS,
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
        volume_app="pavucontrol",
    ),
)

TIME_BLOCK = (
    separator_arrow_reverse(theme["dark_2"], theme["dark_3"]),
    date(theme["dark_3"]),
    separator_pipe_reverse(theme["dark_3"], theme["accent"]),
    time(theme["accent"], theme["dark_0"]),
    spacer(theme["accent"], 8),
)


def init_widgets_list():
    """
    Initialize the widgets list.

    Returns:
        list: A list of widgets.
    """
    return [
        *GROUP_BLOCK,
        *LAYOUT_BLOCK,
        *STATS_BLOCK,
        spacer(theme["dark_1"], 8),
        separator_arrow_reverse(theme["dark_1"], theme["dark_2"]),
        spacer(theme["dark_2"], 8),
        widget.Systray(
            padding=4,
            background=theme["dark_2"],
            fontsize=2,
            icon_size=16,
        ),
        spacer(theme["dark_2"], 8),
        *TIME_BLOCK,
    ]


def init_secondary_widgets_list():
    """
    Initializes the secondary widgets list by combining the elements of the LEFT_SIDE, MIDDLE, and RIGHT_SIDE lists.

    Returns:
        list: A list of widgets.
    """
    return [
        *GROUP_BLOCK,
        *LAYOUT_BLOCK,
        *STATS_BLOCK,
        *TIME_BLOCK,
    ]

    # widgets_list = [
    #     # spacer(theme["dark_2"], 8),
    #     # separator_pipe(theme["dark_1"], theme["dark_2"]),
    #     # separator_pipe(theme["dark_2"], theme["dark_1"]),
    #     # default_spacer(theme["dark_2"]),
    #     # separator_pipe_reverse(theme["dark_2"], theme["dark_1"]),
    #     # # cpu_widget(),
    #     # spacer(theme["dark_2"], 8),
    #     # # sys_tray(),
    #     # separator_pipe_reverse(theme["dark_2"], theme["dark_1"]),
    #     # date(),
    #     # time(),
    #     # spacer(theme["dark_1"], 8),
    # ]
