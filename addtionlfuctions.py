from playsound import playsound
import pathlib
c = pathlib.Path(__file__).parent.resolve()

print(c)

def finish():
    playsound(str(c)+'/Music/ost/finish1.wav')

def start():
    playsound(str(c)+'/Music/ost/start.mp3')
