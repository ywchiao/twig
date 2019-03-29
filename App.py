#!/usr/bin/python3

import curses
import types

from Frame.Frame import Frame
from WindowManager.Manager import WindowManager

class App():
    def __init__(self, stdscr):
        self._queue = []
        self._frames = []

        self._focused = None

        self.MOUSE_CLICK = 0
        self.KEY_PRESSED = 1
        self.CMD_EXIT = 2

        self._window = stdscr
        WindowManager.register(stdscr)

    def paint(self):
        self._window.border()
        self._window.refresh()

        for k, frame in WindowManager.getFrames():
            frame.paint()

    def start(self):
        frames = WindowManager.getFrames()
        self._focused = frames[len(frames) - 1][1]

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
                    type=self.MOUSE_CLICK, x=x, y=y
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
                elif e.type == self.KEY_PRESSED:
                    self._focused.handle(e.key)
                    self.paint()
                else:
                    self._clicked(e)
                    self.paint()

            self._queue = []

    def _clicked(self, e):
        k, self._focused = WindowManager.checkClicked(e.x, e.y)

def main(stdscr):
    app = App(stdscr)

    frameOne = Frame(30, 10, "window one")
    frameOne.addHandler(ord("w"), lambda : frameOne.move(0, -1))
    frameOne.addHandler(ord("a"), lambda : frameOne.move(-1, 0))
    frameOne.addHandler(ord("s"), lambda : frameOne.move(0, 1))
    frameOne.addHandler(ord("d"), lambda : frameOne.move(1, 0))

    frameTwo = Frame(30, 10, "window two")
    frameTwo.addHandler(ord("w"), lambda : frameTwo.move(0, -1))
    frameTwo.addHandler(ord("a"), lambda : frameTwo.move(-1, 0))
    frameTwo.addHandler(ord("s"), lambda : frameTwo.move(0, 1))
    frameTwo.addHandler(ord("d"), lambda : frameTwo.move(1, 0))
    frameTwo.moveTo(10, 7)

    frameThree = Frame(30, 10, "window three")
    frameThree.addHandler(ord("w"), lambda : frameThree.move(0, -1))
    frameThree.addHandler(ord("a"), lambda : frameThree.move(-1, 0))
    frameThree.addHandler(ord("s"), lambda : frameThree.move(0, 1))
    frameThree.addHandler(ord("d"), lambda : frameThree.move(1, 0))
    frameThree.moveTo(17, 13)

    app.start()

if __name__ == "__main__":
    curses.wrapper(main)
