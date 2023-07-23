from pmt.misc.utils import proceed_theme, add_slash_if_needed 
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib
import os
import toml


class PMT(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
       # Load the current directory from the TOML file
        current_directory = self.load_current_directory()

        # Create a Builder
        global builder
        builder = Gtk.Builder()
        builder.add_from_file("data/pmt.ui")

        apply_button = builder.get_object("apply_button")
        apply_button.connect("clicked", self.proceed)

        directory_entry = builder.get_object("directory_entry")
        directory_entry.set_text(current_directory)
        directory_button = builder.get_object("directory_button")
        directory_button.connect("clicked", self.show_open_dialog)

        image_dropdown = builder.get_object("image_dropdown")
        image_dropdown.connect("notify::selected-item", self.dropdown_callback)
        if current_directory != (None or ""):
            self.on_directory_entry_change(directory_entry)
            self.dropdown_callback(image_dropdown, '')

        # Obtain and show the main window
        self.win = builder.get_object("main_window")
        # Application will close once it no longer has active windows attached to it
        self.win.set_application(self)
        self.win.present()

        self.open_dialog = builder.get_object("directory_dialog")
        self.open_dialog.set_title("Select a File")
        directory_entry.connect("changed", self.on_directory_entry_change)

    def load_current_directory(self):
        try:
            with open(os.path.expanduser('~/.config/pmt/config.toml'), 'r') as f:
                config = toml.load(f)
                return config.get('current_directory', '')
        except:
            return ''

    def save_current_directory(self, current_directory):
        config_path = os.path.expanduser('~/.config/pmt/config.toml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = toml.load(f)
        else:
            config = {}

        config['current_directory'] = current_directory

        with open(config_path, 'w') as f:
            toml.dump(config, f)

    def dropdown_callback(self, dropdown, smth):
        global current_image_path
        image = builder.get_object("wallpaper_image")
        directory_entry = builder.get_object("directory_entry")
        current_image_path = add_slash_if_needed(
            directory_entry.get_buffer().get_text()) + \
            dropdown.get_selected_item().get_string()
        self.update_image(current_image_path, image)

    def show_open_dialog(self, button):
        parent_window = self.get_active_window()
        self.open_dialog.open(parent_window, None,
                              self.open_dialog_open_callback)

    def update_image_dropdown(self, directory, dropdown):
        try:
            dir_contents = os.listdir(directory)
            string_list = Gtk.StringList()
            for item in dir_contents:
                string_list.append(item)

            # Set the menu for the menu button
            dropdown.set_model(string_list)
        except:
            ""

    def on_directory_entry_change(self, entry):
        image_dropdown = builder.get_object("image_dropdown")
        current_directory = entry.get_text()
        self.save_current_directory(current_directory)
        self.update_image_dropdown(current_directory, image_dropdown)

    def update_image(self, path, image):
        image.set_from_file(path)

    def open_dialog_open_callback(self, dialog, result):
        try:
            file = dialog.open_finish(result)
            if file is not None:
                directory_entry = builder.get_object("directory_entry")
                directory_entry.set_text(file.get_path())
                current_directory = file.get_path()

        except GLib.Error as error:
            print(f"Error opening file: {error.message}")

    def proceed(self, button):
        proceed_theme(current_image_path, "dark")
