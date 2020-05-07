import random
a = [1, 2, 3, 4]
b = [10, 10, 2, 1]
c = [1, 1, 1, 1]

for x in range(0, 4):
    c.insert(0, a[x] * b[x])

print(c)

print(round(random.random(), 3), round(random.random(), 3), round(random.random(), 3))
