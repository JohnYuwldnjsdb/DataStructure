N = 7
s = 0
g = [[] for i in range(N)]

g[0] = [(1, 9), (2, 10)]
g[1] = [(0, 9), (3, 10), (4, 5), (6, 3)]
g[2] = [(0, 10), (3, 9), (4, 7), (5, 2)]
g[3] = [(1, 10), (2, 9), (5, 4), (6, 8)]
g[4] = [(1, 5), (2, 7), (6, 1)]
g[5] = [(2, 2), (3, 4), (6, 6)]
g[6] = [(1, 3), (3, 8), (4, 1), (5, 6)]

visited = [False for i in range(N)]
D = [float('inf') for i in range(N)]
D[s] = 0

ans = 0

for k in range(N):
    m = -1
    minV = float("inf")
    
    for j in range(N):
        if not visited[j] and D[j] < minV:
            minV = D[j]
            m = j
    visited[m] = True
    ans += minV
    
    for u, w in g[m]:
        if not visited[u]:
            if w < D[u]:
                D[u] = w

print(ans)