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

    def tic_tac_toe(self, arg):
        arg.disabled = True
        arg.text = 'X' if self.switch else 'O'
        self.switch = not self.switch