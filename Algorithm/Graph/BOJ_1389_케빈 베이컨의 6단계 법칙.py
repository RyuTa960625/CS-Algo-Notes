from collections import deque

def bfs(s):
    global ans, ans_cnt, n
    dis = [-1] * (n + 1)
    dis[0] = 0

    q = deque()

    q.append(s)
    dis[s] = 0

    while q:
        px = q.popleft()

        for nxt in graph[px]:
            if dis[nxt] != -1:
                continue

            dis[nxt] = dis[px] + 1
            q.append(nxt)

    total = sum(dis)
    
    if total < ans_cnt:
        ans = s
        ans_cnt = total
    elif total == ans_cnt:
        if s < ans:
            ans = s


n, m = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = list(map(int, input().split()))

    graph[s].append(e)
    graph[e].append(s)

ans = int(1e9)
ans_cnt = int(1e9)
for s in range(1, n + 1):
    bfs(s)

print(ans)