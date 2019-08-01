#!/bin/bash
mkdir -p ~/.local/share/send_to_emailchef
cp -rf lib/* ~/.local/share/send_to_emailchef
chmod +x ~/.local/share/send_to_emailchef/__init__.py
cp activator/send_to_emailchef.bash ~/.local/share/nautilus/scripts