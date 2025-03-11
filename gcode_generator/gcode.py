import math
"""
G-Code generation module.
"""

def generate_square(size: float, depth: float) -> str:
    """
    Generates G-Code for a square shape.

    Args:
        size (float): Side length of the square in mm.
        depth (float): Cutting depth in mm.

    Returns:
        str: Generated G-Code as a string.
    """
    return f"""
G21        ; Set units to millimeters
G90        ; Absolute positioning
G0 Z5      ; Move Z axis up
G0 X0 Y0   ; Move to starting point
G1 Z-{depth} F100 ; Move Z axis down to cutting depth
G1 X{size} ; Move along X axis
G1 Y{size} ; Move along Y axis
G1 X0      ; Move back to starting X position
G1 Y0      ; Move back to starting Y position
G0 Z5      ; Move Z axis up
"""

def generate_circle(side_length: float, depth: float) -> str:
    """
    Generates G-Code for an equilateral triangle.

    Args:
        side_length (float): Length of each side in mm.
        depth (float): Cutting depth in mm.

    Returns:
        str: Generated G-Code as a string.
    """
    height = (math.sqrt(3) / 2) * side_length  # Height of an equilateral triangle
    gcode = [
        "G21",        # Set units to millimeters
        "G90",        # Absolute positioning
        "G0 Z5",      # Move Z axis up
        "G0 X0 Y0",   # Move to starting point (bottom-left corner)
        f"G1 Z-{depth} F100",  # Move Z axis down to cutting depth
        f"G1 X{side_length} Y0",  # Move to bottom-right corner
        f"G1 X{side_length / 2} Y{height}",  # Move to top corner
        "G1 X0 Y0",   # Move back to starting point
        "G0 Z5",      # Move Z axis up
    ]
    return "\n".join(gcode)