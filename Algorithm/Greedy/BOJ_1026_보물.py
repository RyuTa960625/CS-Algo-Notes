N = int(input())

Alist = list(map(int, input().split()))
Blist = list(map(int, input().split()))

sum = 0

for _ in range(len(Alist)):
    sum += min(Alist)*max(Blist)
    Alist.remove(min(Alist))
    Blist.remove(max(Blist))

print(sum)