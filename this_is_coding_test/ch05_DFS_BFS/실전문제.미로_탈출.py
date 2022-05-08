'''
2022/05/08

당신은 N*M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 괴물이 있어 이를 피해 탈출해야 한다. 당신의 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

input)
5 6
101010
111111
000001
111111
111111

output)
10
'''

'''
이 문제는 BFS를 이용했을 떄 매우 효과적을오 해결할 수 있다. BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문이다. 그러므로 (1,1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다. 특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.
'''
from collections import deque
def solution(n,m,matrix):
    graph = []
    for row in matrix.split():
        graph.append(list(map(int, row)))
    
    # 이동할 네 방향 정의(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS 구현
    def bfs(x, y):
        # 큐(deque) 라이브러리 사용
        queue = deque()
        queue.append((x,y))

        # 큐가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()

            # 현재 위치에서 네 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 공간을 벗어난 경우 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                # 괴물인 경우 무시
                if graph[nx][ny] == 0:
                    continue

                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
        
        # 가장 오른쪽 아래까지의 최단 거리 반환
        return graph[n-1][m-1]

    return bfs(0,0)


n, m = 5 ,6
matrix = "101010\n111111\n000001\n111111\n111111"
print(solution(n, m, matrix))