from libqtile import qtile, widget
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
        update_interval=5,
        **FONT_PARAMS,
    )


def memory_widget():
    return widget.Memory(
        background=theme["dark_1"],
        format="{MemPercent}%",
        update_interval=5,
        **FONT_PARAMS,
    )


def date():
    return widget.Clock(
        format="%A %d ",
        background=theme["dark_2"],
        **FONT_PARAMS,
    )


def time():
    return widget.Clock(
        format="%I:%M",
        background=theme["dark_2"],
        **FONT_PARAMS,
    )


def current_layout():
    return (
        widget.CurrentLayout(
            background=theme["dark_1"],
            fmt="󰙀 {}",
            **FONT_PARAMS,
        ),
    )


def wallpaper_widget():
    return widget.Wallpaper(
        background=theme["dark_1"],
        **FONT_PARAMS,
        fmt=" 󰲍  {}",
        directory=f"~/.config/qtile/wallpapers/{theme['name']}",
        max_chars=40,
    )


def volume_widget():
    return (
        widget.Volume(
            background=theme["dark_1"],
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
            **FONT_PARAMS,
        ),
    )


def sys_tray():
    return (
        widget.Systray(
            padding=4,
            background=theme["dark_1"],
            fontsize=2,
            icon_size=16,
        ),
    )


def groups():
    return (
        widget.GroupBox(
            **FONT_PARAMS,
            borderwidth=2,
            padding=2,
            highlight_method="block",
            background=theme["dark_2"],
            inactive=theme["dark_3"],
            active=theme["accent"],
            block_highlight_text_color=theme["blue_1"],
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
    )
