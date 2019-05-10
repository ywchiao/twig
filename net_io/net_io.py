
from __future__ import annotations

import json
import socket
import struct

from event.event import Event
from handler.handler import Handler
from logcat.logcat import LogCat
from message.message import Message

class NetIO(Handler):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self._in_buffer = b""
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.on(Event.MSG_SEND, self._on_msg_send)
        self.on(Event.SIGN_IN, self._on_sign_in)

    @LogCat.log_func
    def connect(self, host: str, port: int) -> None:
        self._socket.connect((host, port))
        self._socket.setblocking(0)

    def recv(self):
        msg = []

        try:
            self._in_buffer += self._socket.recv(1024)
        except:
            pass

        while len(self._in_buffer) > 4:
            msg_len = struct.unpack(">I", self._in_buffer[:4])[0]

            if len(self._in_buffer) >= (msg_len + 4):
                msg_json = json.loads(
                    str(self._in_buffer[4:msg_len + 4].decode())
                )

                msg.append(
                    Message(msg_json["type"], **msg_json["kwargs"])
                )

                self._in_buffer = self._in_buffer[msg_len+4:]
            else:
                break

        return msg

    @LogCat.log_func
    def send(self, msg):
        msg_stream = repr(msg).encode()

        self._socket.sendall(
            struct.pack(">I", len(msg_stream)) + msg_stream
        )

    @LogCat.log_func
    def _on_msg_send(self, e: Event, type: str, who: str, text: str) -> None:
        self.send(
            Message(type, who=who, text=text)
        )

    @LogCat.log_func
    def _on_sign_in(self, e: Event, user_id: str, passwd: str) -> None:
        self.send(Message(
            e.type,
            user_id=user_id,
            passwd=passwd
        ))

# net_io.py
