import json
from os import path

from common.mongo.controller import MongoController

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


def load_settings() -> dict:
    with open(ENUMS_SETTINGS["FILE_NAME"], "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}
    return data


def override_settings(data: dict):
    with open(ENUMS_SETTINGS["FILE_NAME"], "w") as f:
        f.seek(0)  # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()  # remove remaining part


def get_mongo_controller() -> MongoController:
    settings = load_settings()
    mongo_url = settings[ENUMS_SETTINGS["MONGO_URL"]]
    db_name = settings[ENUMS_SETTINGS["MONGO_DATABASE_NAME"]]

    controller = MongoController(mongo_url, db_name)

    return controller
