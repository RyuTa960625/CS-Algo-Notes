N = int(input())

dp = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = int(i / 3) + int(i % 3)

if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')