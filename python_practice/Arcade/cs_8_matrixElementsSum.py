def solution(matrix):
    isHaunted = [False] * len(matrix[0])
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not isHaunted[col]:
                if matrix[row][col] > 0:
                    result += matrix[row][col]
                else:
                    isHaunted[col] = True

    return result

matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]

print(solution(matrix))