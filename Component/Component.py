
import uuid

class Component:
    def __init__(self):
        self._id = uuid.uuid4().hex

        self._handlers = {}

    def handle(self, key):
        handled = False

        if self._handlers[key]:
            self._handlers[key]()

        return handled

    def addHandler(self, key, fun):
        self._handlers[key] = fun
