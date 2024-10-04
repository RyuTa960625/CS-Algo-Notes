import sys
sys.setrecursionlimit(10 ** 6)

def pre_order(istart, iend, pstart, pend):
    if istart > iend or pstart > pend:
        return

    root = postorder[pend]
    print(root, end=' ')

    pre_order(istart, pos[root] - 1, pstart, pstart + pos[root] - istart - 1)
    pre_order(pos[root] + 1, iend, pstart + pos[root] - istart, pend - 1)



n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i

pre_order(0, n - 1, 0, n - 1)