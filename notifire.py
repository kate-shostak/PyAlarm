import os

class Notifier():
    def __init__(self, event_trigger):
        self.event_trigger = event_trigger

    def start(self):
        for i in xrange(5): 
            os.system('notify-send --urgency=low "Hi!"') 
            os.system('aplay -q beep.wav')
