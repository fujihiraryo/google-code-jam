MAX = 1234567
LIST = []
for cnt in range(2, 7 + 1):
    start = 1
    while int("".join(str(start + i) for i in range(cnt))) <= MAX:
        x = int("".join(str(start + i) for i in range(cnt)))
        LIST.append(x)
        start += 1
LIST.sort()


def solve(y):
    for x in LIST:
        if x > y:
            return x


for case in range(int(input())):
    y = int(input())
    ans = solve(y)
    print(f"Case #{case+1}: {ans}")
