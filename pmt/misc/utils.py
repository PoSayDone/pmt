import os
from pmt.modules.theming import get_theme_from_image
from pmt.modules.templates import handle_templates
from pmt.modules.wallpaper import set_wallpaper

def add_slash_if_needed(s):
    if s == "":
        return ""
    elif s[-1] != '/':
        s += '/'
    return s


def proceed_theme(path, color_scheme_type):
    if os.path.isdir(path):
        files = os.listdir(path)
        random_file = random.choice(files)
        path = os.path.join(path, random_file)

    theme = get_theme_from_image(path, color_scheme_type)
    handle_templates(theme)
    set_wallpaper(path, "hyprpaper")

