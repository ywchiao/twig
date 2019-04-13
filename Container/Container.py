
from Component.Component import Component

class Container(Component):
    def __init__(self):
        super().__init__()

        self._components = []
#        self._layout_manager = layout_manager

    def addComponent(self, component):
        self._components.append(component)

    def layout(self):
        self._layout_manager.layout(self._components)
