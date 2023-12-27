x = 433
y = 6
t = 1
for i in reversed(range(x)):
    if i % y == 0:
        if i / 4 % 2 != 0:
            t += 1 * y
        print(f'the left outs are {x - i}')
        print(f'so the final answer is: {t}π/{y}')
        break

div , rem = divmod(x, y)
t = 1
i = div * y
if i / 4 % 2 != 0:
    t += 1 * y
print(f'the left outs are {rem}')
print(f'so the final answer is: {t}π/{y}')
