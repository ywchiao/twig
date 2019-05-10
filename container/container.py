
from __future__ import annotations

from component.component import Component
from logcat.logcat import LogCat

class Container(Component):
    def __init__(self, x=0, y=0, width=1, height=1):
        super().__init__(x, y, width, height)

        self._components = []

    @LogCat.log_func
    def add(self, component) -> Container:
        self._components.append(component)

        return self

    @property
    def components(self):
        return self._components

# container.py
