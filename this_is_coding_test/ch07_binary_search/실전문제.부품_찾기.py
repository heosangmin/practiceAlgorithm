'''
2022/05/10

매장에 부품이 N개 있다. 손님이 M개 종류의 부품을 구매하려 한다. 이때 매장에 부품이 모두 있는지 확인하는 프로그램을 작성하라.

1 <= N <= 1,000,000
1 <= M <= 1,000,000

input)
5
8 3 7 9 2
3
5 7 9

output)
no yes yes
'''

# 1. 이진 탐색으로 풀기
def binary_search(array, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 2. 계수 정렬로 풀기
n = int(input())
array = [0] * 1000001

# 전체 부품 번호를 기록
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 3. set으로 풀기
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

