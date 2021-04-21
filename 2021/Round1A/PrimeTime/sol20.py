from collections import defaultdict

MAX = 50000


class Sieve:
    def __init__(self, n):
        table = [i for i in range(n)]
        for i in range(2, n):
            if table[i] != i:
                continue
            for j in range(2 * i, n, i):
                table[j] = i
        self.table = table

    def factorize(self, x):
        y = x
        factor = defaultdict(int)
        while y > 1:
            factor[self.table[y]] += 1
            y //= self.table[y]
        return factor


sieve = Sieve(MAX)
for case in range(int(input())):
    m = int(input())
    deck = [map(int, input().split()) for _ in range(m)]
    cnt = defaultdict(int)
    total = 0
    for p, n in deck:
        cnt[p] = n
        total += p * n
    for x in range(max(0, total - MAX), total)[::-1]:
        factor = sieve.factorize(x)
        if any(cnt[p] < factor[p] for p in factor):
            continue
        if sum(p * (cnt[p] - factor[p]) for p in cnt) == x:
            break
    print(f"Case #{case+1}: {x}")
