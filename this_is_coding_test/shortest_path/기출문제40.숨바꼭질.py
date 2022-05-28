'''
2022/05/28

당신은 술래를 피해 1~N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발한다. 전체 맵에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결한다. 또한 전체맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어진다.

당신은 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있다. 이때 최단 거리의 의미는 지나야 하는 길의 최소 개수를 의미한다. 당신이 숨을 헛간의 번호를 출력하는 프로그램을 작성하라.

6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
-> 4 2 3 (숨어야 하는 헛간 번호, 그 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간 수)

'''

import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = [(0, 1)]
distance[1] = 0

while q:
    dist, now = heapq.heappop(q) # 현재 노드, 노드까지 오기까지 걸린 거리
    if distance[now] < dist: # 이미 처리된 적 있다면 생략
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

max_val = -1e9
for i in range(1, n+1):
    if distance[i] < 1e9:
        max_val = max(max_val, distance[i])

print(distance.index(max_val), max_val, distance.count(max_val))
