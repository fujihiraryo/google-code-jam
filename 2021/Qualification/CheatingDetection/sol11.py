m = 10000
n = 100
t = int(input())
p = int(input())
for case in range(t):
    x = []
    for _ in range(n):
        x.append([int(c) for c in input()])
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
    susp = [0] * n
    for j in range(20, 80):
        i = min(range(n), key=lambda i: diff[i][j] / diff[i][0])
        susp[i] += 1
    ans = max(range(n), key=lambda i: susp[i])
    print(f"Case #{case+1}: {ans+1}")
