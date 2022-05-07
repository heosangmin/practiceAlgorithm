'''
2022/05/07

Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = true;

For
grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
'''

'''
완전 무식하게 풀었다.
다른 사람의 자바 풀이가 재미 있어서 가져와 봤다.
boolean solution(int[][] grid) {
    int[] rowsSumary = new int[9];
    int[] colsSumary = new int[9];
    int[] sectSumary = new int[9];
    for(int row = 0; row < 9; row++){
        for(int col = 0; col < 9; col++){
            rowsSumary[row] += grid[row][col];
            colsSumary[col] += grid[row][col];
            sectSumary[(col / 3) + ((row / 3) * 3)] += grid[row][col];
        }
    }
    return Arrays.stream(grid[0]).distinct().count() == 9 &&  
           Arrays.stream(rowsSumary).allMatch(x -> x == 45) && 
           Arrays.stream(colsSumary).allMatch(x -> x == 45) &&
           Arrays.stream(sectSumary).allMatch(x -> x == 45);
}
'''

def solution(grid):
    for i in range(9):
        if len(set(grid[i])) != 9:
            return False
    
    for i in range(9):
        col = set()
        for j in range(9):
            col.add(grid[j][i])
        if len(col) != 9:
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            temp.append(grid[i][j])
            temp.append(grid[i][j+1])
            temp.append(grid[i][j+2])
            temp.append(grid[i+1][j])
            temp.append(grid[i+1][j+1])
            temp.append(grid[i+1][j+2])
            temp.append(grid[i+2][j])
            temp.append(grid[i+2][j+1])
            temp.append(grid[i+2][j+2])
            print(temp)
            if len(set(temp)) != 9:
                return False

    return True

grid = [[1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4]]
print(solution(grid)) # f

# grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
#         [4, 6, 5, 8, 7, 9, 3, 2, 1],
#         [7, 9, 8, 2, 1, 3, 6, 5, 4],
#         [9, 2, 1, 4, 3, 5, 8, 7, 6],
#         [3, 5, 4, 7, 6, 8, 2, 1, 9],
#         [6, 8, 7, 1, 9, 2, 5, 4, 3],
#         [5, 7, 6, 9, 8, 1, 4, 3, 2],
#         [2, 4, 3, 6, 5, 7, 1, 9, 8],
#         [8, 1, 9, 3, 2, 4, 7, 6, 5]]
# print(solution(grid)) # t

# grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
#         [4, 6, 5, 8, 7, 9, 3, 8, 1],
#         [7, 9, 8, 2, 1, 3, 6, 5, 4],
#         [9, 2, 1, 4, 3, 5, 8, 7, 6],
#         [3, 5, 4, 7, 6, 8, 2, 1, 9],
#         [6, 8, 7, 1, 9, 2, 5, 4, 3],
#         [5, 7, 6, 9, 8, 1, 4, 3, 2],
#         [2, 4, 3, 6, 5, 7, 1, 9, 8],
#         [8, 1, 9, 3, 2, 4, 7, 6, 5]]
# print(solution(grid)) # f

# grid = [[1,2,3,4,5,6,7,8,9], 
#  [1,2,3,4,5,6,7,8,9], 
#  [1,2,3,4,5,6,7,8,9], 
#  [1,2,3,4,5,6,7,8,9], 
#  [1,2,3,4,5,6,7,8,9], 
#  [1,2,3,4,5,6,7,8,9], 
#  [1,2,3,4,5,6,7,8,9], 
#  [1,2,3,4,5,6,7,8,9], 
#  [1,2,3,4,5,6,7,8,9]]
# print(solution(grid)) # f