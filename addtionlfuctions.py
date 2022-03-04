import sys
import subprocess
import os
try:
    from playsound import playsound
except Exception:
        print('there seems to be an error! no worries Ill fix it for you right away')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                               'playsound==1.2.2'])
        from playsound import playsound
import pathlib


c =(pathlib.Path(__file__).parent.resolve())
def finish():
    g = (str(c)+'/Music/ost/finish1.wav').replace(" ", "%20")
    if os.name == "posix":
        playsound(g)
    else:
        playsound(g.replace('/', '\\'))
def start():
    g =(str(c)+'/Music/ost/start.mp3').replace(" ", "%20")
    if os.name == "posix":
        playsound(g)
    else:
        playsound(g.replace('/', '\\'))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
