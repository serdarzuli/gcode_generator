"""
G-Code Generator and Simulator GUI using tkinter.
"""
import tkinter as tk
from tkinter import messagebox, filedialog
from gcode_generator.gcode import generate_square, generate_circle
from gcode_generator.animation import  visualize_gcode_3d_animated
from gcode_generator.simulator import visualize_gcode_3d

class GCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("G-Code Generator and Simulator")
        self.root.geometry("600x400")

        # Variables
        self.shape_var = tk.StringVar(value="square")
        self.size_var = tk.DoubleVar(value=10.0)
        self.depth_var = tk.DoubleVar(value=2.0)
        self.gcode = ""

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange widgets in the GUI."""
        # Shape selection
        shape_frame = tk.LabelFrame(self.root, text="Shape", padx=10, pady=10)
        shape_frame.pack(fill="x", padx=10, pady=5)

        tk.Radiobutton(shape_frame, text="Square", variable=self.shape_var, value="square").pack(anchor="w")
        tk.Radiobutton(shape_frame, text="Circle", variable=self.shape_var, value="circle").pack(anchor="w")

        # Size and depth input
        input_frame = tk.LabelFrame(self.root, text="Parameters", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(input_frame, text="Size (mm):").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(input_frame, textvariable=self.size_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Depth (mm):").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(input_frame, textvariable=self.depth_var).grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(button_frame, text="Generate G-Code", command=self.generate_gcode).pack(side="left", padx=5)
        tk.Button(button_frame, text="Simulate G-Code", command=self.simulate_gcode).pack(side="left", padx=5)
        tk.Button(button_frame, text="Save G-Code", command=self.save_gcode).pack(side="left", padx=5)

        # Output text box
        output_frame = tk.LabelFrame(self.root, text="Generated G-Code", padx=10, pady=10)
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.output_text = tk.Text(output_frame, height=10)
        self.output_text.pack(fill="both", expand=True)

    def generate_gcode(self):
        """Generate G-Code based on user input."""
        shape = self.shape_var.get()
        size = self.size_var.get()
        depth = self.depth_var.get()

        if shape == "square":
            self.gcode = generate_square(size, depth)
        elif shape == "circle":
            self.gcode = generate_circle(size, depth)

        self.output_text.delete(1.0, tk.END)  # Clear previous output
        self.output_text.insert(tk.END, self.gcode)

    def simulate_gcode(self):
        """Simulate the generated G-Code."""
        if not self.gcode:
            messagebox.showwarning("No G-Code", "Please generate G-Code first.")
            return

        # Choose between static or animated simulation
        visualize_gcode_3d(self.gcode)  # Static 3D visualization
        # visualize_gcode_3d_animated(self.gcode)  # Animated 3D visualization

    def save_gcode(self):
        """Save the generated G-Code to a file."""
        if not self.gcode:
            messagebox.showwarning("No G-Code", "Please generate G-Code first.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".gcode",
            filetypes=[("G-Code Files", "*.gcode"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.gcode)
            messagebox.showinfo("Success", f"G-Code saved to {file_path}")

def main():
    root = tk.Tk()
    app = GCodeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()