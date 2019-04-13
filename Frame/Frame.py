import curses

from Container.Container import Container
from LayoutManager import BorderLayout
from WindowManager.Manager import WindowManager

"""
   Frame: +--------+
          |Title   |
          +--------+
          |Content |
          |status  |
          +--------+
 """
class Frame(Container):
    def __init__(self, width, height, caption):
#        super(BorderLayout)
        super().__init__()

        self._win = curses.newwin(height, width, 0, 0)
        self._titlebar = self._win.derwin(3, width, 0, 0)
        self._status = self._win.derwin(1, width, height - 1, 0)
        self._caption = caption

        WindowManager.register(self)

    def dimension(self):
        up, left = self._win.getbegyx()
        height, width = self._win.getmaxyx()

        return (left, up, width, height)

    def paint(self):
        self._win.addstr(1, 1, f"win: {self._caption}")
        self._win.box()
        self._titlebar.border(0, 0, 0, 0, 0, 0, curses.ACS_LTEE, curses.ACS_RTEE)
        self._win.refresh()

        for component in self._components:
            component.paint()

    def move(self, off_x, off_y):
        y, x = self._win.getbegyx()

        self._win.mvwin(y + off_y, x + off_x)

        for component in self._components:
            component.move(off_x, off_y)

    def moveTo(self, x, y):
        self._win.mvwin(y, x)

