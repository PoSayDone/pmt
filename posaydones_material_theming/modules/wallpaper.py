import subprocess
import os


def set_wallpaper(wallpaper_path, wallpaper_program):
    match wallpaper_program:
        case "hyprpaper":
            file = open(os.path.expanduser(
                "~/.config/hypr/hyprpaper.conf"), "w")
            file.write(
                f"preload={wallpaper_path} \
                \nwallpaper=,{wallpaper_path}")
            file.close()
            subprocess.run("killall hyprpaper", shell=True,
                           capture_output=False)
            subprocess.run("hyprpaper > /dev/null 2>&1 & disown",
                           shell=True, capture_output=False)
        case "swww":
            subprocess.run(
                f"swww img {wallpaper_path} --transition-step=10 --transition-fps=90",
                shell=True, capture_output=False)
