'''
2022/05/25

7 2
1 1 2 2 2 2 3
-> 4

7 4
1 1 2 2 2 2 3
-> -1
'''

n, x = map(int, input().split())
data = list(map(int, input().split()))

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = start + (end - start) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# result = []
# while True:
#     idx = binary_search(data, x, 0, len(data)-1)
#     if not idx:
#         break
#     else:
#         result.append(idx)
#         data.remove(x)

# print(len(result) if len(result) > 0 else -1)

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    # 개수를 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = start + (end - start) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid+1, end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = start + (end - start) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return last(array, target, mid+1, end)

count = count_by_value(data, x)

if count == 0:
    print(-1)
else:
    print(count)
