from itertools import product

t = int(input())
for case in range(t):
    m = int(input())
    ps, ns = [], []
    for _ in range(m):
        p, n = map(int, input().split())
        ps.append(p)
        ns.append(n)
    ans = 0
    for xs in product(*[range(n + 1) for n in ns]):
        sums = 0
        pros = 1
        for i in range(m):
            sums += ps[i] * xs[i]
            pros *= ps[i] ** (ns[i] - xs[i])
        if sums == pros:
            ans = max(ans, sums)
    print(f"Case #{case+1}: {ans}")
