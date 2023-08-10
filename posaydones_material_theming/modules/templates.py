import os
import subprocess
import chevron
import toml


def process_template(file_path, output_file_path, theme, hook):
    """
    function for processing items from config

    :param file_path string: path to template file
    :param output_file_path string: path to output after template has been processed
    :param theme dict: theme dict
    :param hook string: shell string to proceed after template has been processed
    """
    with open(file_path, 'r') as file:
        template = file.read()

    output = chevron.render(template, theme)

    with open(output_file_path, 'w') as file:
        file.write(output)

    if hook:
        subprocess.Popen(hook, shell=True, executable="/bin/bash")


def handle_templates(theme):
    """
    handles templates from config file

    :param theme dict: theme dict
    """
    with open(os.path.expanduser("~/.config/pmt/config.toml"), encoding="utf8") as file:
        config = toml.load(file)

    # Iterate over the items in the configuration
    for item in config['item']:
        file_path = item['file']
        template = item['template']
        hook = item.get('hook')
        process_template(os.path.expanduser(f"~/.config/pmt/templates/{template}.mustache"),
                         os.path.expanduser(file_path),
                         theme,
                         hook)
