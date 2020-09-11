"""
This module defines custom actions which can be undertaken by a user

EVERY ACTION HAS TO RETURN A MESSAGE INDICATING THE NEXT ACTION
"""
import json

import prompts
from enums import ENUMS_SETTINGS


def set_mongo_url():
    url = prompts.ask_mongo_url()[ENUMS_SETTINGS["MONGO_URL"]]

    with open("settings.json", "r+") as f:
        try:
            data = json.load(f)
        except:
            data = {}

        data[ENUMS_SETTINGS["MONGO_URL"]] = url

        f.seek(0)  # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()  # remove remaining part

    return {"action": prompts.CHOICES_GENERAL["MENU_MAIN"]}
