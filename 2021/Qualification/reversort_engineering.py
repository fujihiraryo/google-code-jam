from itertools import permutations


def reversort_cost(a):
    n = len(a)
    cost = 0
    for i in range(n - 1):
        j = min(range(i, n), key=lambda j: a[j])
        cost += j - i + 1
        a[i : j + 1] = a[i : j + 1][::-1]
    return cost


def full_search(n, c):
    for a in permutations(range(1, n + 1)):
        if reversort_cost(list(a)) == c:
            return " ".join([str(x) for x in a])
    return "IMPOSSIBLE"


for case in range(int(input())):
    n, c = map(int, input().split())
    ans = full_search(n, c)
    print(f"Case #{case+1}: {ans}")
