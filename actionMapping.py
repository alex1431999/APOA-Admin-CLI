"""
This module maps actions to their corresponding function which shall be executed
"""
import actions
import prompts


def map_action(action: str) -> any:
    # General
    if action == prompts.CHOICES_GENERAL["MENU_MAIN"]:
        return prompts.menu_main

    # Main Menu
    if action == prompts.CHOICES_MENU_MAIN["SETTINGS"]:
        return prompts.menu_settings

    # Settings Menu
    if action == prompts.CHOICES_MENU_SETTINGS["BACK"]:
        return prompts.menu_main
    if action == prompts.CHOICES_MENU_SETTINGS["SET_MONGO_URL"]:
        return actions.set_mongo_url

    # Default
    return prompts.menu_main
