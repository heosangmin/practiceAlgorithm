'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

For cell = "a1", the output should be
solution(cell) = 2.

For cell = "c2", the output should be
solution(cell) = 6.
'''

def solution(cell):
    result = 0
    c = [ord(cell[0])-96, int(cell[1])]
    m = [[1,2],[2,1],[1,-2],[2,-1],[-1,-2],[-2,-1],[-2,1],[-1,2]]
    for i in m:
        if 0 < c[0] + i[0] < 9 and 0 < c[1] + i[1] < 9:
            result +=1
    return result

print(solution(cell = "a1")) # 2
print(solution(cell = "c2")) # 6

'''
무식하게 모든 케이스를 다 조건문으로 적으려다가 이건 아닌 것 같아서 다른 사람의 풀이를 참고했다.
체스 문제가 가끔 나오는데 위와 같이 말의 갈 수 있는 방향을 더하는 방식으로 확인하는 것이 이해하기 편하다고 느낀다.
'''