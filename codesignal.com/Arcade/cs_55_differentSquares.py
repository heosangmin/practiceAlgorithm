'''
2022/05/06

Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.
'''

def solution(matrix):
    if len(matrix) < 2 or len(matrix[0]) < 2:
        return 0
    s = set()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            # s.add(str(matrix[i][j]) + str(matrix[i][j+1]) + str(matrix[i+1][j]) + str(matrix[i+1][j+1]))
            # 튜플로 만들어서 넣어도 됐다.
            s.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))

    return len(s)

'''
무식하게 한 칸씩 이동하면서 확인하는 수밖에 없지 않을까?
'''

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]] # 6
print(solution(matrix)) # 6

matrix = [[9,9,9,9,9], 
 [9,9,9,9,9], 
 [9,9,9,9,9], 
 [9,9,9,9,9], 
 [9,9,9,9,9], 
 [9,9,9,9,9]]
print(solution(matrix)) # 1

matrix = [[3]]
print(solution(matrix)) # 0

matrix = [[3,4,5,6,7,8,9]]
print(solution(matrix)) # 0

matrix = [[3], 
 [4], 
 [5], 
 [6], 
 [7]]
print(solution(matrix)) # 0

matrix = [[2,5,3,4,3,1,3,2], 
 [4,5,4,1,2,4,1,3], 
 [1,1,2,1,4,1,1,5], 
 [1,3,4,2,3,4,2,4], 
 [1,5,5,2,1,3,1,1], 
 [1,2,3,3,5,1,2,4], 
 [3,1,4,4,4,1,5,5], 
 [5,1,3,3,1,5,3,5], 
 [5,4,4,3,5,4,4,4]]
print(solution(matrix)) # 54

matrix = [[1,1,1,1,1,1,2,2,2,3,3,3,9,9,9,2,3,9]]
print(solution(matrix)) # 0