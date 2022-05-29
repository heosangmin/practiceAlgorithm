'''
2022/05/29

공항에는 G개의 탑승구가 있으며, 각각의 탑승구는 1번부터 G번까지의 번호로 구분된다.

공항에는 P개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1번부터 $g_i$번째$(a <= g_i <= G)$ 탑승구 중 하나에 영구적으로 도킹해야 한다. 이때 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있다.

또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떠한 탑승구도 도킹할 수 없는 비행기가 나오는 경우, 그 시점에서 공항의 운행을 중지한다. 공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 한다. 비행기를 최대 몇 대 도킹할 수 있는지를 출력하는 프로그램을 작성하라.

[ex1]
4
3
4
1
1
-> 2

[ex2]
4
6
2
2
3
3
4
4
-> 3
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


g = int(input()) # 탑승구의 수
p = int(input()) # 비행기의 수

parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i

result = 0
for _ in range(p):
    plane = int(input()) # 도착한 비행기
    if find_parent(parent, plane) == 0: # 도킹할 수 없을 경우
        break
    union_parent(parent, parent[plane], parent[plane]-1)
    result += 1


print(result)