import time
import threading

class IntervalReminder():
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 360

    def __init__(self, event_trigger, notifire):
        self.event_trigger = event_trigger
        self.notifire = notifire

    def start(self):
        print "Please, enter the desired interval (min), so I could remind you."
        self.user_interval = int(raw_input()) * IntervalReminder.SECONDS_IN_MINUTE
        
        notifire_thread = threading.Thread(target=self.interval_mode)
        notifire_thread.start()

    def interval_mode(self):
        while True:
            time.sleep(self.user_interval)
            self.notifire.start()