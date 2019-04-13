
from BorderLayout import BorderLayout

class LayoutManager:
    _layouts = {}

    def __init__(self):
        pass

    @classmethod
    def BorderLayout(cls):
        if "_border_layout" not in cls._layouts:
            cls._layouts["_border_layout"] = BorderLayout()

        return cls._layouts["_border_layout"]
