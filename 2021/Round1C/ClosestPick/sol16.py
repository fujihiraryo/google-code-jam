def solve0(k, lst):
    lst.sort()
    sub = [(lst[i + 1] - lst[i]) // 2 for i in range(len(lst) - 1)]
    if 1 not in lst:
        sub.append(lst[0] - 1)
    if k not in lst:
        sub.append(k - lst[-1])
    sub.sort(reverse=True)
    if len(sub) >= 2:
        return (sub[0] + sub[1]) / k
    return sub[0] / k


def solve1(k, lst):
    lst.sort()
    sub = [lst[i + 1] - lst[i] - 1 for i in range(len(lst) - 1)]
    return max(sub) / k


def solve(k, lst):
    lst = list(set(lst))
    if len(lst) == 1:
        return (k - 1) / k
    return max(solve0(k, lst), solve1(k, lst))


for case in range(int(input())):
    n, k = map(int, input().split())
    (*lst,) = map(int, input().split())
    ans = solve(k, lst)
    print(f"Case #{case+1}: {ans}")
