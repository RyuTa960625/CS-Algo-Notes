import heapq
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dij(start):
    q = []
    distance = [1e9] * (n+1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return node, dist

first_end, first_dist = dij(1)
second_end, second_dist = dij(first_end)
print(second_dist)