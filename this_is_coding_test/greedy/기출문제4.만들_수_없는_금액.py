'''
2022/05/15

만들 수 없는 금액

N개의 동전을 가지고 있다. 이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하라.

cond)
- 1 <= N <= 1,000
- 각 화폐는 1,000,000 이하의 자연수

input)
5
3 2 1 1 9

output)
8

풀이를 여러 번 읽어봐야 할듯.
'''

n = int(input())
data = map(int, input().split())
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)