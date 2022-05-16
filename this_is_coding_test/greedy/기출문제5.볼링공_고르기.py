'''
2022/05/16

볼링공 고르기

A와 B가 볼링을 치고 있다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 한다. 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여된다. 또한 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주한다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재한다.

N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하라.

input cond)
- 첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어짐 (1 <= N <= 1,000, 1 <= M <= 10)
- 둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어짐

input)
5 3
1 3 2 3 2

output)
8

input)
8 5
1 5 4 3 2 4 5 2

output)
25
'''

# itertools.combinations 써도 되겠지만.
# 아래 방법이라면 시간 복잡도에서 걸릴지도.
n, m = map(int, input().split())
balls = list(map(int, input().split()))
result = 0

for a in range(n-1):
    for b in range(a+1,n):
        if balls[a] != balls[b]:
            result += 1

print(result)

# 책 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)