class Player:

    def __init__(self):
        self.name = ""
        self.point = 0
        self.correctly_answer = 0
        self.error_answer = 0

    def set_succes_answer(self):
        self.correctly_answer += 1
    
    def set_error_answer(self):
        self.error_answer += 1
