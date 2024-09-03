from copy import deepcopy
import sys

sys.setrecursionlimit(10**6)

def mark1(i,j):
    l[i][j]=(a1,l[i][j])
    if i!=0 and l[i][j][1]==l[i-1][j]:
        mark1(i-1,j)
    if i!=N-1 and l[i][j][1]==l[i+1][j]:
        mark1(i+1,j)
    if j!=0 and l[i][j][1]==l[i][j-1]:
        mark1(i,j-1)
    if j!=N-1 and l[i][j][1]==l[i][j+1]:
        mark1(i,j+1)

def mark2(i,j):
    l2[i][j]=(a2,l2[i][j])
    if l2[i][j][1] in ['R','G']:
        if i!=0 and l2[i-1][j] in ['R','G']:
            mark2(i-1,j)
        if i!=N-1 and l2[i+1][j] in ['R','G']:
            mark2(i+1,j)
        if j!=0 and l2[i][j-1] in ['R','G']:
            mark2(i,j-1)
        if j!=N-1 and l2[i][j+1] in ['R','G']:
            mark2(i,j+1)
    else:
        if i!=0 and 'B'==l2[i-1][j]:
            mark2(i-1,j)
        if i!=N-1 and 'B'==l2[i+1][j]:
            mark2(i+1,j)
        if j!=0 and 'B'==l2[i][j-1]:
            mark2(i,j-1)
        if j!=N-1 and 'B'==l2[i][j+1]:
            mark2(i,j+1)

N=int(input())
l=[]
for _ in range(N):
    l.append(list(input()))
l2=deepcopy(l)
a1=0
a2=0
for i in range(N):
    for j in range(N):
        if type(l[i][j])==str:
            a1+=1
            mark1(i,j)
for i in range(N):
    for j in range(N):
        if type(l2[i][j])==str:
            a2+=1
            mark2(i,j)
print(a1,a2)
