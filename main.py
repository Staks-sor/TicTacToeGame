from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class TicTacToeGame(GridLayout):

    def __init__(self, **kwargs):
        super(TicTacToeGame, self).__init__(**kwargs)
        self.cols = 10
        self.rows = 10
        self.spaces = [' '] * 100
        self.current_player = 'X'

        for i in range(100):
            button = Button(text=' ', font_size=30)
            button.bind(on_release=self.make_move)
            self.add_widget(button)

    def make_move(self, instance):
        button_index = self.children.index(instance)
        if self.spaces[button_index] == ' ':
            self.spaces[button_index] = self.current_player
            instance.text = self.current_player

            if self.check_winner(self.current_player):
                self.show_popup('Победа!', f'Игрок {self.current_player} победил!')
                self.reset_board()
            elif self.check_draw():
                self.show_popup('Ничья!', 'Ничья!')
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14],  # horizontal
            [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [25, 26, 27, 28, 29],  # horizontal
            [30, 31, 32, 33, 34], [35, 36, 37, 38, 39], [40, 41, 42, 43, 44],  # horizontal
            [45, 46, 47, 48, 49], [50, 51, 52, 53, 54], [55, 56, 57, 58, 59],  # horizontal
            [60, 61, 62, 63, 64], [65, 66, 67, 68, 69], [70, 71, 72, 73, 74],  # horizontal
            [75, 76, 77, 78, 79], [80, 81, 82, 83, 84], [85, 86, 87, 88, 89],  # horizontal
            [90, 91, 92, 93, 94], [95, 96, 97, 98, 99],  # horizontal

            [0, 10, 20, 30, 40], [1, 11, 21, 31, 41], [2, 12, 22, 32, 42],  # vertical
            [3, 13, 23, 33, 43], [4, 14, 24, 34, 44], [5, 15, 25, 35, 45],  # vertical
            [6, 16, 26, 36, 46], [7, 17, 27, 37, 47], [8, 18, 28, 38, 48],  # vertical
            [9, 19, 29, 39, 49], [50, 51, 52, 53, 54], [55, 56, 57, 58, 59],  # vertical
            [60, 61, 62, 63, 64], [65, 66, 67, 68, 69], [70, 71, 72, 73, 74],  # vertical
            [75, 76, 77, 78, 79], [80, 81, 82, 83, 84], [85, 86, 87, 88, 89],  # vertical
            [90, 91, 92, 93, 94], [95, 96, 97, 98, 99],  # vertical

            [0, 11, 22, 33, 44], [5, 16, 27, 38, 49], [10, 21, 32, 43, 54],  # diagonal
            [15, 26, 37, 48, 59], [20, 31, 42, 53, 64], [25, 36, 47, 58, 69],  # diagonal
            [30, 41, 52, 63, 74], [35, 46, 57, 68, 79], [40, 51, 62, 73, 84],  # diagonal
            [45, 56, 67, 78, 89], [50, 61, 72, 83, 94], [55, 66, 77, 88, 99],  # diagonal
            [9, 18, 27, 36, 45], [14, 23, 32, 41, 50], [19, 28, 37, 46, 55],  # diagonal
            [24, 33, 42, 51, 60], [29, 38, 47, 56, 65], [34, 43, 52, 61, 70],  # diagonal
            [39, 48, 57, 66, 75], [44, 53, 62, 71, 80], [49, 58, 67, 76, 85],  # diagonal
            [54, 63, 72, 81, 90], [59, 68, 77, 86, 95], [64, 73, 82, 91, 100]  # diagonal
        ]

        for condition in win_conditions:
            if all(self.spaces[i] == player for i in condition):
                return True
        return False

    def check_draw(self):
        return ' ' not in self.spaces

    def reset_board(self):
        self.spaces = [' '] * 100
        for child in self.children:
            child.text = ' '

    def show_popup(self, title, message):
        content = Label(text=message)
        popup = Popup(title=title, content=content, size_hint=(None, None), size=(200, 200))
        popup.open()


class TicTacToeApp(App):

    def build(self):
        return TicTacToeGame()


if __name__ == '__main__':
    TicTacToeApp().run()
