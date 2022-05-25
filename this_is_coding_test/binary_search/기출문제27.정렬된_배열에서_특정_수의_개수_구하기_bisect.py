'''
2022/05/25

7 2
1 1 2 2 2 2 3
-> 4

7 4
1 1 2 2 2 2 3
-> -1
'''

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_value(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
data = list(map(int, input().split()))

# 값이 [x,x] 범위에 있는 데이터의 개수 계산
count = count_by_value(data, x, x)

if count == 0:
    print(-1)
else:
    print(count)