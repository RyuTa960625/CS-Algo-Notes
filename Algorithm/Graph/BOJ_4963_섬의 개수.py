import sys
sys.setrecursionlimit(10**6)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dsf(graph, x, y, visit):

        for _ in range(8):
            nx = x + dx[_]
            ny = y + dy[_]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and visit[nx][ny] == False:
                visit[nx][ny] = True
                dsf(graph, nx, ny, visit)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                dsf(island, i, j, visited)
                cnt += 1

    print(cnt)