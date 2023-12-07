from libqtile import layout
from themes import current_theme


theme = current_theme


def init_layouts():
    return [
        layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
        layout.MonadTall(
            border_focus=theme["accent"],
            border_normal=theme["dark_1"],
            margin=8,
            single_margin=4,
        ),
    ]
