import json
import os
import time
from pathlib import Path
import bin.ERRORS as error
from bin.constants import standard_session_time, defualt_data


   

filename = "bin/config.json"


def changelog():
    s = True
    data_needed = list(defualt_data)
    while s:
        print("type the following number to change the correct section")
        for i, t in enumerate(data_needed):
            print(f"{i + 1}: to change {t.replace('_', ' ')}")
        print(f"6: if you finished changing your config")
        try:
            t = int(input("")) - 1
            with open(filename, "r") as f:
                jpt = json.load(f)
                if t == 5:
                    break
                old_value = jpt[data_needed[t]]
                change = input(
                    f'change {data_needed[t]} value to ("{old_value}" is the old value): '
                )

                if data_needed[t] != "name":

                    if not change.replace(".", "").isnumeric():
                        print("\nthats not a vaild number! please try again \n")
                        continue
                    jpt[data_needed[t]] = float(change)
                else:
                    jpt[data_needed[t]] = change

                print(
                    f'\nYour {data_needed[t]} has been changed from "{old_value}" to "{change}" successfully!'
                )
                time.sleep(0.5)
            os.remove(filename)
            with open(filename, "w") as f:

                json.dump(jpt, f, indent=4)

        except (KeyError, ValueError):
            print("This key doesnt exist please recheck the number you entered!")
    return jpt


def check(key, maxx):
    try:
        if int(key) < 1 or int(key) > maxx:
            raise ValueError
    except ValueError:
        print("ErrorVE1 please retry and recheck your input!")
        return False
    else:
        return True


def load_config():
    if Path(filename).is_file():
        with open(filename, "r") as e:
            try:
                file = json.load(e)
            except json.decoder.JSONDecodeError:
                error.error_CD()
            config = file
        key = input(
            f"Hello {config['name']}!! welcome back to studyNoter. please type \n 1 /if you would like to continue \n 2 /if you would like to change your config \n 3 /if you would like to go with default config \n 4 /if you would like to take a look at your config and reload \n "
        )
        if not check(key, 4):
            load_config()
            
        else:
            if key == "3":
                config = defualt_data
            elif key == "2":
                config = changelog()
            elif key == "4":
                print(config)
                time.sleep(1)
                config = load_config()
    else:
        key = input(
            f"Hello welcome to studyNoter!. please type \n 1 /if you would like to go with default config \n 2 /if you would like to set your own config \n"
        )

        if not check(key, 2):
            load_config()
        else:
            if key == "1":
                config = defualt_data
            else:
                dicts = {}
                for i in list(defualt_data):
                    while True:
                        new = input(f"set {i} value to: ")
                        if i != "name":
                            if not new.replace(".", "").isnumeric():
                                print("thats not a number! please retry again")
                                continue
                            dicts[i] = float(new)
                        else:
                            dicts[i] = new
                        break

                with open(filename, "w") as g:
                    json.dump(dicts, g, indent=4)
                    config = dicts
    config['co_efficent'] = standard_session_time / config['session_time']
    return config
