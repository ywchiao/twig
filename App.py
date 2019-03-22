
import curses
import types

from Frame.Frame import Frame

class App():
    def __init__(self, stdscr):
        self._queue = []
        self._frames = []

        self._focused = None

        self.MOUSE_CLICK = 0
        self.KEY_PRESSED = 1
        self.CMD_EXIT = 2

        self._window = stdscr

    def addComponent(self, frame):
        self._frames.append(frame)

        if not self._focused:
            self._focused = frame

    def paint(self):
        self._window.border()
        self._window.refresh()

        for frame in self._frames:
            frame.paint()

    def start(self):
        self._loop()

    def _checkInput(self):
        e = self._window.getch()
        event = None

        if e == ord("q"):
            self._queue.append(
                types.SimpleNamespace(
                    type=self.CMD_EXIT
                )
            )
        elif e == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()

            self._queue.append(
                types.SimpleNamespace(
                    type=self.CLICK, x=x, y=y
                )
            )
        elif e > 0:
            self._queue.append(
                types.SimpleNamespace(
                    type=self.KEY_PRESSED, key=e
                )
            )

    def _loop(self):
        curses.mousemask(1)
        self._window.nodelay(True)

        self.paint()

        while True:
            self._checkInput()

            for e in self._queue:
                if e.type == self.CMD_EXIT:
                    exit()

                if e.type == self.KEY_PRESSED:
                    self._focused.handle(e.key)
                    self.paint()

            self._queue = []

def main(stdscr):
    app = App(stdscr)

    frame = Frame(30, 10, "this is a test")
    frame.addHandler(ord("w"), lambda : frame.move(0, -1))
    frame.addHandler(ord("a"), lambda : frame.move(-1, 0))
    frame.addHandler(ord("s"), lambda : frame.move(0, 1))
    frame.addHandler(ord("d"), lambda : frame.move(1, 0))

    app.addComponent(frame)

    app.start()

if __name__ == "__main__":
    curses.wrapper(main)
