T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    charger = [0] * (N + 1)

    for i in arr:
        charger[i] += 1

    now_p = 0
    result = 0
    while now_p < N and result != -1:
        for m in range(K):
            if now_p + K - m < N:
                if charger[now_p + K - m] == 1:
                    now_p = now_p + K - m
                    result += 1
                    break
            elif now_p + K - m == N:
                now_p = now_p + K - m
                break
        else:
            result = -1

    if result < 0:
        result = 0

    print(f'#{tc} {result}')