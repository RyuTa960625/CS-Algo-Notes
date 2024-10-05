N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N - 1, -1, -1):
    if K == 0:
        break

    cnt += K // coin[i]
    K %= coin[i]

print(cnt)