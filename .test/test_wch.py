
import curses

def main(stdscr):
    stdscr.nodelay(True)

    curses.mousemask(1)

    while True:
        try:
            e = stdscr.get_wch()
        except curses.error:
            e = -1
            continue
#        e = stdscr.getch()

        if e == "q":
            break
        elif e == curses.KEY_MOUSE:
            e = "got it"

        stdscr.addstr(e)

if __name__ == "__main__":
    curses.wrapper(main)
