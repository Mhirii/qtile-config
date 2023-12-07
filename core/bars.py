from libqtile import widget, qtile

from settings import FONT_PARAMS
from themes import current_theme
from core.widgets import (
    cpu_widget,
    date,
    default_spacer,
    memory_widget,
    separator_pipe_reverse,
    slash,
    slash_reverse,
    spacer,
    separator_pipe,
    time,
)

theme = current_theme

# ⭘
LEFT_SIDE = (
    spacer(theme["dark_3"], 8),
    widget.TextBox(
        **FONT_PARAMS,
        text="⭘ ",
        background=theme["dark_3"],
    ),
    separator_pipe(theme["dark_2"], theme["dark_3"]),
    widget.GroupBox(
        **FONT_PARAMS,
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
    separator_pipe(theme["dark_1"], theme["dark_2"]),
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
        **FONT_PARAMS,
        prompt=" ❯ ",
    ),
    separator_pipe(theme["dark_0"], theme["dark_1"]),
    default_spacer(theme["dark_0"]),
)
MIDDLE = (separator_pipe_reverse(theme["dark_2"], theme["dark_1"]),)
RIGHT_SIDE = (
    separator_pipe_reverse(theme["dark_0"], theme["dark_1"]),
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
    separator_pipe_reverse(theme["dark_1"], theme["dark_2"]),
    date(),
    time(),
    spacer(theme["dark_2"], 8),
)


def init_widgets_list():
    return [
        *LEFT_SIDE,
        *RIGHT_SIDE,
        separator_pipe_reverse(theme["dark_2"], theme["dark_3"]),
        widget.Systray(
            padding=4,
            background=theme["dark_3"],
            fontsize=2,
            icon_size=16,
        ),
    ]


def init_secondary_widgets_list():
    return [*LEFT_SIDE, *MIDDLE, *RIGHT_SIDE]

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
