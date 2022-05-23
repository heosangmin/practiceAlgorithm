'''
2022/05/23

https://www.acmicpc.net/problem/16234

2 20 50
50 30
20 40
-> 1

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
-> 3
'''
from collections import deque
n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

day = 0
while True:
    union = []
    visited = [[False] * n for _ in range(n)]

    # 연합을 만듦
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                tmp_union = [(i,j)]

                # bfs
                q = deque([(i,j)])
                visited[i][j] = True

                while q:
                    v = q.popleft()
                    for d in range(4):
                        nx = v[0] + dx[d]
                        ny = v[1] + dy[d]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if l <= abs(data[v[0]][v[1]] - data[nx][ny]) <= r:
                                visited[nx][ny] = True
                                tmp_union.append((nx,ny))
                                q.append((nx,ny))

                if len(tmp_union) > 1:
                    union.append(tmp_union)
    
    if len(union) > 0:
        day += 1
        # 인구 이동
        for u in union:
            sum_of_union = 0
            for c in u:
                sum_of_union += data[c[0]][c[1]]
            for c in u:
                data[c[0]][c[1]] = int(sum_of_union / len(u))
    else:
        break

# print("last union:",union)
# print("last data:",data)
print(day)
