from pathlib import Path
import platform
import subprocess

home = str(Path.home())
conf_dir = home + "/.config/qtile/"
scripts_dir = conf_dir + "scripts/"

hostname = platform.node


def number_of_screens():
    return int(subprocess.check_output([scripts_dir + "screens.sh"]))
