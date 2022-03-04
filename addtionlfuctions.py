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


c = str(pathlib.Path(__file__).parent.resolve())
def finish():
    g = c+'/Music/ost/finish1.wav'
    if os.name == "posix":
        playsound(g)
    else:
        playsound(g.replace('/', '\\'))

def start():
    g = 'Music/ost/start.mp3'
    if os.name == "posix":
        playsound(g)
    else:
        playsound(g.replace('/', '\\'))


