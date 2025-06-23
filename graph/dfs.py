adj_list = [[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]

visited = [False for i in range(len(adj_list))]

def dfs(cur):
    print(cur, end = " ")
    
    for child in adj_list[cur]:
        if not visited[child]:
            visited[child] = True
            dfs(child)

for i in range(len(adj_list)):
    if not visited[i]:
        visited[i] = True
        dfs(i)