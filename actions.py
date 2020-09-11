"""
This module defines custom actions which can be undertaken by a user

EVERY ACTION HAS TO RETURN A MESSAGE INDICATING THE NEXT ACTION
"""

import prompts
from enums import ENUMS_SETTINGS
from helpers import load_settings, override_settings


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
