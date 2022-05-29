'''
2022/05/29

당신이 사는 나라에는 N개의 여행지가 있으며, 각 여행지는 1~N번까지의 번호로 구분된다. 또한 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있다. 이때, 여행지가 도로로 연결되어 있다면 양방향으로 이동이 가능하다는 의미이다. 당신은 하나의 여행 계획을 세운 뒤에 이 여행 계획이 가능한지 여부를 판단하고자 한다. 예를 들어 N=5이고, 다음과 같이 도로의 정보가 주어졌다고 가정하자.

- 1번 여행지 - 2번 여행지
- 1번 여행지 - 4번 여행지
- 1번 여행지 - 5번 여행지
- 2번 여행지 - 3번 여행지
- 2번 여행지 - 4번 여행지

만약 당신의 여행 계획이 2번 -> 3번 -> 4번 -> 3번이라고 해보자. 이 경우 2번 -> 3번 -> 2번 -> 4번 -> 2번 -> 3번의 순서로 여행지를 방문하면, 여행 계획을 따를 수 있다.

여행지의 개수와 여행지 간의 연결 정보가 주어졌을 떄, 당신의 여행 계획이 가능한지의 여부를 판별하는 프로그램을 작성하라.

[풀이]
'여행 계획'에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능한 여행 경로이다. 따라서 두 노드 사이에 도로가 존재하는 경우에는 union 연산을 이용해서, 서로 연결된 두 노드를 같은 집합에 속하도록 만든다.

[ex]
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
-> YES
'''

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# n:여행지 수, m:여행 계획에 속한 도시 수
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# 두 여행지가 서로 연결되어 있는지 여부(graph[a][b]==1: a와 b가 연결됨)
# union 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 연결된 경우 union 수행
            union_parent(parent, i+1, j+1)

# 여행 계획
plan = list(map(int, input().split()))

result = True
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")

