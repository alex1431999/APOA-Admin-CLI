"""
This module maps actions to their corresponding function which shall be executed
"""
import sys

import actions
import prompts


def map_action(action: str) -> any:
    # General
    if action == prompts.CHOICES_GENERAL["MENU_MAIN"]:
        return prompts.menu_main
    if action == prompts.CHOICES_GENERAL["MENU_SETTINGS"]:
        return prompts.menu_settings
    if action == prompts.CHOICES_GENERAL["MENU_DATABASE"]:
        return prompts.menu_database

    # Main Menu
    if action == prompts.CHOICES_MENU_MAIN["SETTINGS"]:
        return prompts.menu_settings
    if action == prompts.CHOICES_MENU_MAIN["DATABASE"]:
        return prompts.menu_database
    if action == prompts.CHOICES_MENU_MAIN["EXIT"]:
        return sys.exit

    # Settings Menu
    if action == prompts.CHOICES_MENU_SETTINGS["SHOW"]:
        return actions.show_settings
    if action == prompts.CHOICES_MENU_SETTINGS["SET_MONGO_URL"]:
        return actions.set_mongo_url
    if action == prompts.CHOICES_MENU_SETTINGS["BACK"]:
        return prompts.menu_main

    # Database Menu
    if action == prompts.CHOICES_MENU_DATABASE["ADD_USER"]:
        return actions.add_user
    if action == prompts.CHOICES_MENU_DATABASE["BACK"]:
        return prompts.menu_main

    # Default
    return prompts.menu_main
