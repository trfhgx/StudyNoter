import random, time

trys = 10

true = 0
mode = input('+ or x : ')
st = time.time()

while trys > 0:
    tt = time.time()

    x = 7
    y = random.randint(2, 9)



    question = int(input(f'what is {x} {mode} {y} = '))
    et = time.time()

    elapsed_time = et - tt
    print(f'time taken: {int(elapsed_time)}')

    if mode == '+':
        print(x + y)

        if question == x + y:
            print('correct')
            true += 1
    else:
        print(x * y)

        if question == x * y:
            print('correct')
            true += 1
    trys -= 1

et = time.time()

# get the execution time
elapsed_time = et - st
elapsed_time -= 5
print(int(elapsed_time))
print(true)
print(f'Your score is {int((true * 10) / (elapsed_time * 0.8))}/10')