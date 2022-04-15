'''
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.

For cell1 = "A1" and cell2 = "H3", the output should be
solution(cell1, cell2) = false.
'''

def solution(cell1, cell2):
    col1 = ord(cell1[0]) - ord('A')
    col2 = ord(cell2[0]) - ord('A')
    row1 = int(cell1[1]) - 1
    row2 = int(cell2[1]) - 1

    if col1 % 2 == col2 % 2:
        return row1 % 2 == row2 % 2
    else:
        return row1 % 2 != row2 % 2

print(solution("A1", "C3")) # T
print(solution("A1", "H3")) # F