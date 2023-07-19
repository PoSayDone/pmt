from material_color_utilities_python import *

additional_colors = [
    {"blend": True, "value": argbFromHex("#f38ba8"), "name": "red"},
    {"blend": True, "value": argbFromHex("#fab387"), "name": "orange"},
    {"blend": False, "value": argbFromHex("#f9e2af"), "name": "yellow"},
    {"blend": False, "value": argbFromHex("#a6e3a1"), "name": "green"},
    {"blend": False, "value": argbFromHex("#94e2d5"), "name": "teal"},
    {"blend": True, "value": argbFromHex("#89b4fa"), "name": "blue"},
    {"blend": True, "value": argbFromHex("#cba6f7"), "name": "magenta"},
    {"blend": False, "value": argbFromHex("#f2cdcd"), "name": "brown"},
]


def return_theme(theme, color_scheme_type):
    theme_json_string = theme.get("schemes").get(color_scheme_type).toJSON()
    theme_dict = json.loads(theme_json_string)
    custom_colors = theme.get("customColors")
    palettes = theme.get("palettes")
    for value in custom_colors:
        key = value.get("color").get("name")
        if (key == "yellow" or key == "green" or key == "teal") and (color_scheme_type == "dark"):
            theme_dict[key] = TonalPalette.fromInt(
                value.get(color_scheme_type).get("color")).tone(92)
        else:
            theme_dict[key] = value.get(color_scheme_type).get("color")

        if (color_scheme_type == "dark"):
            theme_dict['surfaceDim'] = palettes.get("neutral").tone(6)
            theme_dict['surface'] = palettes.get("neutral").tone(6)
            theme_dict['surfaceBright'] = palettes.get("neutral").tone(24)
            theme_dict['surface1'] = palettes.get("neutral").tone(4)
            theme_dict['surface2'] = palettes.get("neutral").tone(10)
            theme_dict['surface3'] = palettes.get("neutral").tone(12)
            theme_dict['surface4'] = palettes.get("neutral").tone(17)
            theme_dict['surface5'] = palettes.get("neutral").tone(22)
        else:
            theme_dict['surfaceDim'] = palettes.get("neutral").tone(87)
            theme_dict['surface'] = palettes.get("neutral").tone(98)
            theme_dict['surfaceBright'] = palettes.get("neutral").tone(98)
            theme_dict['surface1'] = palettes.get("neutral").tone(100)
            theme_dict['surface2'] = palettes.get("neutral").tone(96)
            theme_dict['surface3'] = palettes.get("neutral").tone(94)
            theme_dict['surface4'] = palettes.get("neutral").tone(92)
            theme_dict['surface5'] = palettes.get("neutral").tone(90)
            
    rgb_theme_dict = dict()
    
    for key, value in theme_dict.items():
        theme_dict[key] = hexFromArgb(value)[1:]
        rgb_theme_dict[key+"-r"] = redFromArgb(value)
        rgb_theme_dict[key+"-g"] = greenFromArgb(value)
        rgb_theme_dict[key+"-b"] = blueFromArgb(value)
        
    theme_dict.update(rgb_theme_dict)

    return theme_dict


def get_theme_from_color(color, color_scheme_type):
    theme = themeFromSourceColor(argbFromHex(color), additional_colors)
    return return_theme(theme, color_scheme_type)


def get_theme_from_image(path, color_scheme_type):
    img = Image.open(path)

    basewidth = 64
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    theme = themeFromImage(img, additional_colors)
    return return_theme(theme, color_scheme_type)
