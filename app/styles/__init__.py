import os
import sys


def get_stylesheet():
    # Determine the base directory
    if getattr(sys, "frozen", False):
        base_dir = os.path.join(sys._MEIPASS, "app", "styles")
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    folder = os.path.join(base_dir)
    styles = filter(lambda filename: filename.endswith("css"), os.listdir(folder))
    style_text = ""

    for file in styles:
        style = open(os.path.join(folder, file), "r")
        style_text += "\n" + style.read()

    return style_text
