from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    building = [[] for _ in range(n + 1)]
    time = [0] + list(map(int, input().split()))
    indegree = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        building[x].append(y)
        indegree[y] += 1
    win_building = int(input())

    q = deque()
    spend_time = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            spend_time[i] = time[i]

    while q:
        now = q.popleft()
        if now == win_building:
            break
        for nx in building[now]:
            indegree[nx] -= 1
            spend_time[nx] = max(spend_time[nx], spend_time[now] + time[nx])
            if indegree[nx] == 0:
                q.append(nx)

    print(spend_time[win_building])