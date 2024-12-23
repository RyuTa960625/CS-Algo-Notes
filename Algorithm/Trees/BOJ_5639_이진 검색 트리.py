import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

node = []
while True:
    try:
        node.append(int(input()))
    except:
        break

def post_order(root_idx, last_idx):
    if root_idx > last_idx:
        return

    root = node[root_idx]
    right_start_idx = root_idx + 1

    while right_start_idx <= last_idx:
        if node[right_start_idx] > root:
            break
        right_start_idx += 1

    post_order(root_idx + 1, right_start_idx - 1)
    post_order(right_start_idx, last_idx)

    print(root)

post_order(0, len(node) - 1)