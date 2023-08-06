import os
import random
from posaydones_material_theming.modules.theming import get_theme_from_image
from posaydones_material_theming.modules.templates import handle_templates
from posaydones_material_theming.modules.wallpaper import set_wallpaper


def add_slash_if_needed(s):
    if s == "":
        return ""
    elif s[-1] != '/':
        s += '/'
    return s


def proceed_theme(path, color_scheme_type, wallpaper_setter):
    if os.path.isdir(path):
        files = os.listdir(path)
        random_file = random.choice(files)
        path = os.path.join(path, random_file)

    theme = get_theme_from_image(path, color_scheme_type)
    handle_templates(theme)
    set_wallpaper(path, wallpaper_setter)
