import os
import random
import sys
from argparse import ArgumentParser
from .modules import theming
from .modules import templates
from .modules import wallpaper
from .gui import window
from .misc.utils import proceed_theme

def run_gui():
    app = window.PMT(application_id="com.example.GtkApplication")
    app.run(sys.argv)


def main():
    parser = ArgumentParser(prog='cli')
    parser.add_argument('-g','--gui', help='run the GUI')
    parser.add_argument(
        'image_path', nargs='?', default=None, help="Your wallpaper path to set theme for")
    parser.add_argument('-t', '--theme_type', default="dark",
                        help="\"dark\" or \"light\" values are allowed. Default dark.")
    parser.add_argument('-w', '--wallpaper_setter', default="hyprpaper",
                        help="\"hyprpaper\" or \"swww\" values are allowed. Default hyprpaper.")
    args = parser.parse_args()
    if args.image_path is None:
        run_gui()
    else:
        if args.image_path is not None:
            proceed_theme(args.image_path, args.theme_type, args.wallpaper_setter)
        else:
            print("Please provide a wallpaper path")


if __name__ == '__main__':
    main()
