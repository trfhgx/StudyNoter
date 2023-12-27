import math
import bin.ERRORS
import bin.models as models
import bin.config as config
import bin.constants as constants
from bin.Data import Data as data_class
import datetime
from pydub import AudioSegment
from pydub.playback import play

print(f"StudyNoter {constants.version}...")
confi = config.load_config()
data_class = data_class(confi['name'])
data = data_class.start_checks()
print(data)
start = datetime.datetime.now()
temp_data = data[confi['name']]['data']
year = start.strftime("%Y")
evil_bonus = 0
if str(datetime.date.today()) in temp_data[year]:
    cache = True
else:
    cache = False
cache = False

start = start.strftime("%H:%M")




class TimerClass(models.threading.Thread):
    def __init__(self, count, sessionst, special):
        self.special = special
        models.threading.Thread.__init__(self)
        self.event = models.threading.Event()
        self.sessions = sessionst
        self.sessions2 = sessionst
        self.sessions_done = 0
        self.done2 = 0
        self.break_count = 0
        self.standard_break_time = float(confi['break_time'])
        self.count = count
        self.cache = 0
        if cache and True :
            self.sessions_done = int(temp_data[year][str(datetime.date.today())] * (confi['co_efficent']))
            print(self.sessions_done)
            self.cache = self.sessions_done
            self.break_count = self.sessions_done % 4
        print('long break', self.break_count >= math.ceil(4 * confi['co_efficent']), self.break_count, math.ceil(4 * confi['co_efficent']))


        c = 1
        self.finish_time = sessionst * confi['session_time'] * 60 + sessionst
        while c < self.sessions:
            print(math.ceil(4 * confi['co_efficent']), c)
            if c % 4 == 0:
                self.break_count = 0
                if c == 4:
                    k  = 0
                else:
                    k = 1
                break_count = (
                        confi['long_break_time'] * 60
                        + confi['long_break_time'] * 60 * ((c * 0.2) / (8 * confi['co_efficent'])) * k
                )
                print('long break', c, break_count / 60, confi['long_break_time'] )


                # break_count = (
                #         confi['long_break_time'] * 60 * ((c * 0.7) / (4 * confi['co_efficent']))
                # )

            else:
                break_count = (
                                      self.standard_break_time + (c - 1) * confi['bonus_break_time']
                              ) * 60
            c += 1
            self.finish_time += break_count
            if special:
                self.finish_time += 60 * 40
        print(self.sessions)

        if self.sessions > 12:
            print(' hiel')
        s1 = datetime.datetime.now()
        self.finish_time = (s1 + datetime.timedelta(seconds=self.finish_time)).strftime("%Y/%m/%d  %H:%M")


    def run(self):
        now = datetime.datetime.now()
        now = now.strftime("%H:%M")
        print(f'started at {start} time now is {now} and the sessions will end in {self.finish_time}')
        bonus = 1

        if self.special:
            if self.done2 == 0:
                self.sessions_done -= 1
                bonus = 1.8
            elif self.sessions_done - 1 == self.sessions2 + self.cache:
                self.sessions_done = -2
                bonus = 0.3

        self.done2 += 1
        print(f"Session {int(self.sessions_done + 1)}/{int(self.sessions2 + self.cache)}")
        models.art.tprint(f"Session {int(self.sessions_done + 1)} ")
        models.addtionlfuctions.playsong(
            "start.wav", __file__, self.sessions_done, confi['co_efficent'],self.sessions, self.sessions2
        )
        self.count *= bonus
        while self.count > 0 and not self.event.is_set():
            self.event.wait(1 + evil_bonus)
            self.count -= 1
            self.timer_(self.count)

        print("\033[1m\nGreat job you finished ! enjoy your break!")
        data_class.check_year(data)
        data_class.set_data(data, str(datetime.date.today()), 1 / confi['co_efficent'])
        models.addtionlfuctions.playsong(
            "finish", __file__, self.sessions_done, confi['co_efficent'],self.sessions, self.sessions2
        )
        self.sessions -= 1
        self.break_count += 1
        self.sessions_done += 1
        print(self.break_count)
        if self.sessions > 0:
            self.break_time()
        else:
            self.stop()
            print(
            '\033[1m'+f"\nAstonishing job! you did {self.sessions_done} session and that means you studied/worked for {self.sessions_done * confi['session_time']} minutes! now go rest and enjoy your day"
            )

    def break_time(self) -> None:
        print('long break', self.break_count >= math.ceil(4 * confi['co_efficent']), self.break_count, math.ceil(4 * confi['co_efficent']))
        if self.break_count >= math.ceil(4 * confi['co_efficent']):
            print('Long break moment')
            self.break_count = 0
            if self.sessions_done == 4:
                k = 0
            else:
                k = 1
            break_count = (
                    confi['long_break_time'] * 60
                    + confi['long_break_time'] * 60 * ((self.sessions_done * 0.2) / (8 * confi['co_efficent'])) * k
            )

        else:
            break_count = (
                self.standard_break_time + (self.sessions_done - 1) * confi['bonus_break_time']
            ) * 60
        if self.break_count == 12:
            break_count = (
                    confi['long_break_time'] * 60 * ((self.sessions_done / (4 * confi['co_efficent'])) + 4)
            )

        while break_count > 0 and not self.event.is_set():
            self.event.wait(1 - evil_bonus)
            break_count -= 1
            self.timer_(break_count, True)

        print(f" Get ready for another session there is {self.sessions} sessions left")
        self.count = 60 * confi['session_time']
        self.run()

    @staticmethod
    def timer_(num: int, breaki=False) -> None:
        if num < 0:
            num = 0
        num = int(num)
        q, mod = divmod(num, 60)

        if q < 10:
            t = "\033[1m\033[91m\033[4m{:02d}:{:02d}\033[0m".format(q, mod)
        elif q < 20:
            t = "\033[1m\033[93m{:02d}:{:02d}\033[0m".format(q, mod)

        else:
            t = "\033[1m\033[96m{:02d}:{:02d}\033[0m".format(q, mod)
        if breaki:
            t = "\033[1m\033[92m\033[4m{:02d}:{:02d}\033[0m".format(q, mod)

        models.sys.stdout.write(f"\rTime left: {t}\033[0m")
        models.sys.stdout.flush()

    def stop(self):
        self.event.set()




