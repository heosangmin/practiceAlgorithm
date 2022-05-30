'''
2022/05/30


https://www.acmicpc.net/problem/19236

7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
->33

16 7 1 4 4 3 12 8
14 7 7 6 3 4 10 2
5 2 15 2 8 3 6 4
11 8 2 4 13 5 9 4
->43

12 6 14 5 4 5 6 7
15 1 11 7 3 7 7 5
10 3 8 3 16 6 1 1
5 8 2 7 13 6 9 2
->76

2 6 10 8 6 7 9 4
1 7 16 6 4 2 5 8
3 7 8 6 7 6 14 8
12 7 15 4 11 3 13 3
->39
'''
import copy

array = [[] for _ in range(4)]
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0, 8, 2):
        array[i].append([row[j],row[j+1]-1])

result = 0

# 8가지 방향 정의(위, 왼쪽 위, 왼쪽, 왼쪽 아래, 아래, 오른쪽 아래, 오른쪽, 오른쪽 위)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


# 반시계 방향 45도 회전
def turn_left(d):
    return (d+1) % 8

# 현재 배열에서 특정한 번호의 물고기 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None

# 모든 물고기를 회전 및 이동
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 확인(낮은 번호부터)
    for i in range(1,17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1] # 물고기가 향하고 있는 방향
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동 가능하다면 이동시키기
                if 0 <= nx < 4 and 0 <= ny < 4: # 지도 내에
                    if not (nx == now_x and ny == now_y): # 상어 없다면
                        array[x][y][1] = direction # 향하고 있는 방향으로 갱신하고
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y] # 바꾸기
                        break
                direction = turn_left(direction)

# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재 방향으로 계속 이동시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            # 물고기가 존재한다면
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

# 모든 경우를 탐색하기 위한 DFS
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array) # 리스트를 통째로 복사

    # 1. 현재 위치의 물고기 먹기
    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1 # 물고기를 먹었으므로 번호를 -1로 변경

    # 2. 물고기들 이동
    move_all_fishes(array, now_x, now_y)

    # 3. 상어가 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 곳이 없다면 종료
    if len(positions) == 0:
        result = max(result, total) # 최댓값 저장
        return
    # 모든 이동 가능한 위치로 재귀 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)

