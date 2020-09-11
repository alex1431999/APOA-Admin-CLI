from pyfiglet import Figlet

from controller import run
from helpers import generate_default_settings


def print_header():
    text = Figlet(font="slant").renderText("APOA Admin")
    print(text)


if __name__ == "__main__":
    generate_default_settings()
    print_header()
    run()
