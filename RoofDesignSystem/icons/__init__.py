import os


def get_icons():
    icon_folder_path = os.path.dirname(__file__)
    images = os.listdir(icon_folder_path)
    icon_path_by_filename = {}

    for filepath in images:
        image_name = os.path.splitext(filepath)[0]
        image_filepath = os.path.join(icon_folder_path, filepath)
        icon_path_by_filename[image_name] = image_filepath

    return icon_path_by_filename
