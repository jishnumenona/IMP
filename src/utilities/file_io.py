import os
import shutil
import json

"""
================ DIRECTORY FUNCTIONS ====================
"""


def list_directory(path: str) -> list[str]:
    """
    Lists all files and directories within a specified directory.

    Args:
        path: The directory path.

    Returns:
        A list of filenames and directory names within the specified path.
    """
    entries = os.listdir(path)
    return entries


def create_directory(path: str) -> None:
    """
    Creates a new directory at the specified path.

    Args:
        path: The directory path to create.
    """
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def delete_directory(path: str) -> None:
    """
    Deletes a directory at the specified path.

    Args:
        path: The directory path to delete.
    """
    try:
        os.rmdir(path)
    except OSError as error:
        print(f"Error deleting directory: {error}")


def get_file_path(filename: str, path: str) -> str | None:
    """
    Searches for a file within a directory and returns its path.

    Args:
        filename: The name of the file to search for.
        path: The directory path to search in.

    Returns:
        The full path of the file if found, None otherwise.
    """
    for entry in os.listdir(path):
        if entry == filename:
            return os.path.join(path, entry)
    return None


def copy_file(src_path: str, dst_path: str) -> None:
    """
    Copies a file from one location to another.

    Args:
        src_path: The source file path.
        dst_path: The destination file path.
    """
    shutil.copyfile(src_path, dst_path)


def move_file(src_path: str, dst_path: str) -> None:
    """
    Moves a file from one location to another.

    Args:
        src_path: The source file path.
        dst_path: The destination file path.
    """
    shutil.move(src_path, dst_path)


"""
    ================ END OF DIRECTORY FUNCTIONS ====================
"""


"""
================ JSON CONFIG FUNCTIONS ====================
"""


def read_json_config(path):
    """
    Reads a JSON configuration file and returns a dictionary representation of its data.

    Args:
        path: The path to the JSON configuration file.

    Returns:
        A dictionary containing the data from the JSON file.
    """
    with open(path, "r") as f:
        return json.load(f)


def write_json_config(path, data):
    """
    Writes a dictionary representation of data to a JSON configuration file.

    Args:
        path: The path to write the JSON configuration file.
        data: The dictionary containing the data to write.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def get_config_value(key, path):
    """
    Retrieves the value of a nested key within the JSON configuration file.

    Args:
        key: A string representing the key to retrieve.
        path: The path to the JSON configuration file.

    Returns:
        The value associated with the specified key.
    """
    data = read_json_config(path)
    keys = key.split(".")
    for k in keys:
        data = data[k]
    return data


def set_config_value(key, value, path):
    """
    Sets the value of a nested key within the JSON configuration file.

    Args:
        key: A string representing the key to set.
        value: The value to set for the specified key.
        path: The path to the JSON configuration file.
    """
    data = read_json_config(path)
    keys = key.split(".")
    for k in keys[:-1]:
        data = data.setdefault(k, {})
    data[keys[-1]] = value
    write_json_config(path, data)


def delete_config_value(key, path):
    """
    Deletes a nested key from the JSON configuration file.

    Args:
        key: A string representing the key to delete.
        path: The path to the JSON configuration file.
    """
    data = read_json_config(path)
    keys = key.split(".")
    for k in keys[:-1]:
        data = data[k]
    del data[keys[-1]]
    write_json_config(path, data)


# Additional functions and functionalities can be added here

