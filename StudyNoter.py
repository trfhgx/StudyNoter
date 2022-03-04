import threading
import time
from threading import Thread,Event
from datetime import datetime
import subprocess
import sys
try:
    import art
except Exception:
        print('there seems to be an error! no worries Ill fix it for you right away')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                               'art'])
        import art

import addtionlfuctions


# implement pip as a subprocess:


app_version = "3.0.0 Alpha"
schooldays = [0, 1, 2, 3, 6]
weekends = [4, 5]
standard_session_time = 5
bonus = {'v':1.85, 'n':0.8 , 'y': 1.33}

class TimerClass(threading.Thread):
    def __init__(self, count, sessions):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.sessions = sessions
        self.sessions2 = sessions
        self.sessions_done = 0
        self.break_count = 0
        self.standard_break_time = 10
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
            self.break_count = 0
            break_count = 65 * 60 * (self.sessions_done / 4)

        else:
            break_count = (self.standard_break_time + self.sessions_done * 3) * 60

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


def before_start():
    print("Before we start tell us how you feel right now from a scale of 1 to 10 the higher the better")
    ok = True
    while ok:
        try:
            mood = float(input('1 - 10 :  '))
            if mood <= 10 and mood >= 0:
                e = (input('are your exams near to start? v=very close, n=not by a long shot, y=in the middle v/n/y: '))
                sessions(mood, e)
                ok = False
            else:
                print(f"{addtionlfuctions.bcolors.FAIL}Error VE2 ")
                print(f"{addtionlfuctions.bcolors.WARNING}There seems to be an error (VE2 = the number inputted is not in range of 0-10 ) with processing your input please recheck your input! {addtionlfuctions.bcolors.ENDC}")
        except (ValueError , KeyError):
            print(f"{addtionlfuctions.bcolors.FAIL}Error VE1 ")
            print(f"{addtionlfuctions.bcolors.WARNING}There seems to be an error (VE1) with processing your input please recheck your input{addtionlfuctions.bcolors.ENDC}")




def sessions(mood, e):
    now = datetime.now()
    sessionss = standard_session_time
    parm = now.weekday()
    if parm in schooldays:
        sessionss =( (sessionss * 0.7) * (mood / 5.5) ) * (bonus[e])
    else:
        sessionss = ((sessionss * 1.35) * (mood / 7.5)) * (bonus[e])
    if sessionss <= 0:
        print('You should take a break today and enjoy yourself!')
    else:
        s = input('Are you ready!? ')

        t = TimerClass(60 * 50, round(sessionss))
        t.run()



before_start()


