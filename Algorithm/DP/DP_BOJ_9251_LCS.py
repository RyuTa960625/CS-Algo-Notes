s1=input()
s2=input()

dp=[[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for row in range(1, len(s1)+1):
  for col in range(1, len(s2)+1):
    if s1[row-1] == s2[col-1]:
      dp[row][col] = dp[row-1][col-1]+1
    else:
      dp[row][col] = max(dp[row-1][col],dp[row][col-1])

print(dp[-1][-1])