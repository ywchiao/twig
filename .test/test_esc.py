
import curses
import os
import time

def get_delay(window, key):
    while True:
        start = time.time()
        ch = window.getch()
        end = time.time()
        if ch == key:
            return end-start

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)

    stdscr.addstr("Press ESC")
    esc_delay = get_delay(stdscr, 27)

    stdscr.addstr("\nPress SPACE")
    space_delay = get_delay(stdscr, ord(" "))

    return esc_delay, space_delay

if __name__ == "__main__":
    os.environ.setdefault("ESCDELAY", "25")
    esc_delay, space_delay = curses.wrapper(main)
    print(f"Escape delay: {esc_delay*1000} ms")
    print(f"Space delay: {space_delay*1000} ms")

# test_esc.py
