"""
The controller handles the workflow of the application and defines the initial state of the cli
"""

import prompts

from actionMapping import map_action


def run():
    def loop(action: any):
        """
        Recursive call executing the next action
        """
        # Execute the action, every action has to return an answer
        answer = action()

        # Map the next action
        action_next = map_action(answer["action"])

        # Recursive call
        loop(action_next)

    # Start the cli by opening the main menu
    loop(prompts.menu_main)
