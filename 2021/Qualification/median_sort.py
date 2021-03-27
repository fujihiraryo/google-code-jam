from itertools import combinations

t, n, q = map(int, input().split())
for _ in range(t):
    ans = list(range(1, n + 1))
    for i, j, k in combinations(range(n), 3):
        print(ans[i], ans[j], ans[k], flush=True)
        res = int(input())
        if res == ans[i]:
            ans[i], ans[j] = ans[j], ans[i]
        if res == ans[k]:
            ans[j], ans[k] = ans[k], ans[j]
    print(*ans, flush=True)
    res = int(input())
    if res == -1:
        exit()
