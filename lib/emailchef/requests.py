import requests
import json


def login(username, password):
    payload = {
        "username": username,
        "password": password
    }
    print("Payload: ", payload)

    r = requests.post("https://app.emailchef.com/api/login", data=payload)
    result = r.json()
    if r.status_code is 200:
        if result["authkey"]:
            return result["authkey"]
    else:
        print("Error: %s" % result['message'])

    return False


def load_template(authkey, html, name, new_dd):
    payload = {
        "html": html,
        "raw_html": html,
        "name": name,
        "new_dd": new_dd
    }

    headers = {'authkey': authkey}

    r = requests.post("https://app.emailchef.com/apps/api/v1/mytemplates", headers=headers, data=json.dumps({
        "instance_in": payload
    }))
    new_id = r.text.strip().replace('"', '')
    if r.status_code is 200:
        return int(new_id)

    return -1
