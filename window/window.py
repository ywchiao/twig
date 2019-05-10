
from __future__ import annotations

from const.color import Color
from container.container import Container
from event.event import Event
from logcat.logcat import LogCat
from viewport.viewport import Viewport

class Window(Container):
    @LogCat.log_func
    def __init__(
        self, x: int, y:int, width: int, height: int, caption: str = None
    ):
        super().__init__(x, y, width, height)

        self._caption = caption
        self._focus = None

        self._win = Viewport(width, height)
        self._win.move_to(x, y)

        self._modal = False

        self.set_background(Color.TEXT)

        self._handlers = {
            Event.CLICK: self._on_click,
            Event.KEY_PRESSED: self._on_key_pressed,
            Event.PAINT: self._on_paint,
        }

    @LogCat.log_func
    def move(self, off_x: int, off_y: int) -> Window:
        self._win.move(off_x, off_y)

    @LogCat.log_func
    def set_background(self, color) -> Window:
        self._win.set_background(color)

        return self

    @LogCat.log_func
    def set_content(self, content) -> Window:
        self._content = content

        return self

    @LogCat.log_func
    def set_caption(self, caption: str) -> Window:
        self._caption = caption

        return self
    @LogCat.log_func
    def _on_any(self, e: Event) -> None:
        if self._focus:
            self._focus.on_event(e)

    @LogCat.log_func
    def _on_click(self, e: Event, x: int, y: int) -> bool:
        for component in self.components:
            if component.contains(x - self.x, y - self.y):
                Event.trigger(
                    Event(Event.CLICK, component, x=x, y=y)
                )

                if component.focusable:
                    self._focus = component

                break

        return False

    @LogCat.log_func
    def _on_key_pressed(self, e: Event, key: str) -> None:
        if self._focus:
            self._focus.on_event(e)

    @LogCat.log_func
    def _on_paint(self, e: Event) -> None:
        (
            self._win
                .border()
                .print_text(1, 0, f"┨ {self._caption} ┠")
                .refresh()
        )

        for component in self.components:
            component.paint(self._win)

        if self._focus:
            self._focus.paint(self._win)

    @property
    def focused(self) -> bool:
        return self._focused

    @property
    def modal(self) -> bool:
        return self._modal

    @property
    def win(self) -> Viewport:
        return self._win

# window.py
