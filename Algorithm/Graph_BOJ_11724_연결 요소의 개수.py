N, M = map(int, input().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

cnt = 0
for i in range(1, N + 1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)