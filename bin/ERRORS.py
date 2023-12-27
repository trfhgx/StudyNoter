import os

def error_CD():
    print('Oh NO! A major error(CD2=Config_Damage) has been detected')
    print('Fixing the error...')
    os.remove('bin/config.json')
    input('SUCCESS! Please proceed by clicking enter and reopening the app')
    quit()


def error_checker(*args, ind, type_var, forbidden=None):
    try:    
        if isinstance(ind, type_var):
            return ind
        else:
            return type_var(ind)
    except ValueError:
        if args and not isinstance(ind, forbidden):
            for i in args:
                ind = i(ind)
            return ind
        return None

"""
    try:
        value = type_var(ind)
        return value
    except ValueError:
        return None
"""
