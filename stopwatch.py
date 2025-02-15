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
          "      ",
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
    past_times = []
    show_past_times = False  # Start with past times hidden

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Display the current date in the upper left corner
        current_date_str = time.strftime('%A, %B %d, %Y')
        stdscr.addstr(0, 0, current_date_str)

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

        if show_past_times:
            # Calculate the position and size of the past times section
            header = "Past Times"
            section_width = max(len(max(past_times, key=len, default='')), len(header)) + 2
            section_x = (x_offset - section_width) // 2
            section_y = (height - 10) // 2

            # Draw the header above the past times section
            stdscr.addstr(section_y - 2, section_x + (section_width - len(header)) // 2, header, curses.color_pair(1))

            # Draw a horizontal line after the header
            stdscr.hline(section_y - 1, section_x, curses.ACS_HLINE, section_width)

            # Display past times below the line
            for i, past_time in enumerate(past_times[-10:]):
                stdscr.addstr(section_y + i, section_x + 1, past_time, curses.color_pair(1))

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
            past_times.append(elapsed_str)
            elapsed_time = 0
        elif key == ord('p'):  # 'p' to show/hide past times
            show_past_times = not show_past_times
        elif key == ord('q'):  # 'q' to quit
            if running:
                past_times.append(elapsed_str)  # Append the current elapsed time before quitting
            break

    # End curses window
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
