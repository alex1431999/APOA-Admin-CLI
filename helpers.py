import json

from os import path

SETTINGS_FILE_NAME = "settings.json"


def generate_default_settings() -> bool:
    if path.isfile(SETTINGS_FILE_NAME):
        return True

    default_settings = {
        "MONGO_URL": "mongodb://localhost:27017/default_db",
        "MONGO_DATABASE_NAME": "default_db",
    }

    file = open(SETTINGS_FILE_NAME, "w+")
    file.write(json.dumps(default_settings))
