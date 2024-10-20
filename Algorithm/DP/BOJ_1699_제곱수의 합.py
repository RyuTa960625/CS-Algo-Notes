n = int(input())

dp = [0 for _ in range(n+1)]
s = [i**2 for i in range(1, 317)]

for i in range(1, n+1):
    min_list = []
    for j in s:
        if j > i:
            break
        min_list.append(dp[i-j])

    dp[i] = min(min_list) + 1

print(dp[-1])