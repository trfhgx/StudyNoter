from playsound import playsound
import pathlib


c = str(pathlib.Path(__file__).parent.resolve())

def finish():
    playsound(c+'/Music/ost/finish1.wav')

def start():
    playsound(c+'/Music/ost/start.mp3')
