# G-Code Generator and Simulator

## 📌 Project Overview
This project is a Python-based G-Code generator and simulator for CNC milling and 3D printing applications. It allows users to generate G-Code for various shapes (square, circle, triangle, spiral) and visualize the toolpath in 3D.

## 🚀 Features
- **G-Code Generation**:
  - Generate G-Code for square, circle, triangle, and spiral shapes.
  - Customize size, depth, and other parameters.
- **3D Simulation**:
  - Visualize the G-Code toolpath in 3D using `matplotlib`.
  - Supports both static and animated simulations.
- **User-Friendly GUI**:
  - Built with `tkinter` for easy interaction.
  - Save generated G-Code to a file.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/serdarzuli/gcode_generator
   cd gcode_generator
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python main.py 
   ```

## 📂 Project Structure
```
📦 gcode_generator
gcode_generator/
│
├── gcode_generator/              # Main Python package
│   ├── __init__.py               # Package initializer
│   ├── gcode.py                  # G-Code generation functions
│   ├── simulator.py              # G-Code simulation functions
│   ├── utils.py                  # Utility functions
│   └── gui.py                    # GUI application
│
├── tests/                        # Unit tests
│   ├── __init__.py
│   ├── test_gcode.py             # G-Code generation tests
│   └── test_simulator.py         # Simulation tests
│
├── gcode_storage/                # Example G-Code files
│   └── square.gcode
│
├──README.md                      # Project README
├── requirements.txt              # Dependencies
└── main.py                       # Main script to run the application
```

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to fork this repository and contribute! Pull requests are welcome.

## 📬 Contact
For any inquiries, reach out to:
📧 Email: serdar.zuli@gmail.com
🌐 Website: [www.thezuli.com](https://www.thezuli.com)

