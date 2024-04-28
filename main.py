from game import Game
from player import Player
from game_window import Ui_Form
from main_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    game = Game(window=window)
    game.start_game()
    window.show()
    app.exec()
