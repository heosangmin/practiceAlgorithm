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
        array[i].append([row[j],row[j+1]-1]) # 방향 값은 0부터 시작하도록 함

# 최종 결과
result = 0

# 8가지 방향 정의(위, 왼쪽 위, 왼쪽, 왼쪽 아래, 아래, 오른쪽 아래, 오른쪽, 오른쪽 위)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 왼쪽으로 45도 회전
def turn_left(direction):
    return (direction + 1) % 8

# 특정 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None

# 모든 물고기들 이동시키기
def move_all_fishes(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4: # 이동 범위 내
                    if not (nx == now_x and ny == now_y): # 상어 없다면
                        array[x][y][1] = direction # 이동할 방향을 설정하고
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y] # 교체
                        break
                direction = turn_left(direction) # 왼쪽으로 45도 회전


# 상어가 갈 수 있는 위치를 탐색하기
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for _ in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x < 4 and 0 <= now_y < 4 and array[now_x][now_y][0] != -1:
            positions.append((now_x, now_y))
    return positions

# 완전 탐색을 위한 dfs
def dfs(array, now_x, now_y, total): # total: 현 위치에서의 물고기 번호 합계
    global result
    array = copy.deepcopy(array) # 탐색 간에 지도에 영향이 있어서는 안 되므로
    
    # 현재 위치의 물고기 먹기
    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    # 물고기들 이동시키기
    move_all_fishes(array, now_x, now_y)

    # 상어가 갈 수 있는 곳을 탐색하기
    positions = get_possible_positions(array, now_x, now_y)

    # 갈 수 있는 곳이 없다면 종료
    if len(positions) == 0:
        result = max(result, total)
        return
    # 갈 수 있는 모든 곳을 dfs 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)