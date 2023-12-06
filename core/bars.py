from core.widgets import (
    separator_pipe,
    separator_pipe_reverse,
    spacer,
    date,
    time,
    default_spacer,
)
from themes import current_theme
from libqtile import widget
from settings import FONT_PARAMS

theme = current_theme


def init_widgets_list(screen: int):
    widgets_list = [
        spacer(theme["dark_1"], 0),
        separator_pipe(theme["dark_1"], theme["dark_0"]),
        widget.GroupBox(
            **FONT_PARAMS,
            borderwidth=2,
            padding=2,
            highlight_method="block",
            background=theme["dark_1"],
            inactive=theme["dark_2"],
            active=theme["accent"],
            block_highlight_text_color=theme["accent"],
            highlight_color="#4B427E",
            foreground="#4B427E",
            this_current_screen_border=theme["dark_1"],
            this_screen_border=theme["dark_1"],
            other_current_screen_border=theme["dark_2"],
            other_screen_border=theme["dark_1"],
            urgent_alert_method="text",
            # urgent_border="#181c21",
            urgent_text="#af5555",
            rounded=True,
            # hide_unused=True,
            disable_drag=True,
        ),
        spacer(theme["dark_1"], 8),
        separator_pipe(theme["dark_0"], theme["dark_1"]),
        separator_pipe(theme["bg1"], theme["bg"]),
        default_spacer(theme["bg1"]),
        separator_pipe_reverse(theme["bg1"], theme["bg"]),
    ]

    if screen == 0:
        widgets_list.append(
            widget.Systray(
                padding=4,
                background=theme["bg"],
                fontsize=2,
                icon_size=16,
            ),
        )

    widgets_list.append(
        spacer(theme["dark_1"], 8),
        separator_pipe_reverse(theme["dark_1"], theme["dark_0"]),
        widget.TextBox(
            text=" ",
            background=theme["dark_0"],
        ),
        date(),
        time(),
        spacer(theme["dark_0"], 8),
    )
