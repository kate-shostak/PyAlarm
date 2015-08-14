import time
import threading

class Alarm():
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 360

    def __init__(self, event_trigger, notifire):
        self.event_trigger = event_trigger
        self.notifire = notifire

    def start(self):
        print "Eneter the time to notificate you in followin format: hh:mm"
        self.alarm_time = raw_input().split(":")
        self.alarm_mode_loop()

    def alarm_mode_loop(self):
        print "Sleep"
        notifire_thread = threading.Timer(self.time_difference_counter(),self.notifire.start)
        notifire_thread.start()

    def time_difference_counter(self):
        hours_until_beep = abs( int(time.strftime("%H", time.localtime())) - int(self.alarm_time[0]))
        minutes_until_beep = abs( int(time.strftime("%M", time.localtime())) - int(self.alarm_time[1]))
        seconds_until_beep = Alarm.SECONDS_IN_MINUTE - int(time.strftime("%S", time.localtime()))
        time_left_until_alarm_beeps = hours_until_beep*Alarm.SECONDS_IN_HOUR + minutes_until_beep*Alarm.SECONDS_IN_MINUTE + seconds_until_beep
        return time_left_until_alarm_beeps
