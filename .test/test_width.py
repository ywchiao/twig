import curses

def main(stdscr):
#    curses.start_color()
#    curses.use_default_colors()

    stdscr.box()
    stdscr.refresh()
    win = curses.newwin(20, 60, 0, 0)
    win.erase()
    win.box()
    win.addstr(2, 2, "test")

    for x in range(0, 60):
        if 0 == x%10:
            win.addstr(1, x, f"{x//10}")
        win.addstr(2, x, f"{x%10}")

    win.refresh()

    stdscr.getch()

curses.wrapper(main)
