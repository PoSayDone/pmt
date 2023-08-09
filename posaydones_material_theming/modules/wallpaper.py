import subprocess
import os


def set_wallpaper(wallpaper_path, wallpaper_program):
    """
    Wallpaper setting function

    :param wallpaper_path string: Path to wallpaper
    :param wallpaper_program string: Wallpaper setter name
    :raises Exception: Error in setting wallpaper
    """
    try:
        match wallpaper_program:
            case "hyprpaper":
                with open(os.path.expanduser(
                        "~/.config/hypr/hyprpaper.conf"), "w") as file:
                    file.write(
                        f"preload={wallpaper_path} \
                            \nwallpaper=,{wallpaper_path}")
                    file.close()
                subprocess.run("killall hyprpaper", shell=True,
                               capture_output=False, check=False)
                subprocess.run("hyprpaper > /dev/null 2>&1 & disown",
                               shell=True, capture_output=False, check=True)
            case "swww":
                subprocess.Popen(
                    f"swww img {wallpaper_path} --transition-step=10 --transition-fps=90",
                    shell=True)
            case "swaybg":
                subprocess.Popen(
                    f"swaybg -i {wallpaper_path} -m fit", shell=True)
    except Exception as wallpaper_error:
        print("Error changing wallpaper:", wallpaper_error)
