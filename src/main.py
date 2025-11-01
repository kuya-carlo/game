"""
Devil Spawn

A 2D RPG game.
"""

import pathlib

import arcade
from typing import override

ASSETS_PATH = pathlib.Path(__file__).resolve().parent / "assets"


class Main(arcade.Window):
    def __init__(self) -> None:
        pass

    def setup(self):
        pass

    @override
    def on_key_press(self, key: int, modifiers: int):  # type: ignore
        """Processes key Processes

        Arguments:
            key (int): Which key has been pressed
            modifiers (int): Which key has been pressed alongside key
        """

    @override
    def on_key_release(self, symbol: int, modifiers: int):
        """Processes key release

        Arguments:
            key (int): Which key has been pressed
            modifiers (int): Which key has been pressed alongside key
        """

    @override
    def on_update(self, delta_time: float) -> bool | None:
        """Updates position of game objects

        Arguments:
            delta_time (float): How much time since last call
        """
        pass

    @override
    def on_draw(self):
        pass
