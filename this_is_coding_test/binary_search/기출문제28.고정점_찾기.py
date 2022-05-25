'''
2022/05/25

고정점Fixed Point이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다. 예를 들어 수열 a = {-15,-4,2,8,13}이 있을 때 a[2] = 2이므로, 고정점은 2가 된다.

하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있다. 이때 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하라. 고정점은 최대 1개만 존재한다. 만약 고정점이 없다면 -1을 출력한다.

단, 이 문제는 시간 복잡도 O(log N)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다.

5
-15 -6 1 3 7
-> 3

7
-15 -4 2 8 9 13 15
-> 2

7
-15 -4 3 8 9 13 15
-> -1
'''

n = int(input())
array = list(map(int, input().split()))

start, end = 0, n-1

while start <= end:
    mid = start + (end - start) // 2
    if array[mid] == mid:
        result = mid
        break
    elif array[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1
else:
    result = -1

print(result)
