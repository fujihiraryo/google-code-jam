for case in range(int(input())):
    n = int(input())
    (*x,) = input().split()
    ans = 0
    for i in range(n - 1):
        x0, x1 = x[i], x[i + 1]
        k0, k1 = len(x0), len(x1)
        if int(x0[:k1]) < int(x1):
            ans += max(0, k0 - k1)
            x[i + 1] += "0" * (k0 - k1)
        elif int(x0[:k1]) == int(x1):
            if x0[k1:] == "9" * (k0 - k1):
                ans += k0 - k1 + 1
                x[i + 1] += "0" * (k0 - k1 + 1)
            else:
                ans += k0 - k1
                x[i + 1] += str(int(x0[k1:]) + 1).zfill(k0 - k1)
        else:
            ans += k0 - k1 + 1
            x[i + 1] += "0" * (k0 - k1 + 1)
    print(f"Case #{case+1}: {ans}")
