def solve(k, lst):
    ans = 0
    for i in range(1, k):
        for j in range(i + 1, k + 1):
            cnt = 0
            for c in range(1, k + 1):
                a = min(abs(c - i), abs(c - j))
                b = min(abs(c - x) for x in lst)
                if a < b:
                    cnt += 1
            ans = max(ans, cnt)
    return ans / k


for case in range(int(input())):
    n, k = map(int, input().split())
    (*lst,) = map(int, input().split())
    ans = solve(k, lst)
    print(f"Case #{case+1}: {ans}")
