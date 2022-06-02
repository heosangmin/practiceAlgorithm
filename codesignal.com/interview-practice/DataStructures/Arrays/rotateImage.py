'''
2022/06/02

https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB/description

Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

[Example]

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

solution(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

[Input/Output]

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer
'''
from copy import deepcopy
# 우선은 무식하게 하나씩 옮기기
def solution_my(matrix):
    matrix_size = len(matrix)
    new_matrix = deepcopy(matrix)
    for i in range(0, int(matrix_size / 2)):
        for j in range(i, matrix_size - 1):
            temp1 = matrix[i][j]
            temp2 = matrix[j][matrix_size - 1 - i]
            temp3 = matrix[matrix_size - 1 - i][matrix_size - 1 - j]
            temp4 = matrix[matrix_size - 1 - j][i]
            new_matrix[i][j] = temp4
            new_matrix[j][matrix_size - 1 - i] = temp1
            new_matrix[matrix_size - 1 - i][matrix_size - 1 - j] = temp2
            new_matrix[matrix_size - 1 - j][i] = temp3

    for i in range(matrix_size):
        print(new_matrix[i])
    return matrix

# 다른 사람 풀이
def solution_others(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    return a

# 또는
def solution_others_again(a):
    return list(zip(*reversed(a)))

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# print(solution_others(a))
print(solution_others_again(a))

a = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9,  10, 11, 12],
     [13, 14, 15, 16]]
# print(solution_others(a))
print(solution_others_again(a))

a = [[ 1,  2,  3,  4,  5],
     [ 6,  7,  8,  9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]]
# print(solution_others(a))
print(solution_others_again(a))