import os
from pydub import AudioSegment
from pydub.playback import play
import pathlib
import bin.config as config
file_version = '4.0.0 alpha'

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

def playsong(song ,t, f, speed_co):

    c = (pathlib.Path(t).parent.resolve())

    g = (str(c)+f'/Music/ost/{song}')

    if os.name == "posix":
        song = AudioSegment.from_wav(g)
    else:
        song = AudioSegment.from_wav(g.replace('/', '\\'))
    song = speed_change(song, 1 + (f / 10) * (speed_co ** -1))
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

