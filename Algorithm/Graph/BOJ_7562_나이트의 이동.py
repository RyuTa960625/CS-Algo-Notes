from collections import deque

def bfs():
    while check:
        x, y = check.popleft()
        if x == xd and y == yd:
            return board[x][y]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                check.append([nx, ny])


t = int(input())
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

for i in range(t):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    x, y = map(int, input().split())
    xd, yd = map(int, input().split())
    check = deque()
    check.append([x, y])
    print(bfs())