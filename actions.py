"""
This module defines custom actions which can be undertaken by a user

EVERY ACTION HAS TO RETURN A MESSAGE INDICATING THE NEXT ACTION
"""

import prompts
from enums import ENUMS_SETTINGS, ENUMS_CREATE_USER
from helpers import load_settings, override_settings, get_mongo_controller


def set_mongo_url():
    url = prompts.ask_mongo_url()[ENUMS_SETTINGS["MONGO_URL"]]

    settings = load_settings()
    settings[ENUMS_SETTINGS["MONGO_URL"]] = url
    override_settings(settings)

    return {"action": prompts.CHOICES_GENERAL["MENU_MAIN"]}


def show_settings():
    data = load_settings()

    print("=========DATA=========")
    print(data)
    print("=========DATA=========")

    return {"action": prompts.CHOICES_GENERAL["MENU_SETTINGS"]}


def add_user():
    username = prompts.ask_username_creation()[ENUMS_CREATE_USER["USERNAME"]]

    while username is None or username == "":
        print("Please enter a non empty username")
        username = prompts.ask_username_creation()[ENUMS_CREATE_USER["USERNAME"]]

    password = prompts.ask_password_creation()[ENUMS_CREATE_USER["PASSWORD"]]

    while username is None or username == "":
        print("Please enter a non empty password")
        password = prompts.ask_password_creation()[ENUMS_CREATE_USER["PASSWORD"]]

    controller = get_mongo_controller()
    controller.add_user(username, password)

    return {"action": prompts.CHOICES_GENERAL["MENU_DATABASE"]}
