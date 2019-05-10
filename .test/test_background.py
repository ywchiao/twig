
import curses

def main(stdscr):
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
        curses.init_pair(i+1, 195, i)

    stdscr.addstr(f"number of color_pairs: {curses.COLOR_PAIRS}\n")
    stdscr.addstr(f"number of colors:      {curses.COLORS}\n")

    try:
        for i in range(0, curses.COLORS):
            stdscr.addstr(f"cr:{i} ", curses.color_pair(i))
    except curses.error:
        pass

    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)

# test_color.py
