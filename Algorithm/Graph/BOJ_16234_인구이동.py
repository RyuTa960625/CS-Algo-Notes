# [1] bfs를 루프내에 구현 (상대적으로 빠름: 700mS)
from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while ans<=2000:
    # [1] 전체를 순회하면서, 미방문=>연합처리
    q = deque()
    v = [[0]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:                # 미방문

                q.append((i, j))  # 큐에 초기데이터 삽입
                v[i][j] = 1  # 방문표시
                alst = [(i, j)]  # 연합에 추가
                sm = arr[i][j]  # 합계

                while q:
                    ci, cj = q.popleft()
                    # 네방향, 범위내, 미중복, *조건맞으면(L<=인구차이<=R)
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                            q.append((ni, nj))
                            v[ni][nj] = 1
                            alst.append((ni, nj))
                            sm += arr[ni][nj]
                if len(alst) > 1:   # 연합인 경우 처리(평균값 각각 저장)
                    for ti, tj in alst:
                        arr[ti][tj] = sm // len(alst)
                    flag = 1        # 연합이 있는 경우 1 리턴
    if flag==0:                     # 이동이 없었음
        break
    ans+=1
print(ans)