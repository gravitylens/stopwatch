#!/bin/bash

# Ensure PyInstaller is installed
pip install pyinstaller

# Compile the Python script into an executable
pyinstaller --onefile stopwatch.py

# Create the destination directory if it doesn't exist
mkdir -p ~/.local/bin/

# Copy the executable to ~/.local/bin/
cp dist/stopwatch ~/.local/bin/

# Clean up build files
rm -rf build dist stopwatch.spec

echo "Executable has been copied to ~/.local/bin/"
