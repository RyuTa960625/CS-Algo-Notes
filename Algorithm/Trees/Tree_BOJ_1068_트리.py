n = int(input())
maps = list(map(int, input().split()))
delete = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    if maps[i] != -1:
        if i != delete:
            graph[maps[i]].append(i)

def dfs(a):
    while graph[a]:
        x = graph[a].pop()
        dfs(x)

    graph[a].append(False)

dfs(delete)

cnt = 0
for i in range(n):
    if not graph[i]:
        cnt += 1

print(cnt)