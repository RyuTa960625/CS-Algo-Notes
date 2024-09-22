def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # 중간점

    if array[mid] == target: # target을 찾았으면 리턴
        return mid
    elif array[mid] > target: # target이 중간점보다 작으면 왼쪽부분 탐색
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target: # target이 중간점보다 크면 오른쪽부분 탐색
        return binary_search(array, target, mid+1, end)
    else:
        return None


N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort() # A 정렬

for i in B:
    result = binary_search(A, i, 0, N-1)
    if result == None:
        print(0)
    else:
        print(1)