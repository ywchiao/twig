
import curses

from color.color import Color

def main(stdscr):
    color = Color()

    stdscr.addstr(f"number of color_pairs: {curses.COLOR_PAIRS}\n")
    stdscr.addstr(f"number of colors:      {curses.COLORS}\n")
    try:
        for i in range(0, curses.COLORS):
            stdscr.addstr(f"cr:{i} ", color.pair(i))
#            stdscr.addstr(f"cr:{i} ", color.reversed(i))
    except curses.error:
        pass

    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)

# test_color.py
