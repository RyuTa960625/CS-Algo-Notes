import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
maps = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    maps[start][end] = min(cost, maps[start][end])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if maps[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(maps[i][j], end=" ")
    print()