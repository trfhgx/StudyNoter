import os
import sys

def error_CD():
    print('A major error(CD=Config_Damage) has been detected')
    print('Fixing the error...')
    os.remove('bin/config.json')
    input('Please proceed by clicking enter and reopening the app')
    sys.exit()