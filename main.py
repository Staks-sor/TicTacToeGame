"""Второе задание от Y-lab созадние крестики-нолики 10х10 обратные"""
"""Перед началом установите pip install kivy"""


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
            reversed(range(4, 41, 9)),
            reversed(range(5, 51, 9)),
            reversed(range(6, 61, 9)),
            reversed(range(7, 71, 9)),
            reversed(range(8, 81, 9)),
            reversed(range(9, 91, 9)),
            reversed(range(19, 92, 9)),
            reversed(range(29, 93, 9)),
            reversed(range(39, 94, 9)),
            reversed(range(49, 95, 9)),
            reversed(range(59, 96, 9)),
        )
        #пробегаемся по игровому полю с помощью цикла, изначально хотел сделать иначе vector = lambda item: [self.buttons[x].text for x in item], но столкнулся с проблемой
        vector = (
            [self.button[x].text for x in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)],
            [self.button[x].text for x in (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)],
            [self.button[x].text for x in (20, 21, 22, 23, 24, 25, 26, 27, 28, 29)],
            [self.button[x].text for x in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39)],
            [self.button[x].text for x in (40, 41, 42, 43, 44, 45, 46, 47, 48, 49)], # Координат X
            [self.button[x].text for x in (50, 51, 52, 53, 54, 55, 56, 57, 58, 59)],
            [self.button[x].text for x in (60, 61, 62, 63, 64, 65, 66, 67, 68, 69)],
            [self.button[x].text for x in (70, 71, 72, 73, 74, 75, 76, 77, 78, 79)],
            [self.button[x].text for x in (80, 81, 82, 83, 84, 85, 86, 87, 88, 89)],
            [self.button[x].text for x in (90, 91, 92, 93, 94, 95, 96, 97, 98, 99)],

            [self.button[y].text for y in (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)],
            [self.button[y].text for y in (1, 11, 21, 31, 41, 51, 61, 71, 81, 91)],
            [self.button[y].text for y in (2, 12, 22, 32, 42, 52, 62, 72, 82, 92)],
            [self.button[y].text for y in (3, 13, 23, 33, 43, 53, 63, 73, 83, 93)],
            [self.button[y].text for y in (4, 14, 24, 34, 44, 54, 64, 74, 84, 94)], # Координат Y
            [self.button[y].text for y in (5, 15, 25, 35, 45, 55, 65, 75, 85, 95)],
            [self.button[y].text for y in (6, 16, 26, 36, 46, 56, 66, 76, 86, 96)],
            [self.button[y].text for y in (7, 17, 27, 37, 47, 57, 67, 77, 87, 97)],
            [self.button[y].text for y in (8, 18, 28, 38, 48, 58, 68, 78, 88, 98)],
            [self.button[y].text for y in (9, 19, 29, 39, 49, 59, 69, 79, 89, 99)],

            [self.button[d].text for d in (5, 16, 27, 38, 49)],
            [self.button[d].text for d in (4, 15, 26, 37, 48, 59)],
            [self.button[d].text for d in (3, 14, 25, 36, 47, 58, 69)],
            [self.button[d].text for d in (2, 13, 24, 35, 46, 57, 68, 79)],
            [self.button[d].text for d in (1, 12, 23, 34, 45, 56, 67, 78, 89)],
            [self.button[d].text for d in (0, 11, 22, 33, 44, 55, 66, 77, 88, 99)], # Диагональ слева на право
            [self.button[d].text for d in (10, 21, 32, 43, 54, 65, 76, 87, 98)],
            [self.button[d].text for d in (20, 31, 42, 53, 64, 75, 86, 97)],
            [self.button[d].text for d in (30, 41, 52, 63, 74, 85, 96)],
            [self.button[d].text for d in (40, 51, 62, 73, 84, 95)],
            [self.button[d].text for d in (50, 61, 72, 83, 94)],

            [self.button[d].text for d in (40, 31, 22, 13, 4)],
            [self.button[d].text for d in (50, 41, 32, 23, 14, 5)],
            [self.button[d].text for d in (60, 51, 42, 33, 24, 15, 6)],
            [self.button[d].text for d in (70, 61, 52, 43, 34, 25, 16, 7)],
            [self.button[d].text for d in (80, 71, 62, 53, 44, 35, 26, 17, 8)],
            [self.button[d].text for d in (90, 81, 72, 63, 54, 45, 36, 27, 18, 9)],  # Диагональ справа на лево
            [self.button[d].text for d in (91, 82, 73, 64, 55, 46, 37, 28, 19)],
            [self.button[d].text for d in (92, 83, 74, 65, 56, 47, 38, 29)],
            [self.button[d].text for d in (93, 84, 75, 66, 57, 48, 39)],
            [self.button[d].text for d in (94, 85, 76, 67, 58, 49)],
            [self.button[d].text for d in (95, 86, 77, 68, 59)],
        )

        loose = False
        color = [1.0, 0.0, 0.0, 1.0]
        # Здесь так же пробигаемся циклом по списку кнопок с координатами.
        for index in range(42):
            if vector[index].count('X') == 5:
                loose = True
                self.a.text = str(int(self.a.text) + 1)
                for i in coordinate[index]:
                    self.button[i].color = color
                break
            elif vector[index].count('O') == 5:
                loose = True
                self.b.text = str(int(self.b.text) + 1)
                for i in coordinate[index]:
                    self.button[i].color = color
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
