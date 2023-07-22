import os
import random
import sys
from argparse import ArgumentParser
from app.modules import theming
from app.modules import templates
from app.modules import wallpaper
from app.gui import window


def proceed_theme(path, color_scheme_type):
    if os.path.isdir(path):
        files = os.listdir(path)
        random_file = random.choice(files)
        path = os.path.join(path, random_file)

    theme = theming.get_theme_from_image(path, color_scheme_type)
    templates.handle_templates(theme)
    wallpaper.set_wallpaper(path, "hyprpaper")

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
    args = parser.parse_args()
    if args.image_path is None:
        run_gui()
    else:
        if args.image_path is not None:
            proceed_theme(args.image_path, args.theme_type)
        else:
            print("Please provide a wallpaper path")


if __name__ == '__main__':
    main()
