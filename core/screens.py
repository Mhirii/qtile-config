from utils.screens import number_of_screens
from libqtile.config import Screen
from libqtile import bar, widget

screen = []
for i in range(number_of_screens):
    screen.append(
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=35,
                opacity=1,
                # background="000000",
                border_color="#282738",
                border_width=[0, 0, 0, 0],
                margin=[0, 0, 0, 0],
            ),
        ),
    )
