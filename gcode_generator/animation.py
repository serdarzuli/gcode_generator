"""
G-Code simulation module with 3D animation.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def visualize_gcode_3d_animated(gcode: str):
    """
    Visualizes G-Code in 3D with animation.

    Args:
        gcode (str): G-Code to visualize.
    """
    x, y, z = [0], [0], [0]  # Start at the origin (0, 0, 0)
    for line in gcode.split("\n"):
        line = line.strip()  # Remove leading/trailing whitespace
        if not line or line.startswith(";"):  # Skip empty lines and comments
            continue

        if line.startswith("G0") or line.startswith("G1"):  # Handle G0 and G1 commands
            parts = line.split()
            x_value = None
            y_value = None
            z_value = None
            for part in parts:
                if part.startswith("X"):
                    try:
                        x_value = float(part[1:])  # Extract X value
                    except ValueError:
                        continue  # Skip invalid X values
                elif part.startswith("Y"):
                    try:
                        y_value = float(part[1:])  # Extract Y value
                    except ValueError:
                        continue  # Skip invalid Y values
                elif part.startswith("Z"):
                    try:
                        z_value = float(part[1:])  # Extract Z value
                    except ValueError:
                        continue  # Skip invalid Z values

            # Update X, Y, and Z coordinates
            if x_value is not None:
                x.append(x_value)
            else:
                x.append(x[-1])  # Keep the last X value if no new X value is provided

            if y_value is not None:
                y.append(y_value)
            else:
                y.append(y[-1])  # Keep the last Y value if no new Y value is provided

            if z_value is not None:
                z.append(z_value)
            else:
                z.append(z[-1])  # Keep the last Z value if no new Z value is provided

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel("X Axis (mm)")
    ax.set_ylabel("Y Axis (mm)")
    ax.set_zlabel("Z Axis (mm)")
    ax.set_title("3D G-Code Animation")

    # Initialize an empty line for the animation
    line, = ax.plot([], [], [], lw=2, marker='o')

    # Set axis limits
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))
    ax.set_zlim(min(z), max(z))

    def init():
        """Initialize the line."""
        line.set_data([], [])
        line.set_3d_properties([])
        return line,

    def animate(i):
        """Update the line for each frame."""
        line.set_data(x[:i], y[:i])
        line.set_3d_properties(z[:i])
        return line,

    # Create the animation
    ani = animation.FuncAnimation(
        fig, animate, frames=len(x), init_func=init, interval=100, blit=True
    )

    plt.show()