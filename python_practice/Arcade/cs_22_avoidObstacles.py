'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.
'''

def solution(inputArray):
    i = 2
    while True:
        if all(x % i != 0 for x in inputArray):
            return i
        i += 1


print(solution([5, 3, 6, 7, 9])) # 4
print(solution([2, 3])) # 4
print(solution([1, 4, 10, 6, 2])) # 7
