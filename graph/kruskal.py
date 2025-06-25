weights = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5),
        (1, 6, 3), (2, 3, 9), (3, 5, 4), (3, 6, 8),
        (2, 4, 7), (2, 5, 2), (4, 6, 1), (5, 6, 6)]
weights.sort(key=lambda x:x[2])

p = [i for i in range(7)]

def find(u):
    if p[u] == u:
        return p[u]
    p[u] = find(p[u])
    return p[u]

def union(u, v):
    u = find(u)
    v = find(v)
    p[u] = v

mst = []
cost = 0
size = 0

for w in weights:
    if find(w[0]) != find(w[1]):
        union(w[0], w[1])
        mst.append(w[:2])
        cost += w[2]
        size += 1
        
        if size == 7:
            break

print("MST:", *mst)
print("Cost:", cost)