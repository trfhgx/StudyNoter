import os
from pydub import AudioSegment
from pydub.playback import play
import pathlib
import random

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def playsong(song ,t, f, speed_co, sessions, real_sessions):

    c = (pathlib.Path(t).parent.resolve())
    if "finish" in song:
        ts = random.randint(1,2)
        song = song+str(ts)+'.wav'
        g = (str(c) + f'/Music/ost/{song}')
    else:
        song = random.choice([i for i in os.listdir(str(c)+"/Music/ost") if 'start' in i and 'wav' in i])

        g = (str(c) + f'/Music/ost/{song}')
    rem = song

    if os.name == "posix":
        song = AudioSegment.from_wav(g)
    else:
        song = AudioSegment.from_wav(g.replace('/', '\\'))
    f += 1
    x = 2 * speed_co * ((sessions ** -1)) + 0.2

    if f == 0:
        speed = 1.2
        song = speed_change(song, speed)
    else:
        speed = x + (f / 6) * (speed_co ** -1)
        song = speed_change(song, speed)
    if "start" in rem:
        print("Speed is %.2f" % (speed * 100 - 100), "%",
              "Slower" if speed * 100 - 100 < 0 else "Faster" + " Than the original")

    play(song)


