"""
MANUEL TEST
Main script to run the G-Code generator and simulator.
"""
from gcode_generator.gcode import generate_square
from gcode_generator.simulator import visualize_gcode_3d_plotly
from gcode_generator.utils import save_gcode
from gcode_generator.animation import visualize_gcode_3d_animated

def main():
    size = 10.0  # mm
    depth = 2.0  # mm

    # Generate G-Code
    gcode = generate_square(size, depth)
    print("Generated G-Code:\n", gcode)

    # Save G-Code to a file
    save_gcode(gcode, "gcode_storage/animated_square.gcode")

    # Visualize G-Code
    visualize_gcode_3d_plotly(gcode)
    # visualize_gcode_3d_animated(gcode)


if __name__ == "__main__":
    main()