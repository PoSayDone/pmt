# Posaydone's material theming
Small gui + cli app for managing your colorscheme using material color utilities

<p align="center">
  <img src="https://github.com/PoSayDone/pmt/assets/29358657/b86ba512-b505-4820-a08e-fb0e48ec8054" alt="drawing" width="600"/>
</p>

# Installation

using pipx
`pipx install posaydones-material-theming`

# Usage

Pass path to folder with your images to pick random one or pass image path to set it.

Also there are different flags, you could see them running `pmt -h`

# Configuring

Config folder is `~/.config/pmt/`. There are two configuration filies for configuration `config.toml` and `colors.toml`.

## config.toml

In config.toml file you write down all apps you want to style.

```
[[item]]
file = "file to process with template"
hook = "command to run after template is processed"
template = "template name"
```

## colors.toml

If you want to add more colors, you could use colors.toml file. You should add colors to colors.toml this way:

```
[[color]]
name="red"
value="#f38ba8"
blend=true
darkTone=...
lightTone=...
```

Only required options is name and value, all others are optional.

* Name is the identifier which you should use in your templates (checkout Main colors section in templates). 
* Value is hex representation of color.
* Blend is option to harmonize your given color, with colorscheme you've got, it's cool feature but sometimes it gives ugly colors (for example yellow), so I'm not enabling it on all colors. 
* DarkTone and LightTone, these options gives opportunity to change the tone of color in light and dark scheme.


## Templates
Templates should be in ~/.config/pmt/templates/ folder and be .mustache file type.

### Example template

```
//examaple.mustache

background: #{{surface}};
foreground: #{{onSurface}};
accent: #{{primary}};
on_accent: #{{onPrimary}};
```


List of default colors:

### Surfaces, outlines:
```
surface
surfaceDim
surfaceBright
surface1
surface2
surface3
surface4
surface5
onSurface
onSurfaceVariant
outline
outlineVariant
```

### Main colors:
```
replace color with primary, secondary, tertiary, error or custom color name

color
onColor
colorContainer
onColorContainer
```
