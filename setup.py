from setuptools import setup, find_packages

setup(
    name="gcode_generator",  #
    version="0.1",  # 
    author="Serdar Zuli",  #
    author_email="serdar.zuli@gmail.com",  # Yazar e-posta
    description="A Python-based G-Code generator and simulator for CNC milling and 3D printing.",  #
    long_description=open("README.md").read(),  # 
    long_description_content_type="text/markdown",  # 
    url="https://github.com/serdarzuli/gcode_generator",  # Proje URL'si
    packages=find_packages(),  # 
    install_requires=[  # 
        "matplotlib>=3.5.0",
        "plotly"
    ],
    classifiers=[  # 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "gcode-generator=gcode_generator.main:main",
        ],
    },
    python_requires=">=3.9",  # 
)