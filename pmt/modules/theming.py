import os
from material_color_utilities_python import *
import toml


def get_argb_core_theme(color_scheme_type, source_color):
    core_palette = CorePalette.of(source_color)
    theme = {}  # Our resulted theme dict

    color_categories = {
        "primary": "a1",
        "secondary": "a2",
        "tertiary": "a3",
        "error": "error"
    }

    if color_scheme_type == "dark":
        for category, suffix in color_categories.items():
            # Building primary, secondary, tertiary and error colors
            theme[f"{category}"] = getattr(core_palette, suffix).tone(80)
            theme[f"on{category.capitalize()}"] = getattr(core_palette,
                                                          suffix).tone(20)
            theme[f"{category}Container"] = getattr(
                core_palette, suffix).tone(30)
            theme[f"on{category.capitalize()}Container"] = getattr(core_palette,
                                                                   suffix).tone(90)

        # Building surfaces and outlines
        theme["surfaceDim"] = getattr(core_palette, "n1").tone(6)
        theme["surface"] = getattr(core_palette, "n1").tone(6)
        theme["surfaceBright"] = getattr(core_palette, "n1").tone(24)

        theme["surface1"] = getattr(core_palette, "n1").tone(4)
        theme["surface2"] = getattr(core_palette, "n1").tone(10)
        theme["surface3"] = getattr(core_palette, "n1").tone(12)
        theme["surface4"] = getattr(core_palette, "n1").tone(17)
        theme["surface5"] = getattr(core_palette, "n1").tone(22)

        theme["onSurface"] = getattr(core_palette, "n1").tone(90)
        theme["onSurfaceVariant"] = getattr(core_palette, "n2").tone(80)

        theme["outline"] = getattr(core_palette, "n2").tone(60)
        theme["outlineVariant"] = getattr(core_palette, "n2").tone(30)

    if color_scheme_type == "light":
        for category, suffix in color_categories.items():
            # Building primary, secondary, tertiary and error colors
            theme[f"{category}"] = getattr(core_palette, suffix).tone(40)
            theme[f"on{category.capitalize()}"] = core_palette.get(
                suffix).tone(100)
            theme[f"{category}Container"] = getattr(
                core_palette, suffix).tone(90)
            theme[f"on{category.capitalize()}Container"] = core_palette.get(
                suffix).tone(10)

        # Building surfaces and outlines
        theme["surfaceDim"] = getattr(core_palette, "n1").tone(87)
        theme["surface"] = getattr(core_palette, "n1").tone(98)
        theme["surfaceBright"] = getattr(core_palette, "n1").tone(98)

        theme["surface1"] = getattr(core_palette, "n1").tone(100)
        theme["surface2"] = getattr(core_palette, "n1").tone(96)
        theme["surface3"] = getattr(core_palette, "n1").tone(94)
        theme["surface4"] = getattr(core_palette, "n1").tone(92)
        theme["surface5"] = getattr(core_palette, "n1").tone(90)

        theme["onSurface"] = getattr(core_palette, "n1").tone(10)
        theme["onSurfaceVariant"] = getattr(core_palette, "n2").tone(30)

        theme["outline"] = getattr(core_palette, "n2").tone(50)
        theme["outlineVariant"] = getattr(core_palette, "n2").tone(80)

    return theme


def get_argb_additional_theme(colors_scheme_type, source_color):
    additional_theme = {}

    with open(os.path.expanduser("~/.config/pmt/colors.toml")) as file:
        colors = toml.load(file)

    # Iterate over the items in the configuration
    for item in colors['color']:
        name = item['name']
        value = argbFromHex(item['value'])
        blend = item['blend']
        darkTone = item.get('darkTone')
        lightTone = item.get('lightTone')

        if (blend):
            value = Blend.harmonize(value, source_color)
        value_palette = TonalPalette.fromInt(value)

        if colors_scheme_type == "dark":
            if darkTone:
                additional_theme[name] = value_palette.tone(darkTone)
            else:
                additional_theme[name] = value_palette.tone(80)
            additional_theme[f"on{name.capitalize()}"] = value_palette.tone(20)
        else:
            if lightTone:
                additional_theme[name] = value_palette.tone(lightTone)
            else:
                additional_theme[name] = value_palette.tone(40)
            additional_theme[f"on{name.capitalize()}"] = value_palette.tone(
                100)

    return additional_theme


def build_theme(argb_core_theme, argb_additional_theme):
    theme = {**argb_core_theme, **argb_additional_theme}
    rgb_theme = {}

    for key, value in theme.items():
        theme[key] = hexFromArgb(value)[1:]
        rgb_theme[key+"-r"] = redFromArgb(value)
        rgb_theme[key+"-g"] = greenFromArgb(value)
        rgb_theme[key+"-b"] = blueFromArgb(value)

    theme.update(rgb_theme)

    return theme


def get_theme_from_color(color, color_scheme_type):
    source_color = argbFromHex(color)
    argb_core_theme = get_argb_core_theme(color_scheme_type, source_color)
    argb_additional_theme = get_argb_additional_theme(
        color_scheme_type, source_color)

    return build_theme(argb_core_theme, argb_additional_theme)


def get_theme_from_image(path, color_scheme_type):
    img = Image.open(path)

    basewidth = 64
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.BILINEAR)
    
    source_color = sourceColorFromImage(img)
    argb_core_theme = get_argb_core_theme(color_scheme_type, source_color)
    argb_additional_theme = get_argb_additional_theme(
        color_scheme_type, source_color)

    return build_theme(argb_core_theme, argb_additional_theme)
