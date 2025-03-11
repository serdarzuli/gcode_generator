import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # for 3D graphics

def visualize_gcode_3d(gcode: str):
    """
    Visualizes G-Code in 3D with colored movements.
    """
    x, y, z = [0], [0], [0]  # Start at the origin (0, 0, 0)
    colors = []  # Store colors for each segment
    current_color = 'b'  # Default color (blue)

    for line in gcode.split("\n"):
        line = line.strip()  # Remove leading/trailing whitespace
        if not line or line.startswith(";"):  # Skip empty lines and comments
            continue

        if line.startswith("G0"):  # Rapid move
            current_color = 'r'  # Red
        elif line.startswith("G1"):  # Linear move
            current_color = 'b'  # Blue

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

            colors.append(current_color)  # Add color for the current segment

    # Plot the G-Code path in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot each segment with its corresponding color
    for i in range(1, len(x)):
        ax.plot(x[i-1:i+1], y[i-1:i+1], z[i-1:i+1], color=colors[i-1], marker='o')

    # Set labels and title
    ax.set_xlabel("X Axis (mm)")
    ax.set_ylabel("Y Axis (mm)")
    ax.set_zlabel("Z Axis (mm)")
    ax.set_title("3D G-Code Simulation with Colored Movements")

    plt.show()

def visualize_gcode_3d_plotly(gcode: str):
    """
    Visualizes G-Code in 3D using Plotly.
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

    # Create a 3D plot using Plotly
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='lines+markers')])
    fig.update_layout(
        title="3D G-Code Simulation with Plotly",
        scene=dict(
            xaxis_title="X Axis (mm)",
            yaxis_title="Y Axis (mm)",
            zaxis_title="Z Axis (mm)",
        ),
    )
    fig.show()