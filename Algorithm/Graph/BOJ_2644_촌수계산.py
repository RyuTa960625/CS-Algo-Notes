import sys
from collections import deque

def bfs():
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        if x == b:
            return visit[b]
        for i in graph[x]:
            if not visit[i]:
                visit[i] = visit[x] + 1
                q.append(i)
    return -1

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
visit = [0]*(n+1)

print(bfs())