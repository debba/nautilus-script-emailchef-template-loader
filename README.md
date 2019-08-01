Nautilus eMailChef Template Loader
-------------------

This python script allow you to easily load your HTML files as eMailChef templates from Nautilus File Manager.

You can select multiple HTML files and use the context "Script" menu.

Requirements
------------

- Python3
- GTK3
- python3-gi
- zenipy 

Installation
-------------

Install it using install.sh:

```	
$ bash install.sh
```

Configuration
-------------

You can setup a configuration with your login credentials in order to remember next times.
You should create a settings.json file inside ~/.local/share/send_to_emailchef/conf as the following:

```	
{
    "username" : "your eMailChef username",
    "password" : "your eMailChef password"
}
```

Usage
------

From Nautilus File Manager you can select your HTML files and from context menu *Script* and select *sendtoemailchef.bash* .

![image preview](https://www.debbaweb.it/nautilus-script/emailchef/preview.png)

Notice
--------
Remember D&D templates follow technical logics, something could break, if HTML template is malformed.

Credits
--------

- [eMailChef](https://www.emailchef.com]) - email marketing platform 

License
--------
_*Nautilus eMailChef Template Loader*_ is licensed under : The Apache Software License, Version 2.0. You can find a copy of the license (http://www.apache.org/licenses/LICENSE-2.0.txt)

Enjoy ;)