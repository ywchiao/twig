import curses

"""
   Frame: +--------+
          |Title   |
          +--------+
          |Content |
          +--------+
 """
class Frame():
    def __init__(self, width, height, caption):
        self._win = curses.newwin(height, width, 0, 0)
        self._titlebar = self._win.derwin(3, width, 0, 0)
        self._caption = caption
        self._handlers = {}

    def handle(self, key):
        handled = False

        if self._handlers[key]:
            self._handlers[key]()

        return handled

    def addHandler(self, key, fun):
        self._handlers[key] = fun

    def paint(self):
        self._win.addstr(1, 1, f"win: {self._caption}")
        self._win.box()
        self._titlebar.border(0, 0, 0, 0, 0, 0, curses.ACS_LTEE, curses.ACS_RTEE)
        self._win.refresh()

    def move(self, off_x, off_y):
        y, x = self._win.getbegyx()

        self._win.mvwin(y + off_y, x + off_x)

    def moveTo(self, x, y):
        self._win.mvwin(y, x)

