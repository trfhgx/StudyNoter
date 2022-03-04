import threading
import time
from threading import Timer,Thread,Event
from datetime import datetime
from playsound import  playsound
import art
import sys
import addtionlfuctions


app_version = "1.1.0 Alpha"
schooldays = [0, 1, 2, 3, 6]
weekends = [4, 5]
standard_session_time = 5
standard_break_time = 10
bonus = {'v':1.75, 'n':0.8 , 'y': 1.3}

class TimerClass(threading.Thread):
    def __init__(self, count, sessions):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.sessions = sessions
        self.sessions2 = sessions
        self.sessions_done = 0
        self.break_count = 0
        self.count = count

    def run(self):
        print(f'Session {self.sessions_done + 1}/{self.sessions2}')
        art.tprint(f'Session {str(self.sessions_done + 1)} ')
        addtionlfuctions.start()
        while self.count > 0 and not self.event.is_set():
            self.timer(self.count)
            self.count -= 1
            self.event.wait(1)

        print(f'Great job you finished ! enjoy your break!')
        self.sessions -= 1
        self.break_count += 1
        self.sessions_done += 1
        addtionlfuctions.finish()
        if self.sessions > 0:
            self.break_time(self.break_count)
        else:
            self.stop()
            print('Great job!!!!!! you are done now go rest')


    def break_time(self, num):
        if num == 4:
            break_count = 90 * 60 * (self.sessions_done / 4)
        else:
            break_count = (standard_break_time + self.sessions_done * 5) * 60

        while break_count > 0 and not self.event.is_set():
            self.timer(break_count)
            break_count -= 1
            self.event.wait(1)
        print(f'Get ready for another session there is {self.sessions} sessions left')
        self.count = 60 * 50
        self.run()


    def timer(self, num):
        q, mod = divmod(num, 60)
        sys.stdout.write(f"\rTime left: {int(q)}:{mod} ")
        sys.stdout.flush()


    def stop(self):
        self.event.set()


def beforestart():
    print("Before we start tell us how you feel right now from a scale of 1 to 10 the higher the better")
    mood = float(input('1 - 10 :  '))
    e = (input('are your exams near to start? v=very close, n=not by a long shot, y=in the middle v/n/y: '))
    sessions(mood, e)


def sessions(mood, e):
    print((bonus[e]))
    now = datetime.now()
    sessions = standard_session_time
    parm = now.weekday()

    if parm in schooldays:
        sessions =( (sessions * 0.6) * (mood / 6) ) * (bonus[e])
    else:
        sessions = ((sessions * 1.35) * (mood / 7)) * (bonus[e])
    if sessions <= 0:
        print('You should take a break today and have fun!')
    else:
        t = TimerClass(60 * 50, round(sessions))
        input('Are you ready!? ')
        t.run()





beforestart()


