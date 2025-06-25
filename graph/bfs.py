from collections import deque

adj_list = [[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]

visited = [False for i in range(len(adj_list))]

def bfs():
    while que:
        cur = que.popleft()
        print(cur, end = " ")
        
        for child in adj_list[cur]:
            if not visited[child]:
                visited[child] = True
                que.append(child)

que = deque()

for i in range(len(adj_list)):
    if not visited[i]:
        visited[i] = True
        que.append(i)
        bfs()