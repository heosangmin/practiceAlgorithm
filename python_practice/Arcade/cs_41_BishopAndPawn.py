'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false.
'''

def solution(bishop, pawn):
    return abs(ord(bishop[0])-ord(pawn[0])) == abs(int(bishop[1])-int(pawn[1]))

    # col_bishop = ord(bishop[0]) - ord('a')
    # row_bishop = int(bishop[1]) - 1
    # col_pawn = ord(pawn[0]) - ord('a')
    # row_pawn = int(pawn[1]) - 1

    # if row_bishop == row_pawn or col_bishop == col_pawn:
    #     return False
    
    # col_bishop = ord(bishop[0]) - ord('a')
    # row_bishop = int(bishop[1]) - 1
    # while(row_bishop >= 0 and col_bishop >= 0):
    #     if row_bishop == row_pawn and col_bishop == col_pawn:
    #         return True
    #     row_bishop -= 1
    #     col_bishop -= 1
    
    # col_bishop = ord(bishop[0]) - ord('a')
    # row_bishop = int(bishop[1]) - 1
    # while(row_bishop < 8 and col_bishop < 8):
    #     if row_bishop == row_pawn and col_bishop == col_pawn:
    #         return True
    #     row_bishop += 1
    #     col_bishop += 1

    # col_bishop = ord(bishop[0]) - ord('a')
    # row_bishop = int(bishop[1]) - 1
    # while(row_bishop < 8 and col_bishop >= 0):
    #     if row_bishop == row_pawn and col_bishop == col_pawn:
    #         return True
    #     row_bishop += 1
    #     col_bishop -= 1

    # col_bishop = ord(bishop[0]) - ord('a')
    # row_bishop = int(bishop[1]) - 1
    # while(row_bishop >= 0 and col_bishop < 8):
    #     if row_bishop == row_pawn and col_bishop == col_pawn:
    #         return True
    #     row_bishop -= 1
    #     col_bishop += 1

    # return False

'''
이럴줄 알았다.
분명 한두 줄로 풀릴 문젠데 생각이 게을러서 무식하게 풀고 말았다.
비숍과 폰 사이의 기울기?를 확인하면 되는 문제다.
즉, 두 말의 x축 차이와 y축 차이가 같으면 되는 것.
'''

print(solution(bishop = "a1", pawn = "c3"))
print(solution(bishop = "h1", pawn = "h3"))
print(solution(bishop = "e7", pawn = "a3"))