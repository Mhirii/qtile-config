from libqtile import layout
from themes import current_theme


theme = current_theme


def init_layouts():
    """
    Initializes and returns a list of layout objects.

    Returns:
        list: A list of layout objects. Each layout object is an instance of the layout class and defines the visual layout of the application window.
    """
    return [
        layout.Columns(
            border_focus=theme["accent"],
            border_focus_stack=[theme["red_1"], theme["dark_1"]],
            border_normal=theme["dark_1"],
            border_width=2,
            grow_amount=10,
            insert_position=1,  # 0 means right above the current window, 1 means right after
            margin=8,
            margin_on_single=8,
            border_on_single=1,
            single_border_width=2,
        ),
        layout.MonadTall(
            border_focus=theme["accent"],
            border_normal=theme["dark_1"],
            margin=8,
            single_margin=4,
        ),
    ]
