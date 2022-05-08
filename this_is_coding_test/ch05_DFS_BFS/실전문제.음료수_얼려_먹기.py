'''
2022/05/08

N*M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

input)
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

output)
8
'''

'''
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.
3. 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.
'''

def solution(n,m,matrix):
    graph = []
    for row in matrix.split():
        graph.append(list(map(int, row)))

    # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우에는 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        # 현재 노드를 아직 방문하지 않았다면
        if graph[x][y] == 0:
            # 해당 노드 방문 처리
            graph[x][y] = 1
            # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False

    # 모든 노드(위치)에 대하여 음료수 채우기
    result = 0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 dfs 실행
            if dfs(i,j) == True:
                result += 1
    
    return result

n, m = 4, 5
matrix = "00110\n00011\n11111\n00000"
print(solution(n,m,matrix)) # 3

n, m = 15, 14
matrix = "00000111100000\n11111101111110\n11011101101110\n11011101100000\n11011111111111\n11011111111100\n11000000011111\n01111111111111\n00000000011111\n01111111111000\n00011111111000\n00000001111000\n11111111110011\n11100011111111\n11100011111111"
print(solution(n,m,matrix)) # 8