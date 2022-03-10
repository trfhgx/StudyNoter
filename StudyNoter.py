import bin.models as models
import bin.config as config

confi = config.load_config()
print(f'StudyNoter v{config.version}')
schooldays = [0, 1, 2, 3, 6]
weekends = [4, 5]
standard_session_time = 5
bonus = {'v':1.85, 'n':0.8 , 'y': 1.33}

class TimerClass(models.threading.Thread):
    def __init__(self, count, sessionst):
        models.threading.Thread.__init__(self)
        self.event = models.threading.Event()
        self.sessions = sessionst
        self.sessions2 = sessionst
        self.sessions_done = 0
        self.break_count = 0
        self.standard_break_time = float(confi.break_time)
        self.count = count

    def run(self):
        print(f'Session {self.sessions_done + 1}/{self.sessions2}')
        models.art.tprint(f'Session {str(self.sessions_done + 1)} ')
        models.addtionlfuctions.playsong('start.wav', __file__, self.sessions_done, confi.co_efficent)
        while self.count > 0 and not self.event.is_set():
            self.event.wait(1)
            self.count -= 1
            self.Timer_(self.count)



        print('\nGreat job you finished ! enjoy your break!')
        models.addtionlfuctions.playsong('finish1.wav', __file__, self.sessions_done, confi.co_efficent)
        self.sessions -= 1
        self.break_count += 1
        self.sessions_done += 1
        if self.sessions > 0:
            self.break_time(self.break_count)
        else:
            self.stop()
            print(f'\nAstonishing job! you did {self.sessions_done} session and that means you studied/worked for {self.sessions_done * confi.session_time} minutes! now go rest and enjoy your day')


    def break_time(self, num):
        if num == 4 * confi.co_efficent:
            self.break_count = 0
            break_count = confi.long_break * 60 * (self.sessions_done / (4 * confi.co_efficent))

        else:
            break_count = (self.standard_break_time + (self.sessions_done - 1) * confi.bonus_break) * 60

        while break_count > 0 and not self.event.is_set():
            self.event.wait(1)
            break_count -= 1
            self.Timer_(break_count)

        print(f'Get ready for another session there is {self.sessions} sessions left')
        self.count = 60 * confi.session_time
        self.run()

    @staticmethod
    def Timer_(num):
        if num < 0: num = 0
        num = int(num)
        q, mod = divmod(num, 60)
        t = '{:02d}:{:02d}'.format(q, mod)
        models.sys.stdout.write(f"\rTime left: {t}")
        models.sys.stdout.flush()


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
                print(f"{models.addtionlfuctions.bcolors.FAIL}Error VE2 ")
                print(f"{models.addtionlfuctions.bcolors.WARNING}There seems to be an error (VE2 = the number inputted is not in range of 0-10 ) with processing your input please recheck your input! {models.addtionlfuctions.bcolors.ENDC}")
        except (ValueError , KeyError):
            print(f"{models.addtionlfuctions.bcolors.FAIL}Error VE1 ")
            print(f"{models.addtionlfuctions.bcolors.WARNING}There seems to be an error (VE1) with processing your input please recheck your input{models.addtionlfuctions.bcolors.ENDC}")




def sessions(mood, e) :
    now = models.datetime.now()
    sessionss = standard_session_time
    parm = now.weekday()
    if parm in schooldays:
        sessionss =( (sessionss * 0.65) * (mood / 5.5) ) * (bonus[e])
    else:
        sessionss = ((sessionss * 1.35) * (mood / 7.5)) * (bonus[e])
    if sessionss < 1:
        print(f'You should take a break today {confi.name}!. Enjoy yourself!')
    else:
        input(f'Are you ready {confi.name}!? ')

        sessionss = sessionss * confi.co_efficent
        t = TimerClass(confi.session_time * 60, models.math.ceil(sessionss))
        t.run()

if __name__ == "__main__":
    before_start()


