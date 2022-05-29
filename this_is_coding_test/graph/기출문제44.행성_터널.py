'''
2022/05/29

https://www.acmicpc.net/problem/2887

5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
-> 4
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

n = int(input()) # 1 <= N <= 100,000
edges = []

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

# planets = []
# for _ in range(n):
#     x, y, z = map(int, input().split())
#     planets.append({
#         "x": x, "y": y, "z": z
#     })

# for i in range(n):
#     for j in range(n):
#         if i != j:
#             edges.append((min(\
#                 abs(planets[i]["x"] - planets[j]["x"]),\
#                 abs(planets[i]["y"] - planets[j]["y"]),\
#                 abs(planets[i]["z"] - planets[j]["z"])),\
#                     i,j))

# edges.sort()

# result = 0
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost

# print(result)

# 위 방법이라면 메모리 초과임

# 모든 노드에 대한 좌표 값 입력받기
x = []
y = []
z = []
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)