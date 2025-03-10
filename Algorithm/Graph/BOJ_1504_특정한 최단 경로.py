import sys, heapq
INF = int(1e9)

N, E = map(int,input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int,sys.stdin.readline().rstrip().split())

    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int,input().split())

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    D[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if D[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(que, (cost,i[0]))

root_A, root_B = 0, 0

D = [INF] * (N + 1)
dijkstra(1)
root_A += D[v1]
root_B += D[v2]

D = [INF] * (N + 1)
dijkstra(v1)
root_A += D[v2]
root_B += D[N]

D = [INF] * (N + 1)
dijkstra(v2)
root_A += D[N]
root_B += D[v1]

ans = min(root_A, root_B)

if ans >= INF:
    print(-1)
else:
    print(ans)