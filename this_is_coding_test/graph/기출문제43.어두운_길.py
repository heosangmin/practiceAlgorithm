'''
2022/05/29

한 마을은 N개의 집과 M개의 도로로 구성되어 있다. 각 집은 0번부터 N-1번까지의 번호로 구분된다. 모든 도로에는 가로등이 구비되어 있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일하다. 예를 들어 2번 집과 3번 집 사이를 연결하는 길이가 7인 도로가 있다고 해보자. 하루 동안 이 가로등을 켜기 위한 비용은 7이 된다.

정부에서는 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 한다. 결과적으로 일부 가로등을 비활성화하여 최대한 많은 금액을 절약하고자 한다. 마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하라.

[ex]
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
-> 51
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n: 집의 수, 1 <= N <= 200,000
# m: 도로의 수, N-1 <= M <= 200,000
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


edges = [] # 모든 간성 정보를 담을 리스트
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
edges.sort() # 비용순으로 정렬

total_cost = 0
added_cost = 0
for edge in edges:
    cost, a, b = edge
    total_cost += cost
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        added_cost += cost

print(total_cost - added_cost)
