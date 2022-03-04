import os
from pydub import AudioSegment
from pydub.playback import play
import pathlib

file_version = '3.5.0 alpha'



def finish(t):
    c = (pathlib.Path(t).parent.resolve())

    g = (str(c)+'/Music/ost/finish1.wav')

    if os.name == "posix":
        song = AudioSegment.from_wav(g)
    else:
        song = AudioSegment.from_wav(g.replace('/', '\\'))
    play(song)

def start(t):
    c = (pathlib.Path(t).parent.resolve())
    g =(str(c)+'/Music/ost/start.mp3')
    if os.name == "posix":
        song = AudioSegment.from_mp3(g)
    else:
        song = AudioSegment.from_mp3(g.replace('/', '\\'))
    play(song)

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

