# Stopwatch

This is a terminal-based stopwatch application written in Python. It displays the elapsed time in the terminal using large digits. The spacebar starts and stops the timer, 'c' clears the timer, 'p' toggles the display of past times, and 'q' quits the application.

## Requirements

- Python 3.x
- `curses` library (usually included with Python)
- `PyInstaller` for creating an executable

## Running the Application

To run the application, navigate to the project directory and execute the script with Python:

```sh
python3 stopwatch.py
```

## Compiling to an Executable

To compile the application into a standalone executable, follow these steps:

1. Install `PyInstaller`:
   ```sh
   pip install pyinstaller
   ```

2. Use `PyInstaller` to create the executable:
   ```sh
   pyinstaller --onefile stopwatch.py
   ```

3. The executable will be created in the `dist` directory.

## Usage

- Press the spacebar to start and stop the timer.
- Press 'c' to clear the timer.
- Press 'p' to toggle the display of past times.
- Press 'q' to quit the application.
