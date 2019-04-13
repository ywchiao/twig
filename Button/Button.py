import curses

from Component.Component import Component

class Button(Component):
    def __init__(self, caption):
        super().__init__()

        self._caption = caption
        self._win = curses.newwin(2, len(caption) + 2, 0, 0)
        self._handlers = {
            "click": self._click
        }

    def dimension(self):
        up, left = self._win.getbegyx()
        height, width = self._win.getmaxyx()

        return (left, up, width, height)

    def move(self, off_x, off_y):
        y, x = self._win.getbegyx()

        self.moveTo(x + off_x, y + off_y)

    def moveTo(self, x, y):
        self._win.mvwin(y, x)

    def paint(self):
        self._win.addstr(0, 1, f"{self._caption}", curses.color_pair(1))
        self._win.refresh()

    def _click(self):
        pass
