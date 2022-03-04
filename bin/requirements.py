import subprocess
import sys
def install():
    print('ERROR M1/// running some code to fix it...')
    with open('bin/requirements ', 'r') as t:
        print('Downloading requirements')
        for i in t.readlines():
            subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                                   i])
        print('\n Finished installing please proceed by rerunning the program')
