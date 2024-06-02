N = int(input())

M = 0

while N >= 0 :
    if N % 5 == 0 :
        M += (N // 5)
        print(M)
        break
    N -= 3
    M += 1

else :
    print(-1)