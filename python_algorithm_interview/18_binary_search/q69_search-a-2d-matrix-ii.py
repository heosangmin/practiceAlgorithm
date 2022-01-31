'''
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
'''
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        효율적인 알고리즘을 요구하고 있다. 책에 있는 풀이대로 해보자.
        타겟을 탐색하되 행의 마지막 요소애서 시작한다.
        인덱스의 값이 타겟보다 작다면 다음 열로 이동한다.
        인덱스의 값이 타겟보다 크다면 행의 왼쪽으로 이동해 비교한다.
        '''
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False

    def searchMatrix_pythonic(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

s = Solution()

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
#print(matrix, target, s.searchMatrix(matrix, target))
print(matrix, target, s.searchMatrix_pythonic(matrix, target))


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
#print(matrix, target, s.searchMatrix(matrix, target))
print(matrix, target, s.searchMatrix_pythonic(matrix, target))