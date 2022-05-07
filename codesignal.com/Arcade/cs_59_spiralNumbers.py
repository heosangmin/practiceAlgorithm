'''
2022/05/07

Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

solution(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
'''

def solution(n):
    # m = [[0] * n] * n # 특정 크기의 2차원 배열을 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야 한다.
    m = [[0] * n for _ in range(n)]
    shift = [(0,1), (1,0), (0,-1), (-1,0)]
    d, x, y = 0, 0, 0
    nextX, nextY = 0, 0

    for i in range(n*n):
        m[x][y] = i+1
        nextX, nextY = x + shift[d][0], y + shift[d][1]

        if nextX < 0 or nextX >= n or nextY < 0 or nextY >= n or m[nextX][nextY] != 0:
            d = (d + 1) % 4 # 방향 바꾸기
            nextX = x + shift[d][0]
            nextY = y + shift[d][1]

        x, y = nextX, nextY

    return m

print(solution(n=3))