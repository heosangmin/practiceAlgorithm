def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # start + (end - start) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search_recursive(array, target, mid+1, end)

def binary_search_iterative(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 # start + (end - start) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

n = 10
target = 7
array = [1,3,5,7,9,11,13,15,17,19]

print("recursive: ", binary_search_recursive(array, target, 0, n-1))
print("iterative: ", binary_search_iterative(array, target, 0, n-1))
