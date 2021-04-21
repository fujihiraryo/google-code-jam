from collections import defaultdict


def cost(a):
    global x
    global y
    cnt01, cnt10 = 0, 0
    for i in range(len(a) - 1):
        if a[i] == 0 and a[i + 1] == 1:
            cnt01 += 1
        if a[i] == 1 and a[i + 1] == 0:
            cnt10 += 1
    return cnt01 * x + cnt10 * y


def full_search(a):
    idx = []
    for i, c in enumerate(a):
        if a[i] == -1:
            idx.append(i)
    n = len(idx)
    min_cost = 10 ** 20
    for s in range(1 << n):
        b = a[:]
        for i in range(n):
            if (1 << i) & s:
                b[idx[i]] = 1
            else:
                b[idx[i]] = 0
        min_cost = min(min_cost, cost(b))
    return min_cost


class Dinic:
    def __init__(self, graph, start, goal, INF=1 << 30):
        n = len(graph)
        self.size = n
        self.graph = graph
        self.start = start
        self.goal = goal
        self.INF = INF

    def bfs(self):
        self.dist = [self.INF] * self.size
        self.dist[self.start] = 0
        queue = [self.start]
        for x in queue:
            for y in self.graph[x]:
                if self.graph[x][y] == 0 or self.dist[y] < self.INF:
                    continue
                self.dist[y] = self.dist[x] + 1
                queue.append(y)

    def dfs(self, x, flow):
        if x == self.goal:
            return flow
        for y in self.graph[x]:
            capa = self.graph[x][y]
            if capa == 0 or self.dist[x] >= self.dist[y] or y in self.checked[x]:
                continue
            self.checked[x].add(y)
            f = self.dfs(y, min(flow, capa))
            if f:
                self.graph[x][y] -= f
                self.graph[y][x] += f
                return f
        return 0

    def max_flow(self):
        res = 0
        while True:
            self.bfs()
            if self.dist[self.goal] == self.INF:
                return res
            flow = self.INF
            self.checked = [set() for _ in range(self.size)]
            while flow:
                flow = self.dfs(self.start, self.INF)
                res += flow


INF = 1 << 30
for case in range(int(input())):
    x, y, string = input().split()
    x, y = int(x), int(y)
    a = []
    for c in string:
        if c == "C":
            a.append(0)
        if c == "J":
            a.append(1)
        if c == "?":
            a.append(-1)
    n = len(a)
    graph = [defaultdict(int) for _ in range(n + 2)]
    for i in range(n):
        if a[i] == 0:
            graph[0][i + 1] = INF
        elif a[i] == 1:
            graph[i + 1][n + 1] = INF
        if i == n - 1:
            continue
        if a[i] != 1 and a[i + 1] != 0:
            graph[i + 1][i + 2] = x
        if a[i] != 0 and a[i + 1] != 1:
            graph[i + 2][i + 1] = y
    ans = Dinic(graph, 0, n + 1).max_flow()
    print(f"Case #{case+1}: {ans}")
