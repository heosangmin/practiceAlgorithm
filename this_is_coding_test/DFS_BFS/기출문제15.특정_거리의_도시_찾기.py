'''
2022/05/20

https://www.acmicpc.net/problem/18352

input1)
4 4 2 1
1 2
1 3
2 3
2 4

output1)
4

input2)
4 3 2 1
1 2
1 3
1 4

output2)
-1

input3)
4 4 1 1
1 2
1 3
2 3
2 4

output3)
2
3

'''
# 모든 간선의 거리가 1이라면 너비 우선 탐색만으로 해결할 수 있다.

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0

for _ in range(m):
    f, t = map(int, input().split())
    graph[f].append(t)

# bfs
q = deque()
q.append(x)
while q:
    now = q.popleft()
    for next_node in graph[now]: # 현재 도시(now)에서 갈 수 있는 도시들
        if distance[next_node] == -1: # 아직 방문하지 않았다면
            distance[next_node] = distance[now] + 1 # 최단거리 갱신
            q.append(next_node)

if k not in distance:
    print(-1)
else:
    for i in range(1,n+1):
        if distance[i] == k:
            print(i)
