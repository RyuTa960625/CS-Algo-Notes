arr = input().split('-')
n = 0

for i in arr[0].split('+'):
    n += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        n -= int(j)

print(n)
