'''
2022/05/20

https://www.acmicpc.net/problem/14502

input1)
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

output1)
27

input2)
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

output2)
9

input3)
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

output3)
3
'''

'''
이 문제는 벽을 3개 설치하는 모든 경우의 수를 다 계산해야 한다. 전체 맵의 크기가 8*8이므로, 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우(바이러스가 하나도 존조해지 않는 경우) 64C3이 될 것이다. 이는 100,000보다도 작은 수이므로, 모든 경우의 수를 고려해도 시간 안에 문제를 해결할 수 있다는 것을 알 수 있다.

또한 모든 조합을 계산할 때는 파이썬의 조합 라이브러리를 이용하거나, DFS 혹은 BFS를 이용하여 해결할 수 있다. 따라서 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에 그러한 조합에 대해서 안전 영역의 크기를 계산하면 된다. 안전 영역의 크기를 구하는 것 또한 DFS나 BFS를 이용하여 계산할 수 있다.

결과적으로 여기서는 가능한 모든 경우의 수를 계산하되, 안전 영역을 계산할 때 DFS나 BFS를 적절히 이용해야 한다는 점이 특징이다. 따라서 DFS 혹은 BFS를 실수 없이 구현해야 정답 판정을 받을 수 있다. 이 문제는 DFS 혹은 BFS를 사용하여 완전 탐색을 수행해야 한다는 점에서 DFS/BFS 문제 혹은 완전 탐색 문제로 분류할 수 있다. 또한 구현 과정이 까다롭기 때문에 구현 유형으루 분류할 수도 있다.

문제 풀이 아이디어를 간랸히 설명하면, 초기에 비어 있는 모든 공간 중에서 3개를 골라 벽을 설치하는 것이다. 매번 벽을 설치할 때마다, 각 바이러스가 사방으로 퍼지는 것을 DFS/BFS로 계산하여 안전영역을 구해야 한다.
'''

from itertools import combinations

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

empty_list = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            empty_list.append((i,j))

empty_list = list(combinations(empty_list, 3))

# 4가지 이동 방향(위,오른쪽,아래,왼쪽)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

# DFS로 바이러스를 퍼지도록 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 실행
                temp[nx][ny] = 2
                virus(nx,ny)

# 현재 맵에서 안전 영역의 크기를 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS로 울타리를 설치하면서, 매번 안전 영역의 크기를 계산
# def dfs(count):
#     global result
#     # 울타리가 3개 설치된 경우
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]
#         # 각 바이러스의 위치에서 전파
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i,j)
#         # 안전 영역 최댓값 계산
#         result = max(result, get_score())
#         return

#     # 빈공간에 울타리 설치
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1

def check():
    global result
    for c in empty_list:
        # 벽 세우기
        data[c[0][0]][c[0][1]] = 1
        data[c[1][0]][c[1][1]] = 1
        data[c[2][0]][c[2][1]] = 1
        # 체크용 맵 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if data[i][j] == 2:
                    virus(i,j)
        # 안전영역 개수 확인
        result = max(result, get_score())
        # 벽 허물기
        data[c[0][0]][c[0][1]] = 0
        data[c[1][0]][c[1][1]] = 0
        data[c[2][0]][c[2][1]] = 0


# dfs(0)
check()
print(result)
