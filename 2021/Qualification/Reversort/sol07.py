def reversort(lst):
    n = len(lst)
    cnt = 0
    for i in range(n - 1):
        j = min(range(i, n), key=lambda j: lst[j])
        cnt += j - i + 1
        lst[i : j + 1] = lst[i : j + 1][::-1]
    return cnt


t = int(input())
for i in range(t):
    input()
    (*lst,) = map(int, input().split())
    cnt = reversort(lst)
    print(f"Case #{i+1}: {cnt}")
