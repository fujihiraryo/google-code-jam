INF = 1 << 32
MAX = 2 ** 20


def bitnot(x):
    size = len(bin(x)) - 2
    return (1 << size) - 1 - x


def to_int(s):
    res = 0
    tmp = 1
    for c in s[::-1]:
        res += tmp * int(c)
        tmp *= 2
    return res


def solve(x, y):
    if max(x, y) >= MAX:
        return None
    dist = [INF] * MAX
    dist[x] = 0
    queue = [x]
    for i in queue:
        if 2 * i < MAX and dist[2 * i] > dist[i] + 1:
            queue.append(2 * i)
            dist[2 * i] = dist[i] + 1
        j = bitnot(i)
        if dist[j] > dist[i] + 1:
            queue.append(j)
            dist[j] = dist[i] + 1
    return dist[y]


for case in range(int(input())):
    s, e = input().split()
    x, y = to_int(s), to_int(e)
    ans = solve(x, y)
    if ans == INF:
        ans = "IMPOSSIBLE"
    print(f"Case #{case+1}: {ans}")
