import random
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


n = 10
m = 10
s = [random.uniform(-3, 3) for _ in range(n)]
q = [random.uniform(-3, 3) for _ in range(m)]
x = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == n - 1 and random.randrange(2) == 1:
            x[i][j] = 1
            continue
        u = random.random()
        if u < sigmoid(s[i] - q[j]):
            x[i][j] = 1
        else:
            x[i][j] = 0

cnt = [0] * m
for i in range(n):
    for j in range(m):
        if x[i][j]:
            cnt[j] += 1

diff = [[0] * (n + 1) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if x[i][j]:
            diff[i][cnt[j]] += 1
    for j in range(n)[::-1]:
        diff[i][j] += diff[i][j + 1]
    print(s[i], x[i], diff[i])
