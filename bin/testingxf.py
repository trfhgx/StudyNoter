import os
import random
print(os.path.dirname(os.path.realpath(__file__)))
songs = random.choice([i for i in os.listdir("../Music/ost") if 'start' in i and 'wav' in i])
print(songs)