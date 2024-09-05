N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

prefix_sum_matrix = [[0 for _ in range(N)] for _ in range(N)]

prefix_sum_matrix[0][0] = matrix[0][0]
for j in range(1,N):
    prefix_sum_matrix[0][j] = prefix_sum_matrix[0][j-1] + matrix[0][j]
for j in range(1,N):
    prefix_sum_matrix[j][0] = prefix_sum_matrix[j-1][0] + matrix[j][0]
for i in range(1,N):
    for j in range(1,N):
        prefix_sum_matrix[i][j] = prefix_sum_matrix[i][j-1] + prefix_sum_matrix[i-1][j] - prefix_sum_matrix[i-1][j-1] + matrix[i][j]

for i in range(N):
    prefix_sum_matrix[i] = [0] + prefix_sum_matrix[i]
zero_padding = [[0 for _ in range(N+1)]]
prefix_sum_matrix = zero_padding + prefix_sum_matrix

for k in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum_matrix[x2][y2] - prefix_sum_matrix[x2][y1-1] - prefix_sum_matrix[x1-1][y2] + prefix_sum_matrix[x1-1][y1-1])