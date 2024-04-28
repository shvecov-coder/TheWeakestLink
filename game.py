import time
import threading
from PySide6.QtWidgets import QLabel, QTimeEdit

class Game:

    window = None
    curr_bank = 0
    summ_array = [5, 10, 15, 20 ,30, 45, 65, 100]
    bank_round = 0
    bank_game = 0
    players = []
    thread_timer = None
    thread_exit_flag = False


    def __init__(self, window):
        self.window = window
        self.window.ui.no.released.connect(self.push_no)
        self.window.ui.yes.released.connect(self.push_yes)
        self.window.ui.bank.released.connect(self.push_bank)
        self.window.ui.timerStart_90.released.connect(self.push_90)

    def get_curr_value_bank(self):
        return self.summ_array[self.curr_bank]

    def get_curr_idx_bank(self):
        return self.curr_bank

    def push_yes(self):
        len_bank = self.get_len_bank()

        if self.curr_bank == len_bank - 1:
            return
        
        self.curr_bank += 1
        print(self.get_curr_idx_bank())
        self.set_active_bank(self.curr_bank + 1)

    def set_active_bank(self, idx):

        for i in range(1, self.get_len_bank() + 1):

            if i == idx:
                color = '#A3375E'
            else:
                color = '#2c5cd8'

            name_object = 'sum_' + str(i)
            temp_label = self.window.findChild(QLabel, name_object)
            temp_label.setStyleSheet(f"background: {color};\n"
                                    "border-radius: 5px;\n"
                                    "font-size: 15px;")

    def start_game(self):
        self.set_active_bank(1)

    def get_len_bank(self):
        return len(self.summ_array)
    
    def plus_bank(self, value):
        self.bank_round += value
        if self.bank_round > 100:
            self.bank_round = 100

    def push_bank(self):
        self.plus_bank(self.get_curr_value_bank())
        self.set_active_bank(1)
        self.curr_bank = 0
        self.window.ui.resultRound.setText(f'{self.bank_round}')
        # сбросить таймер если банк раунда 100 или больше

    def push_no(self):
        self.set_active_bank(1)
        self.curr_bank = 0
    
    def start_timer(self, value):
        temp_label = self.window.findChild(QTimeEdit, 'timer')
        while value:
            temp_label.setSpecialValueText(f'{value}')
            time.sleep(1)
            value -= 1
            print('sec')

    def push_90(self):
        self.thread_timer = threading.Thread(target=self.start_timer, args=[90])
        self.thread_timer.start()
