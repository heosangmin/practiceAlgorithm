'''
2022/05/22

https://www.acmicpc.net/problem/18428

5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
-> YES
'''
from itertools import combinations

n = int(input())
data = []
spaces = []
for _ in range(n):
    data.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if data[i][j] == 'X':
            spaces.append((i,j))

spaces = list(combinations(spaces, 3))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def I_can_see_you(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < n:
        if data[nx][ny] == 'S':
            return True
        if data[nx][ny] == 'O':
            return False
        return I_can_see_you(nx, ny, d)


def check():
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'T':
                for k in range(4): # 북,동,남,서
                    if I_can_see_you(i,j,k):
                        return False
    return True

result = "NO"
for space in spaces:
    # 장애물 세운다
    data[space[0][0]][space[0][1]] = 'O'
    data[space[1][0]][space[1][1]] = 'O'
    data[space[2][0]][space[2][1]] = 'O'
    
    if check():
        result = "YES"
        break

    # 장애물 허문다
    data[space[0][0]][space[0][1]] = 'X'
    data[space[1][0]][space[1][1]] = 'X'
    data[space[2][0]][space[2][1]] = 'X'

print(result)