"""Второе домашнее задание от Y-Lab, деламем крестики нолики против пк с игровым полем 10х10"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "600")
Config.set("graphics", "height", "700")


class MainApp(App):
    def __init__(self):
        super().__init__()
        self.switch = True

    def tic_tac(self, arg):
        arg.disabled = True
        arg.text = "X"

        coordinate = (

            range(0, 10),
            range(10, 20),
            range(20, 30),
            range(30, 40),
            range(40, 50),
            range(50, 60),
            range(60, 70),
            range(70, 80),
            range(80, 90),
            range(90, 100),  # X
            range(0, 100, 10),
            range(1, 101, 10),
            range(2, 102, 10),
            range(3, 103, 10),
            range(4, 104, 10),
            range(5, 105, 10),
            range(6, 106, 10),
            range(7, 107, 10),
            range(8, 108, 10),
            range(9, 109, 10),  # Y
            range(5, 50, 11),
            range(4, 60, 11),
            range(3, 70, 11),
            range(2, 80, 11),
            range(1, 90, 11),
            range(0, 100, 11),  # D
            range(10, 99, 11),
            range(20, 98, 11),
            range(30, 97, 11),
            range(40, 96, 11),
            range(50, 95, 11),
            reversed(range(6, 61, 9)),
            reversed(range(7, 71, 9)),
            reversed(range(8, 81, 9)),
            reversed(range(9, 91, 9)),
            reversed(range(19, 92, 9)),
            reversed(range(29, 93, 9)),
            reversed(range(39, 94, 9))
        )
