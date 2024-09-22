from collections import deque
def bfs(tlst):
    for i,j in tlst:
        arr[i][j]=1

    q = deque()
    w = [[0]*M for _ in range(N)]
    cnt = CNT-3

    for ti,tj in virus:
        q.append((ti,tj))
        w[ti][tj]=1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and w[ni][nj]==0 and arr[ni][nj]==0:
                q.append((ni,nj))
                w[ni][nj]=1
                cnt-=1

    for i,j in tlst:
        arr[i][j]=0
    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            lst.append((i,j))
        elif arr[i][j]==2:
            virus.append((i,j))

CNT = len(lst)
v = [0]*CNT
ans = 0

for i in range(CNT-2):
    for j in range(i+1, CNT-1):
        for k in range(j+1, CNT):
            ans = max(ans, bfs([lst[i],lst[j],lst[k]]))
print(ans)