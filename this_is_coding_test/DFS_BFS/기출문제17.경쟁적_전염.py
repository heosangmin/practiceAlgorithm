'''
2022/05/21

https://www.acmicpc.net/problem/18405

'''
from collections import deque

n, k = map(int, input().split())
data = []
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0: # i,j에 바이러스가 존재하면
            data.append((graph[i][j], 0, i, j)) # (바이러스 종류, 시간, x, y)

target_s, target_x, target_y = map(int, input().split())

data.sort()
q = deque(data)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs
while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx < n and 0 <= ny < n:
            # 아직 방문하지 않았다면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])