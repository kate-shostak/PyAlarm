import os
import threading
import notifire
import intervalmode
import alarmmode
#replace os module with subprocess
#Features:  Ring every n minutes
#           Usual alarm feature
#           Autostart on system start
#           User notifications
#           Notification window

class MainAlarm():

    def __init__(self):
        self.event_trigger = threading.Event()
        self.notifire_handler = notifire.Notifier(self.event_trigger)
        self.alarm = alarmmode.Alarm(self.event_trigger, self.notifire_handler)
        self.interval = intervalmode.IntervalReminder(self.event_trigger, self.notifire_handler)

        self.alarm_fetures = {'i': self.interval.start,
                              'a': self.alarm.start }

    def greetings(self):
        print "Hi, I'm your Alarm. Tell me what to do:\na - usual alarm function\n",
        print "i - interval mode, in which your alarm will notificate you every 0....n minutes."
        while True:
            print "Eneter the key"
            selected_mode = str(raw_input())
            self.alarm_fetures[selected_mode]()

my_alarm = MainAlarm()
my_alarm.greetings()