'''
2022/05/25

https://www.acmicpc.net/problem/2110

무슨 말인지 잘 모르겠다.

5 3
1
2
8
4
9
-> 3
'''

n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = array[1] - array[0] # 집의 좌표 중에 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중에 가장 큰 값
result = 0

while (start <= end):
    mid = start + (end - start) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = array[0]
    count = 1
    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1,n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid
    else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)

