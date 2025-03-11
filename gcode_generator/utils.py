"""
Utility functions for file operations and validations.
"""
import os

def save_gcode(gcode: str, filename: str):
    """
    Saves G-Code to a file.

    Args:
        gcode (str): G-Code to save.
        filename (str): Name of the file to save.
    """
    with open(filename, "w") as file:
        file.write(gcode)

def load_gcode(filename: str) -> str:
    """
    Loads G-Code from a file.

    Args:
        filename (str): Name of the file to load.

    Returns:
        str: Loaded G-Code.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not exist.")
    with open(filename, "r") as file:
        return file.read()