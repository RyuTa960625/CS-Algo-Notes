import sys
from collections import deque


input = sys.stdin.readline

t = int(input())

def bfs(start, cnt):
    queue = deque([start])
    visited[start] = True

    while queue:
        visiting_node = queue.popleft()

        if visited.count(True) == n:
            return cnt

        for item in graph[visiting_node]:
            if not visited[item]:
                visited[item] = True
                queue.append(item)

                cnt += 1

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (1 + n)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1, 0))