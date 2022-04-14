'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
'''

def solution(matrix):
    result = []
    for i in range(0, len(matrix)):
        row = []
        for j in range(0, len(matrix[0])):
            mines = 0
            
            # L,R
            if i == 0:
                mines += matrix[i+1][j]
            elif i == len(matrix) - 1:
                mines += matrix[i-1][j]
            else:
                mines += matrix[i-1][j] + matrix[i+1][j]

            # U,D
            if j == 0:
                mines += matrix[i][j+1]
            elif j == len(matrix[0]) - 1:
                mines += matrix[i][j-1]
            else:
                mines += matrix[i][j-1] + matrix[i][j+1]
            
            # etc
            if i != 0 and j != 0:
                mines += matrix[i-1][j-1]
            if i != len(matrix) - 1 and j != 0:
                mines += matrix[i+1][j-1]
            if i != 0 and j != len(matrix[0]) - 1:
                mines += matrix[i-1][j+1]
            if i != len(matrix) - 1 and j != len(matrix[0]) - 1:
                mines += matrix[i+1][j+1]

            row.append(mines)

        result.append(row)
    return result


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
print(solution(matrix))