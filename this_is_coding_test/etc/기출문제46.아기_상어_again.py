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
array = [] # 전체 지도
for _ in range(n):
    array.append(list(map(int, input().split())))

now_x, now_y = 0,0 # 아기 상어 현재 위치
now_size = 2 # 아기 상어 현재 무게

# 아기 상어 초기 위치 찾고 0으로 초기화
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0
            break

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 현재 위치에서 전체 위치까지의 최단 거리 테이블 만들기(bfs)
def bfs():
    # 최단 거리 테이블
    dist = [[-1] * n for _ in range(n)]
    dist[now_x][now_y] = 0
    q = deque([(now_x, now_y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 지나갈 수 있으면
            if 0 <= nx < n and 0 <= ny < n: # 지도 내
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size: # 물고기 없거나 자기 크기 이하
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

# 최단 거리의 물고기 위치를 찾기
def find(dist):
    min_dist = INF
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if 0 < dist[i][j] < min_dist and 0 < array[i][j] < now_size:
                min_dist = dist[i][j]
                x, y = i, j

    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0
while True:
    # 최단 거리의 물고기 위치 찾기
    value = find(bfs())
    
    # 더이상 먹을 것이 없으면 출력후 종료
    if value == None:
        print(result)
        break

    # 해당 위치의 물고기를 지우기, 아기 상어 증량, 전체 시간 증가
    else:
        result += value[2]
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0
        array[value[0]][value[1]] = 0
        now_x, now_y = value[0], value[1]