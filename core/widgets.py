from libqtile import widget
from settings import FONT, FONT_PARAMS
from themes import current_theme

GLYPH_SIZE = 25
theme = current_theme


def separator_pipe(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=GLYPH_SIZE,
        padding=0,
        background=bg,
        foreground=fg,
        font=FONT,
    )


def separator_pipe_reverse(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=GLYPH_SIZE,
        padding=0,
        background=bg,
        foreground=fg,
        font=FONT,
    )


def slash(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=GLYPH_SIZE,
        padding=0,
        background=bg,
        foreground=fg,
        font=FONT,
    )


def slash_reverse(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=GLYPH_SIZE,
        padding=0,
        background=bg,
        foreground=fg,
        font=FONT,
    )


def default_spacer(bg):
    return widget.Spacer(
        background=bg,
    )


def spacer(bg, space):
    return widget.Spacer(
        length=space,
        background=bg,
    )


def cpu_widget():
    return widget.CPU(
        background=theme["dark_1"],
        format="{load_percent}%",
        foreground=theme["accent"],
        update_interval=5,
        **FONT_PARAMS,
    )


def memory_widget():
    return widget.Memory(
        background=theme["dark_1"],
        format="{MemPercent}%",
        foreground=theme["accent"],
        update_interval=5,
        **FONT_PARAMS,
    )


def date():
    return widget.Clock(
        format="%A %d ",
        background=theme["bg"],
        foreground=theme["dark_1"],
        **FONT_PARAMS,
    )


def time():
    return widget.Clock(
        format="%I:%M",
        background=theme["dark_1"],
        foreground=theme["accent"],
        **FONT_PARAMS,
    )
