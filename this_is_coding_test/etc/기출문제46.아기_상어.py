'''
2022/05/30

https://www.acmicpc.net/problem/16236

3
0 0 0
0 0 0
0 9 0
-> 0

3
0 0 1
0 0 0
0 9 0
-> 3

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
-> 14

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
-> 60

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
-> 48

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9
-> 39
'''

from collections import deque

INF = 1e9
n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 아기 상어의 현재 크기, 현재 위치
now_size = 2
now_x, now_y = 0, 0

# 아기 상어의 위치를 찾고 그 위치에 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 최단 거리를 계산하는 BFS
def bfs():
    # dist : 현재 위치에서 각 위치까지의 최단 거리를 저장함
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 0 < array[i][j] < now_size:
                # 가장 가까운 물고기 한 마리 선택
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x, y = i, j
    
    if min_dist == INF: # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x, y, min_dist # 먹을 물고기의 위치와 최단 거리

result = 0 # 최종 답
ate = 0 # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우 결과 출력, 종료
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 아무 것도 없도록 처리
        array[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0


