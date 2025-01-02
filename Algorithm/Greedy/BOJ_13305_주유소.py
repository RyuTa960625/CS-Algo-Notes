n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

result = 0
minP = p[0]

for i in range(n-1):
    if p[i] < minP:
        minP = p[i]
    result += minP * d[i]

print(result)