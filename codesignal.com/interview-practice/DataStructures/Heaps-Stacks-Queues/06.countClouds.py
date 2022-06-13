'''
2022/06/13

https://app.codesignal.com/interview-practice/task/HdgqPhHqs3NciAHqH

Given a 2D grid skyMap composed of '1's (clouds) and '0's (clear sky), count the number of clouds. A cloud is surrounded by clear sky, and is formed by connecting adjacent clouds horizontally or vertically. You can assume that all four edges of the skyMap are surrounded by clear sky.

Example

For

skyMap = [['0', '1', '1', '0', '1'],
          ['0', '1', '1', '1', '1'],
          ['0', '0', '0', '0', '1'],
          ['1', '0', '0', '1', '1']]
the output should be
solution(skyMap) = 2;

For

skyMap = [['0', '1', '0', '0', '1'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '1'],
          ['0', '0', '1', '1', '0'],
          ['1', '0', '1', '1', '0']]
the output should be
solution(skyMap) = 5.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char skyMap

A 2D grid that represents a map of the sky, as described above.

Guaranteed constraints:
0 ≤ skyMap.length ≤ 300,
0 ≤ skyMap[i].length ≤ 300.

[output] integer

The number of clouds in the given skyMap, as described above.
'''

# 그래프 문제들에서 볼 수 있는 전형적인 타입이다.
# 여기는 힙, 스택, 큐의 카테고리인데 dfs, bfs를 사용한다면 큐 문제라고 볼 수 있겠다.
from collections import deque
def solution(skyMap):
    if len(skyMap) == 0:
        return 0
    n = len(skyMap)
    m = len(skyMap[0])
    visited = [[False] * m for _ in range(n)]
    def bfs(i, j):
        q = deque([(i,j)])
        visited[i][j] = True

        while q:
            x, y = q.popleft()
            for i, j in (-1,0), (0,1), (1, 0), (0, -1):
                nx = x + i
                ny = y + j
                if 0 <= nx < n and 0 <= ny < m:
                    if skyMap[nx][ny] == '1' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
    result = 0
    for i in range(n):
        for j in range(m):
            if skyMap[i][j] == '1' and not visited[i][j]:
                result += 1
                bfs(i,j)

    return result
    

skyMap = [['0', '1', '1', '0', '1'],
          ['0', '1', '1', '1', '1'],
          ['0', '0', '0', '0', '1'],
          ['1', '0', '0', '1', '1']]
print(solution(skyMap)) # 2

skyMap = [['0', '1', '0', '0', '1'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '1'],
          ['0', '0', '1', '1', '0'],
          ['1', '0', '1', '1', '0']]
print(solution(skyMap)) # 5