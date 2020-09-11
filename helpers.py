import json
from os import path

from enums import ENUMS_SETTINGS


def generate_default_settings() -> bool:
    if path.isfile(ENUMS_SETTINGS["FILE_NAME"]):
        return True

    default_settings = {
        ENUMS_SETTINGS["MONGO_URL"]: "mongodb://localhost:27017/default_db",
        ENUMS_SETTINGS["MONGO_DATABASE_NAME"]: "default_db",
    }

    file = open(ENUMS_SETTINGS["FILE_NAME"], "w+")
    file.write(json.dumps(default_settings))
