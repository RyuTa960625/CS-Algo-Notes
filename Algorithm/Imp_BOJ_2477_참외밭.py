K = int(input())
widths = [input().split() for _ in range(6)]
direction = []
length = []
for i in widths:
    direction.append(int(i[0]))
for i in widths:
    length.append(int(i[1]))
max_boxes = []
min_boxes = []

for i in range(1,5):
    if direction.count(i) == 1:
        max_boxes.append(length[direction.index(i)])
        tmp = direction.index(i) + 3
        if tmp >= 6:
            tmp -= 6
        min_boxes.append(length[tmp])

wid = max_boxes[0] * max_boxes[1] - min_boxes[0] * min_boxes[1]
print(wid * K)