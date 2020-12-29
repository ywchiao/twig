
from __future__ import annotations

import curses
import json

from logcat.logcat import LogCat

class Event:
    CLICK = 'click'
    CURSOR_ON = 'cursor_on'
    CURSOR_OFF = 'cursor_off'
    EXIT = 'exit'
    DIALOG_OK = 'dlg_ok'
    DIALOG_CANCEL = 'dlg_cancel'
    FOCUS_IN = 'focus_in'
    FOCUS_OUT = 'focus_out'
    KEY_PRESSED = 'key_pressed'
    LINEFEED = '\n'
    MSG_SEND = 'msg_send'
    NET = 'net'
    PAINT = 'paint'
    SCROLL_DOWN = 'scroll_down'
    SCROLL_H = 'scroll_h'
    SCROLL_LEFT = 'scroll_left'
    SCROLL_RIGHT = 'scroll_right'
    SCROLL_UP = 'scroll_up'
    SCROLL_V = 'scroll_v'
    SIGN_IN = 'sign_in'
    WELCOME = 'welcome'
    WIN_DISPLAY = 'win_display'
    KEY_BACKSPACE = curses.KEY_BACKSPACE
    KEY_DOWN = curses.KEY_DOWN
    KEY_ENTER = curses.KEY_ENTER
    KEY_LEFT = curses.KEY_LEFT
    KEY_RIGHT = curses.KEY_RIGHT
    KEY_UP = curses.KEY_UP
    NET_READ = 'net_read'
    NET_WRITE = 'net_write'

    _queue = []

    def __init__(self, type_: str, target=None, **kwargs):
        self._type = type_
        self._target = target
        self._kwargs = kwargs

    @classmethod
    def empty(cls) -> None:
        cls._queue = []

    @classmethod
    def events(cls) -> list:
        return cls._queue

    @classmethod
    def trigger(cls, e: Event) -> None:
        cls._queue.append(e)

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def target(self):
        return self._target

    @property
    def type(self):
        return self._type

    def __repr__(self):
        return json.dumps({
            'type': self._type,
            'kwargs': self._kwargs
        })

# event.py
