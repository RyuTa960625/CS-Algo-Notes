n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

DP = [0] * (k + 1)
DP[0] = 1
for c in coins:
    for i in range(c, k + 1):
        DP[i] += DP[i - c]
print(DP[k])