N, K = map(int, input().split())

dp = [[0 for x in range(N + 1)] for x in range(K)]

for t in range(K):
    dp[t][0] = 1

for t in range(N + 1):
    dp[0][t] = 1

for x in range(1, K):
    for y in range(1, N + 1):
        dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % 1000000000

print(dp[-1][-1] % 1000000000)