
import curses

from app.app import App
from window.window import Window

def main(stdscr):
    app = App(stdscr)

    app.add_window(Window(30, 10, "Window one").move_to(3, 1))
    app.add_window(Window(30, 10, "Window two").move_to(10, 7))
    app.add_window(Window(30, 10, "Window three").move_to(17, 13))

    app.start()

if __name__ == "__main__":
    curses.wrapper(main)

# test_win.py
