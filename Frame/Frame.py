import curses

class Frame():
    def __init__(self, width, height, caption):
        self._win = curses.newwin(height, width, 0, 0)
        self._caption = caption

    def paint(self):
        self._win.addstr(1, 1, f"win: {self._caption}")
        self._win.box()
#        self._win.refresh()

    def moveTo(self, x, y):
        self._win.mvwin(y, x)
        self.paint()

