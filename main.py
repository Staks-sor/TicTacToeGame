
"""Второе задание от Y-lab созадние крестики-нолики 10х10 обратные"""
"""Перед началом установите pip install kivy"""

import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label
import random

"""Создание размера рабочей программы киви"""

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "500")
Config.set("graphics", "height", "500")

choice = ['X', 'X']

"""Создание основного класса киви"""
class GameApp(App):
    def __init__(self):
        super().__init__()
        self.switch = True

    def tic_tac(self, arg):

        arg.disabled = True
        arg.text = "X"
        #создание разметки игрового поля


        coordinate = []
        for i in range(0, 100, 10):
            coordinate.append([j for j in range(i, i + 10, 1)])


        for i in range(0, 10, 1):
            coordinate.append([j for j in range(i, i + 100, 10)])


        iter_D = [5, 4, 3, 2, 1, 0, 10, 20, 30, 40, 50]
        for i in iter_D:
            coordinate.append([i * 10 + j for j in range(0, 100, 11)])

        #пробегаемся по игровому полю с помощью цикла, изначально хотел сделать иначе vector = lambda item: [self.buttons[x].text for x in item], но столкнулся с проблемой
        vector = lambda item: [self.button[x].text for x in item]
        loose = False
        color_red = [1.0, 0.0, 0.0, 1.0]
        color_green = [1, 0, 0, 1]
        # Здесь так же пробигаемся циклом по списку кнопок с координатами.

        for item in coordinate:
            if vector(item).count('X') == 5:
                loose = True
                self.a.text = str(int(self.a.text) + 1)
                for i in item:
                    self.button[i].color = color_red
                break
            elif vector(item).count('O') == 5:
                loose = True
                self.b.text = str(int(self.b.text) + 1)
                for i in item:
                    self.button[i].color = color_green
                break
        # Рандомайзер который ставит 0 на игровом поле
        ran = random.randint(0, 100)
        self.button[ran].text = "O"
        self.button[ran].disabled = True

        if loose:
            for index in range(100):
                self.button[index].disabled = True
    # Продолжить соревнование с очком
    def restart(self, arg):

        self.switch = 0
        for index in range(100):
            self.button[index].color = [1, 1, 1, 1]
            self.button[index].text = ""
            self.button[index].disabled = False
    # Начать новую игру
    def new_game(self, arg):
        self.a.text = "0"
        self.b.text = "0"
        self.switch = 0
        for index in range(100):
            self.button[index].color = [1, 1, 1, 1]
            self.button[index].text = ""
            self.button[index].disabled = False

    def build(self):
        self.title = "X - O"

        root = BoxLayout(orientation='vertical', padding=5)
        grid = GridLayout(cols=10)
        self.button = [0 for _ in range(100)]
        for index in range(100):
            self.button[index] = Button(color=[0, 0, 0, 1], font_size=24, disabled=False, on_press=self.tic_tac)
            grid.add_widget(self.button[index])

        lbls = BoxLayout(orientation="horizontal", size_hint=(1, .11))
        self.a = Label(text="0", size_hint=(1, .2), font_size=27)
        self.b = Label(text="0", size_hint=(1, .2), font_size=27)
        lbls.add_widget(self.b)
        lbls.add_widget(self.a)

        root.add_widget(grid)
        root.add_widget(Button(text="Restart", size_hint=[1, .1], on_press=self.restart))
        root.add_widget(Button(text="New game", size_hint=[1, .1], on_press=self.new_game))
        root.add_widget(lbls)
        return root


if __name__ == "__main__":
    GameApp().run()