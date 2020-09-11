from PyInquirer import prompt

CHOICES_MENU_MAIN = {
    "SETTINGS": "Settings",
}

CHOICES_MENU_SETTINGS = {
    "SET_MONGO_URL": "Set Mongo DB URL",
    "BACK": "Back",
}


def menu_main():
    options = [
        {
            "type": "list",
            "message": "Select action",
            "name": "action",
            "choices": [{"name": CHOICES_MENU_MAIN[key]} for key in CHOICES_MENU_MAIN]
        }
    ]
    return prompt(options)


def menu_settings():
    options = [
        {
            "type": "list",
            "message": "Select action",
            "name": "action",
            "choices": [{"name": CHOICES_MENU_SETTINGS[key]} for key in CHOICES_MENU_SETTINGS]
        }
    ]
    return prompt(options)
