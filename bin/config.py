import json
import os
from pathlib import Path

data = {1:'name', 2:'session time', 3:'break time', 4:'bonus break time', 5:'long break time'}
version = 'v5.0.0 Alpha'
class Config():
    def __init__(self, name='Joe', session_time=50, break_time=10, bonus_break=3, long_break=65):
        self.name = name
        self.session_time = session_time
        self.break_time = break_time
        self.bonus_break = bonus_break
        self.long_break = long_break


filename = 'bin/config.json'

def changelog():
        s = True
        while s:
            print('type the following number to change the correct section')
            for i in data.keys():
                print(f'{i}: to change {data[i]}')
            print(f"6: if you finished changing your config")
            try:
                t = int(input(''))
                if t == 6:
                    break
                with open(filename, 'r') as f:
                    jpt = json.load(f)
                    change = input(f'change {data[t]} value to: ')

                    if data[t] != 'name':

                        if not change.isnumeric():
                            print('\n thats not a number! please try again \n')
                            continue
                    jpt[data[t]] = change
                os.remove(filename)
                with open(filename, 'w') as f:

                    json.dump(jpt, f, indent=4)

            except (KeyError, ValueError):
                print('This key doesnt exist please recheck the number you entered!')

        config = Config(jpt[data[1]], jpt[data[2]], jpt[data[3]], jpt[data[4]], jpt[data[5]])

        return config


def check(key, max):
    try:
        if int(key) < 1 or int(key) > max:
            raise ValueError
        return True
    except ValueError:
        print('ERROR V1 please RETRY and RECHECK your input!')
        return False


def load_config():
    if Path(filename).is_file():
        with open(filename, 'r') as e:
            file = json.load(e)
            config = Config(file[data[1]], file[data[2]], file[data[3]], file[data[4]], file[data[5]])
        key = input(
            f'Hello {config.name}!! welcome back to studyNoter {version}!. please type \n 1 /if you would like to continue \n 2 /if you would like to change your config \n 3 /if you would like to go with default config \n 4 /if you would like to take a look at your config and continue \n ')
        if not check(key, 4):
            load_config()
        else:
            if key == '3':
                config = Config()
            elif key == '2':
                config = changelog()
            elif key == '4':
                with open(filename, 'r') as nr:
                    nr = json.load(nr)
                    print(nr)


    else:
        key = input(f'Hello welcome to studyNoter {version}!. please type \n 1 /if you would like to go with default config Highly recommended \n 2 /if you would like to set your own config \n')


        if not check(key, 2):
            load_config()
        else:
            if key == '1':
                config = Config()
            else:
                l = True
                while l:
                    dicts = {}
                    for i in data.values():
                        set = input(f'set {i} value to: ')
                        if i != 'name':
                            if not set.isnumeric():
                                l = True
                                print('thats not a number! pleas retry again')
                                break
                            else:
                                l = False
                                dicts[i] = set
                        else:
                            dicts[i] = set

                with open(filename, 'w') as g:
                    json.dump(dicts, g, indent=4)
                    config = Config(dicts[data[1]], dicts[data[2]], dicts[data[3]], dicts[data[4]], dicts[data[5]])



    return config
