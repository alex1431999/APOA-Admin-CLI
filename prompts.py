from PyInquirer import prompt

from enums import ENUMS_SETTINGS

CHOICES_GENERAL = {
    "MENU_MAIN": "Main Menu",
    "MENU_SETTINGS": "Settings Menu",
}

CHOICES_MENU_MAIN = {
    "SETTINGS": "Settings",
}

CHOICES_MENU_SETTINGS = {
    "SHOW": "Show",
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


def ask_mongo_url():
    questions = [
        {
            'type': 'input',
            'name': ENUMS_SETTINGS["MONGO_URL"],
            'message': 'Enter your Mongo URL',
        },
    ]
    return prompt(questions)
