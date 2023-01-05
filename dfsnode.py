def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
# 각 노드가 연결된 정보를 표현
graph = [
    [], # 0번
    [2, 3, 8], # 1번노드와 연결
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7] # 8번노드와 연결
]

visited = [False] * 9

dfs(graph, 1, visited)