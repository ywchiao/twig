
from __future__ import annotations

import selectors
import socket

from event.event import Event
from guest.guest import Guest
from handler.handler import Handler
from message.message import Message

class Muted(Handler):
    def __init__(self):
        self._guests = []
        self._multiplexer = selectors.DefaultSelector()
        self._handlers = {
            Message.CHAT: self._on_msg_chat,
            Message.SIGN_IN: self._on_sign_in
        }

    def on_socket(self, server_socket, mask):
        connection, address = server_socket.accept()  # Should be ready to read
        print(f"Connected by: {address}")

        connection.setblocking(False)

        mask = selectors.EVENT_READ | selectors.EVENT_WRITE

        guest = Guest()

        self._multiplexer.register(connection, mask, guest)

        self._guests.append(guest)

        guest.send_msg(Message(
            Message.WELCOME,
            who="MUTE",
            text=f"歡迎來到 MUTE: Multi-User Texting Environment"
        ))

        guest.send_msg(
            Message(Message.SIGN_IN)
        )

    def start(self, HOST, PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
            serverSocket.bind((HOST, PORT))
            serverSocket.setblocking(False)
            serverSocket.listen()

            self._multiplexer.register(
                serverSocket, selectors.EVENT_READ, self
            )

            print(f"MUTE server start listening at {HOST}:{PORT}")

            while True:
                events = self._multiplexer.select(timeout=None)

                for io, mask in events:
                    io.data.on_socket(io.fileobj, mask)

                for guest in self._guests:
                    for msg in guest.msg_in:
                        print(f"{guest.user}: {msg}")

                        if msg.type in self._handlers:
                            self._handlers[msg.type](guest, **msg.kwargs)

                    guest.msg_in = []

    def _on_msg_chat(self, from_who, who, text):
        for guest in self._guests:
            guest.send_msg(
                Message(
                    Message.CHAT,
                    who=who,
                    text=text
                )
            )

    def _on_sign_in(self, guest, **kwargs):
        print(f"id: {kwargs['user_id']} passwd {kwargs['passwd']}")
        guest.set_user(kwargs["user_id"])

        guest.send_msg(
            Message(
                Message.SYSTEM,
                who="MUTE",
                text="welcome"
            )
        )

if __name__ == "__main__":
    muted = Muted()

    muted.start("127.0.0.1", 4004)

# muted.py
