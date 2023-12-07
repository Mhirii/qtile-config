from libqtile.config import Screen
from libqtile import bar
from core.bars import init_widgets_list, init_secondary_widgets_list
from core.info import number_of_screens


def init_screens():
    n = number_of_screens()
    screens = [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=25,
                opacity=1,
                border_color="#282738",
                border_width=[0, 0, 0, 0],
                margin=[0, 0, 0, 0],
            ),
        )
    ]
    for i in range(n - 1):
        screens.append(
            Screen(
                top=bar.Bar(
                    widgets=init_secondary_widgets_list(),
                    size=25,
                    opacity=1,
                    border_color="#282738",
                    border_width=[0, 0, 0, 0],
                    margin=[0, 0, 0, 0],
                ),
            )
        )
    return screens