def before_start():

    while True:
        try:
            choice = int(input('Type\n1/ if you would like the program to calculate'
                               ' the amount of sessions for you HIGHLY RECOMMENDED!'
                               '\n2/ if you would like to set a custom number of sessions\n'))
            if choice == 1:
                print(
                    "Before we 1start tell us how you feel right now from a scale of 1 to 10 the higher the better"
                )
                while True:
                    mood = bin.ERRORS.error_checker(int, ind=(input("1 - 10 :  ")), type_var=float,
                                                   forbidden=str)
                    print(mood)
                    if not mood:
                        print('The value you entered cant be read by the app!')
                        continue

                    if mood <= 10 and mood >= 0:
                        e = input(
                            "are your exams near to start? v=very close, y=in the middle, n=not by a long shot  v/y/n: "
                        )
                        sessions(mood, e)
                        break
                    else:
                        print(f"Error VE2 ")
                        print(
                            f"There seems to be an error (VE2 = the number inputted is not in range of 0-10 ) with processing your input please recheck your input!"
                        )

                
            else:
                while True:

                    num = bin.ERRORS.error_checker(int, ind=(input('\nNumber of sessions: ')), type_var=int,
                                                   forbidden=str)
                    special = input('do you want very speicial sessions ? ;) y/ : ')
                    if num:
                        break
                    print('The value you entered cant be read by the app!')
                sessions(num, False, bool(special))



        except (FileNotFoundError) as e:
            print(f"Error VE1 wtf")
            print(
                f"There seems to be an error (VE1) with processing your input please recheck your input"
            )


def sessions(mood, use_c, special=False):
    if use_c:
        now = models.datetime.now()
        sessions_s = constants.standard_session_num
        today_date = datetime.date.today()

        # Get the day name
        parm = today_date.strftime("%A")
        bonus = constants.bonus
        if use_c == 'v':
            evil_bonus = 0.5

        if parm in constants.schooldays:
            sessions_s = ((sessions_s * 0.65) * (mood / 5)) * (bonus[use_c])
        else:
            sessions_s = ((sessions_s * 1.35) * (mood / 7.5)) * (bonus[use_c])
        sessions_s = sessions_s * confi['co_efficent']
    else:
        sessions_s = mood

    if sessions_s < 1:
        print(f"You should take a break today {confi['name']}!. Enjoy yourself!")
        quit()
    else:
        input(f"Are you ready {confi['name']}!? ")
        
        t = TimerClass(confi['session_time'] * 15, models.math.ceil(sessions_s), special)
        t.run()

def play_sound():
    winsound.PlaySound("dank", winsound.SND_ALIAS)

if __name__ == "__main__":

        before_start()



