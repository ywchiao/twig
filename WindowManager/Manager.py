
class WindowManager():
    _windows = []
    _counts = 0

    def __init__(self):
        pass

    @classmethod
    def checkClicked(cls, x, y):
        for idx, win in reversed(list(enumerate(cls._windows))):
            if idx == 0:
                break

            left, up, width, height = win[1].dimension()

            if left <= x <= (left + width - 1) and up <= y <= (up + height - 1):
                break

        if idx > 0:
            cls._windows.append(cls._windows.pop(idx))

        return win

    @classmethod
    def getFrames(cls):
        return cls._windows[1::]

    @classmethod
    def register(cls, window):
        cls._windows.append((cls._counts, window))
        cls._counts += 1
