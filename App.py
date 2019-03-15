
import curses

from Frame.Frame import Frame

class App():
    def __init__(self):
        self._frames = []

        curses.wrapper(self._start)

    def _start(self, stdscr):
        curses.mousemask(1)
        stdscr.nodelay(True)

        self._window = stdscr
        self._frames.append(Frame(10, 10, "test"))

        self._paint(0, 0)

        while True:
            e = self._window.getch()

            if e == ord("q"):
                break

            if e == curses.KEY_MOUSE:
                _, x, y, _, _ = curses.getmouse()

                self._paint(x, y)

    def _paint(self, x, y):
        self._window.clear()
        self._window.border()
        self._window.addstr(2, 2, f"mouse clicked: x: {x:02}, y: {y:02}")

        for frame in self._frames:
            frame.paint()

        self._window.refresh()
#        self._frames[0].moveTo(x, y)

if __name__ == "__main__":
    app = App()
