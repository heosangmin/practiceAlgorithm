'''
프렌즈4블록

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ

입력 형식
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.

출력 형식
입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.
'''
def solution(m, n, board):
    '''
    역시 나에겐 문제를 어렵게 생각하는 경향이 있다. 혹은 그냥 똑똑하지 못한 걸지도.
    - 삭제될 블록은 다른 문자로 채워 놓고 나중에 그 문자 개수만 반환하면 된다.
    - 삭제된 공간에 블록이 떨어져도 총 삭제 개수는 변하지 않는다.
    '''
    answer = 0
    spined = []
    marked = []
    loop = True

    # -90 degrees
    for j in range(0, n):
        spined.append([])
        marked.append([])
        for i in range(m - 1,  -1, -1):
            spined[j].append(board[i][j])
            marked[j].append(board[i][j])

    while loop:
        loop = False
        
        for i in range(len(spined) - 1):
            for j in range(len(spined[i]) - 1):
                cur = spined[i][j]
                right = spined[i][j + 1]
                bottom = spined[i + 1][j] if j < len(spined[i + 1]) else None
                diagonal = spined[i + 1][j + 1] if j + 1 < len(spined[i + 1]) else None

                if cur == right and cur == bottom and cur == diagonal:
                    marked[i][j] = "1"
                    marked[i][j + 1] = "1"
                    marked[i + 1][j] = "1"
                    marked[i + 1][j + 1] = "1"
                    loop = True

        for row in marked:
            while "1" in row:
                row.remove("1")
                answer += 1
        
        del(spined)
        spined = marked.copy()

    return answer

def solution_book(m, n, board):
    board = list(list(x) for x in board)

    matched = True
    while matched:
        matched = []

        # 1. 일치 여부를 판별한다.
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] ==\
                    board[i + 1][j] == \
                    board[i + 1][j + 1] != "#":
                    matched.append([i, j])
        
        # 2. 삭제한다.
        for i, j in matched:
            board[i][j] = board[i][j + 1] = board[i + 1][j] = board[i + 1][j + 1] = "#"
        
        # 3. 블록을 떨어뜨린다.
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == "#":
                        board[i + 1][j] = board[i][j]
                        board[i][j] = "#"
    
    return sum(x.count("#") for x in board)

m = 4
n = 5
board =  ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# 14
# print(solution(m, n, board))
print(solution_book(m, n, board))

m = 6
n = 6
board =  ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# 15
# print(solution(m, n, board))
print(solution_book(m, n, board))
