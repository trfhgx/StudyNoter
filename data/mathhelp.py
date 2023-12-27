
import random



def F(x):
    return x + 3


while True:
    options = ['صورة', 'سابقة']
    print(options)
    option_now = random.choice(options)
    random = random.randint(0, 60)





    if option_now == 'سابقة':
        question = input(f'what is the {option_now} of {random} for the equation F(x) = x + 3 // {random} = x + 3 : ')
        if random == F(int(question)):
            print('Correct!')
        else:
            print('wrong')
    else:
        question = input(f'what is the {option_now} of {random} for the equation F(x) = x + 3 :')
        if int(question) == F(random):
            print('correct')
        else:
            print('wrong!')

