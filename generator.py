import random

l = []
n = 10000000

for i in range(n):
    l.append(random.randint(1, 1000000000))

print(l)

with open('numbers.txt', 'w') as w:
    for numbers in l:
        w.write('%s\n' %numbers) 
