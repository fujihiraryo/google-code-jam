def count2(x0, x1):
    if x0 < x1:
        return 0
    for a in range(10):
        if x0 < 10 * x1 + a:
            return 1
    for a in range(10):
        for b in range(10):
            if x0 < 100 * x1 + 10 * a + b:
                return 2
    return 3


def count3(x0, x1, x2):
    cnt = 5
    if x0 < x1:
        cnt = min(cnt, count2(x1, x2))
    for a in range(10):
        if x0 < 10 * x1 + a:
            cnt = min(cnt, 1 + count2(10 * x1 + a, x2))
    for a in range(10):
        for b in range(10):
            if x0 < 100 * x1 + 10 * a + b:
                cnt = min(cnt, 2 + count2(100 * x1 + 10 * a + b, x2))
    return cnt


t = int(input())
for case in range(t):
    n = int(input())
    (*x,) = map(int, input().split())
    if n == 2:
        ans = count2(x[0], x[1])
    if n == 3:
        ans = count3(x[0], x[1], x[2])
    print(f"Case #{case+1}: {ans}")
