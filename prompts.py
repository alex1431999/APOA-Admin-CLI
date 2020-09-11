from PyInquirer import prompt

from enums import ENUMS_SETTINGS, ENUMS_CREATE_USER

CHOICES_GENERAL = {
    "MENU_MAIN": "Main Menu",
    "MENU_SETTINGS": "Settings Menu",
    "MENU_DATABASE": "Database Menu",
}

CHOICES_MENU_MAIN = {
    "SETTINGS": "Settings",
    "DATABASE": "Database",
    "EXIT": "Exit",
}

CHOICES_MENU_SETTINGS = {
    "SHOW": "Show",
    "SET_MONGO_URL": "Set Mongo DB URL",
    "BACK": "Back",
}

CHOICES_MENU_DATABASE = {
    "ADD_USER": "Add user",
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


def menu_database():
    options = [
        {
            "type": "list",
            "message": "Select action",
            "name": "action",
            "choices": [{"name": CHOICES_MENU_DATABASE[key]} for key in CHOICES_MENU_DATABASE]
        }
    ]
    return prompt(options)


def ask_mongo_url():
    questions = [
        {
            "type": "input",
            "name": ENUMS_SETTINGS["MONGO_URL"],
            "message": "Enter your Mongo URL",
        },
    ]
    return prompt(questions)


def ask_username_creation():
    questions = [
        {
            "type": "input",
            "name": ENUMS_CREATE_USER["USERNAME"],
            "message": "Enter a username",
        },
    ]
    return prompt(questions)


def ask_password_creation():
    questions = [
        {
            "type": "input",
            "name": ENUMS_CREATE_USER["PASSWORD"],
            "message": "Enter a password",
        },
    ]
    return prompt(questions)
