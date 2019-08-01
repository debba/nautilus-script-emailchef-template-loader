#!/usr/bin/env python

import zenipy
from validate_email import validate_email
from datetime import date
from emailchef import requests
import os
import json
import magic

if __name__ == "__main__":

    SETTINGS_FILE = os.path.dirname(os.path.realpath(__file__)) + "/conf/settings.json"

    pathsValid = []
    paths = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].splitlines()
    for index, path in enumerate(paths):
        if not os.path.isdir(path):
            mimeType = magic.from_file(path, mime=True)
            if mimeType == "text/html":
                pathsValid.append(path)

    if len(pathsValid) == 0:
        zenipy.zenipy.error(title='Error', text="File selected are not valid.")
        exit(0)

    emailchef_username = None
    emailchef_password = None

    print("Checking settings file in %s exists ... " % SETTINGS_FILE)

    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE) as json_file:
            data = json.load(json_file)
            if "username" in data:
                emailchef_username = data['username']
            if "password" in data:
                emailchef_password = data['password']
            print("From JSON", {
                "username": emailchef_username,
                "password": emailchef_password
            })

    zenipy.zenipy.message(title='eMailChef connector',
                          text='%d files are ready to be transfer to eMailChef' % len(pathsValid))

    if emailchef_username is None or emailchef_password is None:

        emailchef_username = zenipy.zenipy.entry(text='Please provide your eMailChef username',
                                                 title='eMailChef credentials')
        if emailchef_username is None or not validate_email(emailchef_username):
            zenipy.zenipy.error(title='Data provided is wrong',
                                text='Please insert a valid email as eMailChef username')
            exit(0)

        emailchef_password = zenipy.zenipy.password(text='eMailChef password', title='eMailChef credentials')

    authkey = requests.login(emailchef_username, emailchef_password)

    if authkey is False:
        zenipy.zenipy.error(title='Data provided are wrong', text='eMailChef credentials are wrong')
        exit(0)

    for index, template in enumerate(pathsValid):
        with open(template, 'r') as f:
            dd_template = zenipy.zenipy.question(title='Template Type', text='Is it a Drag and Drop template?')

            template_name = zenipy.zenipy.entry(text='Assign template name',
                                                title='Template name for %s' % template,
                                                placeholder="Import from Gnome Nautilus: %s" % date.today())
            new_id = requests.load_template(authkey, f.read(), template_name, int(dd_template))
            if new_id == -1:
                zenipy.zenipy.error(title='Some errors occurred', text="Unable to import template %s" % template)
            else:
                zenipy.zenipy.message(title='Success!', text="Generate new template ID : %d" % new_id)
