"""
This module maps actions to their corresponding function which shall be executed
"""
import prompts


def map_action(action: str) -> any:
    # Main Menu
    if action == prompts.CHOICES_MENU_MAIN["SETTINGS"]:
        return prompts.menu_settings

    # Settings Menu
    if action == prompts.CHOICES_MENU_SETTINGS["BACK"]:
        return prompts.menu_main

    # Default
    return prompts.menu_main
