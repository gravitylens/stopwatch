import curses
import time

# Define large digit representations similar to tty-clock
DIGITS = {
    '0': ["██████",
          "██  ██",
          "██  ██",
          "██  ██",
          "██████"],
    '1': ["  ██  ",
          "  ██  ",
          "  ██  ",
          "  ██  ",
          "  ██  "],
    '2': ["██████",
          "    ██",
          "██████",
          "██    ",
          "██████"],
    '3': ["██████",
          "    ██",
          " █████",
          "    ██",
          "██████"],
    '4': ["██  ██",
          "██  ██",
          "██████",
          "    ██",
          "    ██"],
    '5': ["██████",
          "██    ",
          "██████",
          "    ██",
          "██████"],
    '6': ["█████ ",
          "██    ",
          "██████",
          "██  ██",
          "██████"],
    '7': ["██████",
          "    ██",
          "    ██",
          "    ██",
          "    ██"],
    '8': ["██████",
          "██  ██",
          "██████",
          "██  ██",
          "██████"],
    '9': ["██████",
          "██  ██",
          "██████",
          "    ██",
          "██████"],
    ':': ["      ",
          "  ██  ",
          "      ",
          "  ██  ",
          "      "],
    '.': ["      ",
          "      ",
          "      ",
          "  ██  ",
          "  ██  "]
}

def draw_large_digit(stdscr, digit, y, x):
    for i, line in enumerate(DIGITS[digit]):
        stdscr.addstr(y + i, x, line, curses.color_pair(1))

def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Clear screen
    stdscr.clear()
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True)  # Make getch non-blocking
    stdscr.timeout(100)  # Set getch timeout to 100ms

    start_time = 0
    elapsed_time = 0
    running = False

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Display the current time in the upper right corner
        current_time_str = time.strftime('%H:%M:%S')
        stdscr.addstr(0, width - len(current_time_str) - 1, current_time_str)

        # Display the elapsed time
        elapsed_time = time.time() - start_time if running else elapsed_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        hundredths = int((elapsed_time * 100) % 100)
        elapsed_str = f"{minutes:02}:{seconds:02}.{hundredths:02}"
        
        x_offset = (width - 7 * len(elapsed_str)) // 2
        for i, char in enumerate(elapsed_str):
            draw_large_digit(stdscr, char, height // 2 - 2, x_offset + i * 7)

        # Display instructions at the bottom
        instructions = "Press SPACE to start/stop, 'c' to clear, 'q' to quit"
        stdscr.addstr(height - 1, (width - len(instructions)) // 2, instructions)

        # Refresh the screen
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        if key == ord(' '):  # Spacebar to start/stop
            if running:
                running = False
            else:
                running = True
                start_time = time.time() - elapsed_time
        elif key == ord('c'):  # 'c' to clear
            running = False
            elapsed_time = 0
        elif key == ord('q'):  # 'q' to quit
            break

if __name__ == "__main__":
    curses.wrapper(main)
