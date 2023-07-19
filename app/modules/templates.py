import os
import subprocess
import chevron
import toml


def process_template(file_path, output_file_path, theme, hook):
    with open(file_path, 'r') as file:
        template = file.read()
    
    output = chevron.render(template, theme)
    
    with open(output_file_path, 'w') as file:
        file.write(output)
        
    if hook:
        subprocess.run(hook, shell=True, executable="/bin/bash")


def handle_templates(theme):
    with open(os.path.expanduser("~/.config/pmt/config.toml")) as file:
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
