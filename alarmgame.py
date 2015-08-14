import threading

class AlarmGame():
    def __init__(self, event):
      self.event = event

    def start_game(self):
        user_answer = int(raw_input("How much is 3 + 5 ?: "))
        if user_answer == 8:
            self.event.set()
        else:
            self.start_game()

    '''There should be separate game logic: 
    creation of Enemy and Player classes and so on'''