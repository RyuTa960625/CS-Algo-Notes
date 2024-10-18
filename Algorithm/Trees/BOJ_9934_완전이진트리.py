n = int(input())

tree = list(map(int, input().split()))
level = [[] for _ in range(n)]

def sol(s, e, depth):
    if s==e:
        level[depth].append(tree[s])
        return
    root = (s+e)//2
    level[depth].append(tree[root])
    sol(s, root-1, depth + 1)
    sol(root+1, e, depth + 1)

sol(0,len(tree)-1,0)

for i in level:
    for j in i:
        print(j, end=" ")
    print()