from collections import defaultdict

MAX = 500
is_prime = [1] * MAX
is_prime[0], is_prime[1] = 0, 0
for i in range(2, MAX):
    if not is_prime[i]:
        continue
    for j in range(2 * i, MAX, i):
        is_prime[j] = 0
prime_list = [i for i in range(MAX) if is_prime[i]]


def factorize(x):
    factor = defaultdict(int)
    y = x
    for p in prime_list:
        while y % p == 0:
            y //= p
            factor[p] += 1
    if y != 1:
        factor[y] = 1
    return factor


def solve(deck):
    total = 0
    for p in deck:
        total += p * deck[p]
    min_cand = max(1, total - 3 * 10 ** 4)
    for x in range(min_cand, total)[::-1]:
        factor = factorize(x)
        if any(deck[p] < factor[p] for p in factor):
            continue
        if sum(p * (deck[p] - factor[p]) for p in deck) == x:
            return x
    return 0


for case in range(int(input())):
    deck = defaultdict(int)
    for _ in range(int(input())):
        p, n = map(int, input().split())
        deck[p] = n
    ans = solve(deck)
    print(f"Case #{case+1}: {ans}")
